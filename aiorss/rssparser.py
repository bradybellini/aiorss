import feedparser
import time

class RSSParser:
    
    link_filter = []
    title_filter = []
    name = ''
    url = ''
    categoriesP = []

    def __init__(self, feed):
        self.feed = feed

    def _check_link(self, entry):
        return not any(x in entry.link for x in self.link_filter)

    def _check_title(self, entry):
        return not any(x in entry.title for x in self.title_filter)

    def _filter_entries(self, entries):
        for i in entries:
            if self._check_link(i):
                yield i

    @staticmethod
    def _get_entry_info(feed, e):
        tags = getattr(e, 'tags', 'null')
        author = getattr(e, 'author', 'not listed')
        if 'published_parsed' in e:
            date = e['published_parsed']
            date = time.strftime('%Y-%m-%d %H:%M:%S', date)
        return {
            'title': e.title,
            'link': e.link,
            'author': author,
            'tags': tags,
            'published': date,
            'summary': e.summary,
            'guid': e.guid
        }

    @property
    def entries(self):
        parsed = feedparser.parse(self.feed)
        filtered_entries = list(self._filter_entries(parsed.entries))
        return [self._get_entry_info(parsed.feed, entry)for entry in filtered_entries]