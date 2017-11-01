# Manager level stuff

import os
import hashlib
import datetime
import time
import json
import rssmodule
import settings


class Manager(object):

    def __init__(self, cachedir='cache', testmode=True, timeout=10.0):
        assert type(cachedir) == str
        assert type(testmode) == bool
        assert type(timeout) == float
        self.testmode = testmode
        self.cachedir = cachedir
        if self.testmode:
            self.timeout = 0.1
        else:
            self.timeout = timeout

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

    def touch(self, filename):
        assert type(filename) == str
        path = os.path.join(self.cachedir, filename)
        with open(path, 'a'):
            os.utime(path, None)

    def pretty(self, jsondict):
        print(json.dumps(jsondict, indent=4))

    def checkproviders(self):
        """Return uniq items from providers"""
        now = datetime.datetime.now()
        uniqitems = dict()
        for provider in settings.rssproviders:
            items = dict()
            if self.testmode:
                provider = 'test'
            for key in settings.searchkeys:
                searchphrase = key + '%20' + str(now.year)
                rssurl = settings.rssproviders[provider].format(searchphrase)
                rss = rssmodule.RSS(rssurl)
                time.sleep(self.timeout)
                items = self.check4duplicates(items=rss.getitems())
                for title in items:
                    uniqitems[title] = items[title]
        return uniqitems

    def pushnews(self, items):
        # TODO Where to push? What actions to take?
        self.pretty(items)
        return True
