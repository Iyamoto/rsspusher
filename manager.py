# Manager level stuff

import os


def clearcache(cachedir=''):
    assert type(cachedir) == str
    if cachedir and not os.path.isfile(cachedir):
        if os.path.isdir(cachedir):
            for f in os.listdir(cachedir):
                os.remove(os.path.join(cachedir, f))
        else:
            os.mkdir(cachedir)


def analyze(items=None):
    pass


def grabrss():
    # self.provider = 'skytorrents.in'
    # self.searchphrase = self.searchkey + '%20' + self.year
    # self.rssurl = settings.rssproviders[self.provider].format(self.searchphrase)
    pass


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)