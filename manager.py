# Manager level stuff

import os
import hashlib
import datetime
import time
import json
import logging
import rssmodule
import settings


class Manager(object):

    def __init__(self, cachedir='cache', testmode=True, timeout=60):
        assert type(cachedir) == str
        assert type(testmode) == bool
        self.testmode = testmode
        self.cachedir = cachedir
        if self.testmode:
            self.timeout = 0.1
        else:
            self.timeout = float(timeout)

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
            if self.testmode:
                provider = 'test'
            else:
                if provider == 'test':
                    continue
            for key in settings.searchkeys:
                searchphrase = key + '%20' + str(now.year)
                rssurl = settings.rssproviders[provider].format(searchphrase)
                logging.debug(rssurl)
                try:
                    referrer = 'https://www.skytorrents.in/search/all/ad/1/?l=en-us&q={}'.format(key)
                    rss = rssmodule.RSS(rssurl, referrer=referrer)
                except:
                    logging.debug('Skipping')
                    continue
                logging.debug(str(rss.count()))
                items = self.check4duplicates(items=rss.getitems())
                for title in items:
                    logging.debug(title)
                    uniqitems[title] = items[title]
                time.sleep(self.timeout)
        return uniqitems

    def pushnews(self, items):
        # TODO Where to push? What actions to take?
        self.pretty(items)
        return True

    def updatelocalstate(self, statepath='state.json', data=None):
        if data is None:
            return

        if os.path.isfile(statepath):
            with open(statepath, 'r') as infile:
                state = json.load(infile)
        else:
            state = dict()

        z = state.copy()
        z.update(data)

        # Save updated state locally
        with open(statepath, 'w') as outfile:
            json.dump(z, outfile)

        return len(z)


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    slave = Manager(cachedir='cache', testmode=False, timeout=1*60)
    news = slave.checkproviders()
    slave.pushnews(items=news)
    slave.updatelocalstate(data=news)
