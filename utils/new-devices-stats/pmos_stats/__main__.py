import glob
import subprocess
import os
import json

import requests

import pmos_stats.chart as chart
import argparse
import re
import sys

cli = argparse.ArgumentParser(description="postmarketOS Stats generator")
subparsers = cli.add_subparsers(dest='subcommand')
wiki_cache = None


def subcommand(args=None, parent=subparsers):
    args = args if args else []

    def decorator(func):
        name = func.__name__.replace('_', '-')
        parser = parent.add_parser(name, description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)

    return decorator


def argument(*name_or_flags, **kwargs):
    return ([*name_or_flags], kwargs)


def init():
    if not os.path.isdir('pmaports'):
        command = ['git', 'clone', 'https://gitlab.com/postmarketOS/pmaports.git']
        subprocess.run(command)


def get_current_commit():
    command = ['git', 'rev-parse', 'HEAD']
    stdout = subprocess.check_output(command, cwd='pmaports')
    return stdout.decode("utf-8").rstrip()


def get_subject(commit):
    command = ['git', 'log', '-1', '--pretty=%s', commit]
    stdout = subprocess.check_output(command, cwd='pmaports')
    return stdout.decode("utf-8").rstrip()


def get_commit_per_day(start_ref, end_ref):
    command = ['git', 'log', '--reverse', '--ancestry-path', '{}..{}'.format(start_ref, end_ref)]
    command.append("--pretty=format:'%h %cd'")
    command.append("--date=format:'%Y-%m-%d'")
    raw = subprocess.check_output(command, universal_newlines=True, cwd='pmaports')
    result = []
    last_date = ''
    for line in raw.splitlines(keepends=False):
        c_hash, c_date = line.split(' ')
        if c_date != last_date:
            result.append((c_hash.replace("'", ''), c_date.replace("'", '')))
            last_date = c_date
    return result


def get_value(git_ref):
    command = ['git', 'checkout', git_ref]
    subprocess.check_output(command, cwd='pmaports')
    if os.path.isdir('pmaports/device'):
        devices = len(glob.glob('pmaports/device/device-*'))
        kernels = len(glob.glob('pmaports/device/linux-*'))
        kernels += len(glob.glob('pmaports/main/linux-*'))
        return devices
    devices = len(glob.glob('pmaports/device-*'))
    return devices


def get_devices_on_ref(ref):
    command = ['git', 'checkout', ref]
    subprocess.check_output(command, cwd='pmaports')
    devices = glob.glob('pmaports/device/device-*')
    result = set()
    for device in devices:
        code = device.replace('pmaports/device/device-', '')
        result.add(code)
    return result


def get_device_name(code):
    infofile = 'pmaports/device/device-{}/deviceinfo'.format(code)
    with open(infofile) as handle:
        raw = handle.read()
    name = re.search(r'deviceinfo_name="([^"]+)"', raw)
    return name.group(1)


def get_device_wiki_page(device):
    global wiki_cache
    if not wiki_cache:
        wiki_cache = {}
        raw = requests.get(
            'https://wiki.postmarketos.org/index.php?title=Special:CargoExport&tables=Devices&&fields=_pageName%3DPage%2CCodename&&order+by=%60cargo__Devices%60.%60Manufacturer%60%2C+%60cargo__Devices%60.%60Name%60&limit=5000&format=json').content.decode()

        # There is UTF-8 multibyte spacing in the table somehow
        clean = raw.encode('ascii', 'ignore').decode()

        for row in json.loads(clean):
            for codename in row['Codename'].split(","):
                codename = codename.strip()
                pagename = row['Page'].replace(' ', '_')
                pagename = row['Page'].replace("'", '&39;') # otherwise screws up markdown
                url = 'https://wiki.postmarketos.org/wiki/{}'.format(pagename)
                wiki_cache[codename] = url

    if device in ['nokia-n9', 'nokia-n950']:
        return 'https://wiki.postmarketos.org/wiki/Nokia_N9'
    if device == 'samsung-p4wifi':
        return 'https://wiki.postmarketos.org/wiki/Samsung_Galaxy_Tab_10.1%22_(samsung-p4wifi)'
    if device == 'ouya-ouya':
        return 'https://wiki.postmarketos.org/wiki/Ouya_(ouya-ouya)'
    if device in ['raspberry-pi3', 'raspberry-pi']:
        return 'https://wiki.postmarketos.org/wiki/Raspberry_Pi'
    if device == 'samsung-i8200':
        return 'https://wiki.postmarketos.org/wiki/Samsung_Galaxy_SIII_mini_Value_Edition_(samsung-i8200)'
    if device == 'semc-smultron':
        return 'https://wiki.postmarketos.org/wiki/Sony_Ericsson_Xperia_mini_(semc-smultron)'
    if device == 'planet-geminipda':
        return 'https://wiki.postmarketos.org/wiki/Planet_Computers_Gemini_PDA_(planet-geminipda)'

    if device not in wiki_cache:
        print("ERROR: device " + device + " not found in wiki!")
        print("Edit get_device_wiki_page() in and add the link there: " + __file__)
        exit(1)

    return wiki_cache[device]


@subcommand([argument('filename', help="Output filename")])
def devices_over_time(args):
    init()

    initial_commit = '1c0ff6aa23b9e3ae6900f845021a587bb1280495'
    commits = get_commit_per_day(initial_commit, 'master')
    dataset = []
    for commit in commits:
        value = get_value(commit[0])
        if value is not None:
            dataset.append((commit[1], value))

    c = chart.Chart(dataset)
    with open(args.filename, 'w') as handle:
        handle.write(c.generate())


@subcommand([argument('fromref', help='Oldest ref to check'),
             argument('--md', help='Create markdown list', action="store_true")])
def new_devices(args):
    init()
    a = get_devices_on_ref(args.fromref)
    b = get_devices_on_ref('master')

    added = b - a
    deleted = a - b

    if args.md:
        start = args.fromref
        subject_start = get_subject(start)
        master = get_current_commit()
        subject_master = get_subject(master)
        print("<!-- Generated with: 'pmos-stats " + " ".join(sys.argv[1:]) + "'")
        print("     Start subject: " + subject_start)
        print("     Current master (for next time): " + master)
        print("     Current subject: " + subject_master + " -->")
        print("")
        for device in sorted(added):
            name = get_device_name(device)
            url = get_device_wiki_page(device)
            print('* [{name} `{code}`]({url})'.format(name=name, code=device, url=url))
        print('')
        print('*Thanks to: everyone who ported these devices, see the'
              ' contributors section in each device\'s wiki page.*')

        if deleted:
            print("\nNOTE: the following devices have been deleted (renamed?),"
                  " don't forget to remove them from the list:")
            for device in sorted(deleted):
                print(device)
            print("\nSee also: https://postmarketos.org/renamed")

        # In the 2 year blog post, the script printed asus-z00vd, although that
        # was already mentioned in the 600 days post?! Maybe stuff was renamed,
        # not really worth investigating now. I've double checked all entries,
        # and all others were reported properly.
        print()
        print(" #### NOTE: DOUBLE CHECK THIS LIST! #### ");
        print()

        return

    print('--added--')
    for device in sorted(added):
        name = get_device_name(device)
        print("{} ({})".format(device, name))

    print('\n--deleted--')
    for device in sorted(deleted):
        print(device)


if __name__ == "__main__":
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)
