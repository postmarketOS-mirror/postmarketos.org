import collections
import logo
import markdown
import os
import re
import yaml

from atom import AtomFeed

from datetime import datetime
from flask import Flask, render_template, url_for, Response, request, send_file
from os import listdir

# current dir
import page


app = Flask(__name__)
app.config['DARK'] = False

BLOG_CONTENT_DIR = 'content/blog'
EDGE_CONTENT_DIR = 'content/edge'
PAGE_CONTENT_DIR = 'content/page'

REGEX_SPLIT_FRONTMATTER = re.compile(r'^---$', re.MULTILINE)

WIKI_REDIRECTS = {
    "apkbuild-options": "APKBUILD_options",
    "binfmt_misc": "Troubleshooting#sh:_can.27t_create_.2Fproc.2Fsys.2Ffs.2Fbinfmt_misc.2Fregister:_nonexistent_directory",
    "channels.cfg": "Channels.cfg_reference",
    "chat": "Matrix_and_IRC",
    "contribute": "Contributing",
    "debug-shell": "Inspecting_the_initramfs",
    "depends": "Troubleshooting:dependencies",
    "deviceinfo": "Deviceinfo_reference",
    "devicepkg": "Device_specific_package",
    "devices": "Supported_devices",
    "downstreamkernel-prepare": "Downstream_kernel_specific_package#downstreamkernel_prepare",
    "firefox-cfg": "Firefox#postmarketOS_specific_configuration",
    "fstab": "Fstab",
    "git": "Git_repository_move",
    "howto-bump-pkgrel-pkgver": "Create_a_package#When_should_pkgver.2Fpkgrel_get_increased.3F",
    "intro-phosh": "First_Steps_(Phosh)",
    "irc": "Matrix_and_IRC",
    "issues": "How_to_report_issues",
    "matrix": "Matrix_and_IRC",
    "merge": "Merge_Workflow",
    "mvcfg": "Packaging:_Override_Configuration_Files#postmarketos-mvcfg",
    "newarch": "Add_a_new_architecture_to_postmarketOS",
    "oldkernel": "Troubleshooting:host#Host_system_kernel_is_older_than_3.17",
    "on-device-installer": "On-device_installer",
    "osk-port": "Osk-sdl#Porting_to_New_Devices",
    "partitions": "Partition_Layout",
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

def parse_post(post, external_links=False, create_html=True,
               dir=BLOG_CONTENT_DIR):
    """ :returns: a parsed post, something like this:
                  {"html": "<parsedhtmlcode...",
                   "url": "url/to/the/post",
                   "reading_time": "10 min",
                   "year": 2019} """
    with open(os.path.join(dir, post), encoding="utf-8") as handle:
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

    func="blog_post" if dir == BLOG_CONTENT_DIR else "edge_post"

    data['url'] = url_for(func, y=y, m=m, d=d, slug=slug,
                          _external=external_links)
    data['reading_time'] = reading_time(content)
    data['year'] = y

    return data

def get_posts(dir=BLOG_CONTENT_DIR, **kwargs):
    """ :returns: posts categorized by year, looks like:
                  {2019: [post1, post2, ...], 2018: [...], ...}
                  post1, post2 are the posts as returned by parse_post() above.
    """
    posts = sorted(listdir(dir), reverse=True)
    ret = collections.OrderedDict()
    for post in posts:
        parsed = parse_post(post, kwargs, dir=dir)
        year = parsed['year']
        if not year in ret:
            ret[year] = []
        ret[year].append(parsed)
    return ret

@app.route('/blog/')
def blog():
    return render_template('blog.html',
                           year_posts=get_posts(create_html=False),
                           blog_name="blog")

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

@app.route('/blog/2020/07/21/breaking-update-in-edge/')
def blog_post_redirect_edge():
    # Special post that was created in /blog before /edge was introduced, then
    # moved.
    return render_template("redirect.html",
                           url="/edge/2020/07/21/breaking-update-in-edge/")


@app.route('/blog/<y>/<m>/<d>/<slug>/')
def blog_post(y, m, d, slug):
    blog = parse_post('-'.join([y, m, d, slug]) + '.md')
    return render_template('blog-post.html', **blog)

@app.route('/edge/')
def edge():
    return render_template('blog.html',
                           year_posts=get_posts(create_html=False,
                                                dir=EDGE_CONTENT_DIR),
                           blog_name="edge")

@app.route('/edge/feed.atom')
def edge_atom():
    feed = AtomFeed(author='postmarketOS',
                    feed_url=request.url,
                    icon=url_for('logo_svg', _external=True),
                    title='Breaking updates in pmOS edge',
                    url=url_for('edge', _external=True))

    for year, posts in get_posts(external_links=True, dir=EDGE_CONTENT_DIR).items():
        for post in posts:
            feed.add(content=post['html'],
                     content_type='html',
                     title=post['title'],
                     url=post['url'],
                     # midnight
                     updated=datetime.combine(post['date'],
                                              datetime.min.time()))
    return feed.get_response()

@app.route('/edge/<y>/<m>/<d>/<slug>/')
def edge_post(y, m, d, slug):
    edge = parse_post('-'.join([y, m, d, slug]) + '.md', dir=EDGE_CONTENT_DIR)
    return render_template('blog-post.html', **edge)


@app.route('/move.html')
def static_page_move():
    # Do not redirect /move.html to /move/ (as static_page_redirect() would do)
    # because it is a redirect page already. This would break the JS redirect
    # code in content/page/move.md and we have linked to it in all the github
    # projects by now.
    return static_page_or_wiki_redirect("move")


@app.route('/<page>.html')
def static_page_redirect(page):
    # Pages in /content/page/ used to be at postmarketos.org/<page>.html
    return render_template("redirect.html", url=f"/{page}/")


@app.route('/<page>/')
def static_page_or_wiki_redirect(page):
    """ WARNING: This must be the last route! """
    page_path = os.path.join(PAGE_CONTENT_DIR, f"{page}.md")

    # Wiki redirect
    if not os.path.exists(page_path):
        wiki_url = f"https://wiki.postmarketos.org/wiki/{WIKI_REDIRECTS[page]}"
        return render_template('redirect.html', url=wiki_url)

    # Page from content/page/*.md
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
