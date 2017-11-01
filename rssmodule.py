# RSS related stuff is here

import feedparser as fp
import logging


class RSS(object):
    """RSS related stuff is here"""

    def __init__(self, url='', referrer='http://yandex.ru'):
        self.rssurl = url
        self.rss = fp.parse(self.rssurl, referrer=referrer)
        try:
            self.status = self.rss.status
            if self.status != 200:
                logging.debug(self.status)
                raise Exception(self.status)
        except:
            self.status = None

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
