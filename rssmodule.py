# RSS related stuff is here

import feedparser as fp


class RSS(object):
    """RSS related stuff is here"""

    def __init__(self, url=''):
        self.rssurl = url
        self.rss = fp.parse(self.rssurl)

    def count(self):
        return len(self.rss.entries)

    def gettitles(self):
        titles = list()
        for entry in self.rss.entries:
            titles.append(entry['title'])
        return titles

    def getitems(self):
        items = dict()
        for entry in self.rss.entries:
            items[entry['title']] = entry['link']
        return items

    def analyze(self):
        pass
