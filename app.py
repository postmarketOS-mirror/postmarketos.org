import collections
import logo
import markdown
import os
import re
import yaml

from datetime import datetime
from flask import Flask, render_template, url_for, Response, request, send_file
from werkzeug.contrib.atom import AtomFeed
from os import listdir

# current dir
import page


app = Flask(__name__)
app.config['DARK'] = False

BLOG_CONTENT_DIR = 'content/blog'
PAGE_CONTENT_DIR = 'content/page'

REGEX_SPLIT_FRONTMATTER = re.compile(r'^---$', re.MULTILINE)

WIKI_REDIRECTS = {
    "binfmt_misc": "Troubleshooting#sh:_can.27t_create_.2Fproc.2Fsys.2Ffs.2Fbinfmt_misc.2Fregister:_nonexistent_directory",
    "apkbuild-options": "APKBUILD_options",
    "channels.cfg": "Channels.cfg_reference",
    "chat": "Matrix_and_IRC",
    "debug-shell": "Inspecting_the_initramfs",
    "depends": "Troubleshooting:dependencies",
    "deviceinfo": "Deviceinfo_reference",
    "devicepkg": "Device_specific_package",
    "devices": "Supported_devices",
    "downstreamkernel-prepare": "Downstream_kernel_specific_package#downstreamkernel_prepare",
    "git": "Git_repository_move",
    "howto-bump-pkgrel-pkgver": "Create_a_package#When_should_pkgver.2Fpkgrel_get_increased.3F",
    "irc": "Matrix_and_IRC",
    "matrix": "Matrix_and_IRC",
    "merge": "Merge_Workflow",
    "newarch": "Add_a_new_architecture_to_postmarketOS",
    "oldkernel": "Troubleshooting:host#Host_system_kernel_is_older_than_3.17",
    "on-device-installer": "On-device_installer",
    "osk-port": "Osk-sdl#Porting_to_New_Devices",
    "pmaports.cfg": "Pmaports.cfg_reference",
    "pure-maps": "Pure_Maps",
    "rebase": "Git_workflow#Updating_pmaports_.28rebasing_on_master.29",
    "recoveryzip": "Android_Recovery_Zip_Installation",
    "renamed": "Renamed_Devices",
    "ssh": "SSH",
    "troubleshooting": "Troubleshooting",
    "usbhook": "Inspecting_the_initramfs",
    "vendorkernel": "Vendor_kernel_specific_package",
    "warning-repo": "Troubleshooting#Installed_version_newer_than_the_version_in_the_repositories",
    "warning-repo2": "Troubleshooting#Newer_version_in_binary_package_repositories_than_in_aports_folder",
    "wiki": "Main_Page",
}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/robots.txt')
def robots_txt():
    return send_file('static/robots.txt')

@app.route('/.well-known/dnt-policy.txt')
def dnt_policy():
    return send_file('static/dnt-policy.txt')

@app.route('/.well-known/matrix/server')
def matrix_server():
    return send_file('static/matrix-server.json')

def reading_time(content):
    content = re.sub('<[^<]+?>', '', content)
    words_per_minute = 200
    words = content.split(" ")
    return int(len(words) / words_per_minute)

@app.route('/logo.svg')
def logo_svg():
    return Response(response=logo.create(phone=False), mimetype="image/svg+xml")

def parse_post(post, external_links=False, create_html=True):
    """ :returns: a parsed post, something like this:
                  {"html": "<parsedhtmlcode...",
                   "url": "url/to/the/post",
                   "reading_time": "10 min",
                   "year": 2019} """
    with open(os.path.join(BLOG_CONTENT_DIR, post), encoding="utf-8") as handle:
        raw = handle.read()
    frontmatter, content = REGEX_SPLIT_FRONTMATTER.split(raw, 2)

    data = yaml.load(frontmatter)

    y, m, d, slug = post[:-3].split('-', maxsplit=3)

    if create_html:
        data['html'] = markdown.markdown(content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'
        ], extension_configs={"markdown.extensions.toc": {"anchorlink": True}})
        data['html'] = page.replace(data['html'])

    data['url'] = url_for('blog_post', y=y, m=m, d=d, slug=slug,
                          _external=external_links)
    data['reading_time'] = reading_time(content)
    data['year'] = y

    return data

def get_posts(**kwargs):
    """ :returns: posts categorized by year, looks like:
                  {2019: [post1, post2, ...], 2018: [...], ...}
                  post1, post2 are the posts as returned by parse_post() above.
    """
    posts = sorted(listdir(BLOG_CONTENT_DIR), reverse=True)
    ret = collections.OrderedDict()
    for post in posts:
        parsed = parse_post(post, **kwargs)
        year = parsed['year']
        if not year in ret:
            ret[year] = []
        ret[year].append(parsed)
    return ret

@app.route('/blog/')
def blog():
    return render_template('blog.html',
                           year_posts=get_posts(create_html=False))

@app.route('/blog/feed.atom')
def atom():
    feed = AtomFeed(author='postmarketOS bloggers',
                    feed_url=request.url,
                    icon=url_for('logo_svg', _external=True),
                    title='postmarketOS Blog',
                    url=url_for('blog', _external=True))

    for year, posts in get_posts(external_links=True).items():
        for post in posts:
            feed.add(content=post['html'],
                     content_type='html',
                     title=post['title'],
                     url=post['url'],
                     # midnight
                     updated=datetime.combine(post['date'],
                                              datetime.min.time()))
    return feed.get_response()

@app.route('/blog/<y>/<m>/<d>/<slug>/')
def blog_post(y, m, d, slug):
    blog = parse_post('-'.join([y, m, d, slug]) + '.md')
    return render_template('blog-post.html', **blog)

@app.route('/<page>.html')
def static_page(page):
    with open(os.path.join(PAGE_CONTENT_DIR, page + '.md'),
              encoding="utf-8") as handle:
        raw = handle.read()
    frontmatter, content = REGEX_SPLIT_FRONTMATTER.split(raw, 2)
    data = yaml.load(frontmatter)
    data['html'] = markdown.markdown(content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ], extension_configs={"markdown.extensions.toc": {"anchorlink": True}})
    return render_template('page.html', **data)


@app.route('/<slug>/')
def wiki_redirect(slug):
    """ WARNING: This must be the last route! """
    return render_template('redirect.html', url='https://wiki.postmarketos.org/wiki/' + WIKI_REDIRECTS[slug])
