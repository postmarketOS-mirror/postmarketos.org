from datetime import datetime, timezone
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, register_namespace
from flask import Response


class FeedEntry:
    def __init__(self, content, title, url, content_type, updated):
        self.content = content
        self.title = title
        self.url = url
        self.content_type = content_type
        self.updated = updated

    def generate(self, feed):
        top = SubElement(feed, 'entry')

        title_elem = SubElement(top, "title")
        title_elem.text = self.title
        title_elem.set('type', 'text')

        id_elem = SubElement(top, 'id')
        id_elem.text = self.url

        updated_elem = SubElement(top, 'updated')
        updated_elem.text = self.updated.isoformat()

        link_elem = SubElement(top, 'link')
        link_elem.set('href', self.url)

        content_elem = SubElement(top, 'content')
        content_elem.set('type', self.content_type)
        content_elem.text = self.content


class AtomFeed:
    def __init__(self, title=None, url=None, author=None, icon=None, feed_url=None):
        self.title = title
        self.url = url
        self.author = author
        self.icon = icon
        self.feed_url = feed_url
        self.entries = []
        self.last_updated = None

    def add(self, content, title, url, updated, content_type=None):
        if content_type is None:
            content_type = 'html'

        updated = updated.replace(tzinfo=timezone.utc)

        if self.last_updated is None:
            self.last_updated = updated
        elif updated > self.last_updated:
            self.last_updated = updated

        self.entries.append(FeedEntry(content, title, url, content_type, updated))

    def get_response(self):
        register_namespace('', 'http://www.w3.org/2005/Atom')

        top = Element('feed')
        top.set('xmlns', 'http://www.w3.org/2005/Atom')

        title_elem = SubElement(top, "title")
        title_elem.text = self.title
        title_elem.set('type', 'text')

        id_elem = SubElement(top, 'id')
        id_elem.text = self.feed_url

        updated_elem = SubElement(top, 'updated')
        updated_elem.text = self.last_updated.isoformat()

        link1_elem = SubElement(top, 'link')
        link1_elem.set('href', self.url)

        link2_elem = SubElement(top, 'link')
        link2_elem.set('href', self.feed_url)
        link2_elem.set('rel', 'self')

        author_elem = SubElement(top, 'author')
        author_name_elem = SubElement(author_elem, 'name')
        author_name_elem.text = self.author

        icon_elem = SubElement(top, 'icon')
        icon_elem.text = self.icon

        for entry in self.entries:
            entry.generate(top)

        encoded = tostring(top, xml_declaration=True, encoding='utf-8', method='xml')
        return Response(encoded, mimetype='text/atom')


if __name__ == '__main__':
    _test = AtomFeed(author='postmarketOS bloggers',
                     feed_url='https://example.com/feed.atom',
                     icon='https://example.com/icon.svg',
                     title='postmarketOS Blog',
                     url='https://example.com/blog/')

    _test.add(content='<h1>hi</h1>',
              content_type='html',
              title='test post',
              url='https://example.com/blog/test-post',
              updated=datetime.now())

    print(_test.get_response().response)
