# Manager level stuff

import os
import hashlib


class Manager(object):

    def __init__(self, cachedir='cache'):
        assert type(cachedir) == str
        self.cachedir = cachedir

    def clearcache(self):
        if self.cachedir and not os.path.isfile(self.cachedir):
            if os.path.isdir(self.cachedir):
                for f in os.listdir(self.cachedir):
                    os.remove(os.path.join(self.cachedir, f))
            else:
                os.mkdir(self.cachedir)

    def check4duplicates(self, items=None):
        """Checks dictionary for duplicates in cache"""
        if items is None:
            return {}
        uniqitems = dict()
        for title in items:
            titlehash = hashlib.md5(title.encode('utf-8')).hexdigest()
            path = os.path.join(self.cachedir, titlehash)
            if not os.path.isfile(path):
                self.touch(filename=titlehash)
                uniqitems[title] = items[title]
        return uniqitems

    def checkrss(self):
        # self.provider = 'skytorrents.in'
        # self.searchphrase = self.searchkey + '%20' + self.year
        # self.rssurl = settings.rssproviders[self.provider].format(self.searchphrase)
        # items = analyze()
        pass

    def touch(self, filename):
        assert type(filename) == str
        path = os.path.join(self.cachedir, filename)
        with open(path, 'a'):
            os.utime(path, None)
