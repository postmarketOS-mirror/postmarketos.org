from flask_frozen import Freezer
from app import app, BLOG_CONTENT_DIR, PAGE_CONTENT_DIR, WIKI_REDIRECTS
from os import listdir


freezer = Freezer(app)
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_BASE_URL'] = 'https://postmarketos.org/'


@freezer.register_generator
def blog_post():
    for f in listdir(BLOG_CONTENT_DIR):
        y, m, d, *title = f[:-3].split('-')
        slug = '-'.join(title)
        yield { 'y': y, 'm': m, 'd': d, 'slug': slug }

@freezer.register_generator
def static_page_redirect():
    for f in listdir(PAGE_CONTENT_DIR):
        page = f[:-3]
        yield { 'page': page }

@freezer.register_generator
def static_page_or_wiki_redirect():
    for f in listdir(PAGE_CONTENT_DIR):
        slug = f[:-3]
        yield {'slug': slug}
    for slug, redirect in WIKI_REDIRECTS.items():
        yield {'slug': slug}


def check_conflicts():
    slugs = ["blog", "edge", "static"]

    for f in listdir(PAGE_CONTENT_DIR):
        slug = f[:-3]
        if slug in slugs:
            raise RuntimeError(f"Page {slug}.md generates conflicting URL!")
        slugs.append(slug)

    for slug, redirect in WIKI_REDIRECTS.items():
        if slug in slugs:
            raise RuntimeError(f"WIKI_REDIRECTS: '{slug}' generates"
                                " conflicting URL!")


if __name__ == '__main__':
    print("Checking for conflicting URLs...")
    check_conflicts()
    print("Freezing the website to 'docs'...")
    freezer.freeze()
