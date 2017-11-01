import unittest
import os
import rssmodule
import manager


class RSSTestCase(unittest.TestCase):
    def setUp(self):
        self.rssurl = 'testrss.xml'
        self.rss = rssmodule.RSS(self.rssurl)

    def test_init(self):
        self.assertIsInstance(self.rss, rssmodule.RSS)
        self.assertEqual(self.rssurl, self.rss.rssurl)

    def test_count(self):
        self.assertEqual(int, type(self.rss.count()))

    def test_gettitles(self):
        self.assertEqual(list, type(self.rss.gettitles()))

    def test_getitems(self):
        items = self.rss.getitems()
        self.assertEqual(dict, type(items))
        self.assertNotEqual(dict(), items)
        for title in items:
            link = items[title]
            self.assertEqual(str, type(link))
            self.assertEqual(str, type(title))


class ManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.cachedir = os.path.join('..', 'cachetest')

    def test_clearcache(self):
        # Check if cache dir is created
        if os.path.isdir(self.cachedir):
            os.remove(self.cachedir)
        manager.clearcache(cachedir=self.cachedir)
        self.assertTrue(os.path.isdir(self.cachedir))

        # Write something to self.cachedir

        # Check if the dir is empty

    def test_analyze(self):
        manager.analyze()


if __name__ == '__main__':
    unittest.main()
