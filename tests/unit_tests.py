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
        self.manager = manager.Manager(cachedir=self.cachedir)
        self.manager.clearcache()

        self.rssurl = 'testrss.xml'
        self.rss = rssmodule.RSS(self.rssurl)
        self.rssitems = self.rss.getitems()

    def tearDown(self):
        self.manager.clearcache()

    def test_clearcache(self):
        # Check if cache dir is created
        self. manager.clearcache()
        self.assertTrue(os.path.isdir(self.cachedir))

        # Write something to self.cachedir and clear cache
        filepath = os.path.join(self.cachedir, 'test.txt')
        self.manager.touch(filename='test.txt')

        self.manager.clearcache()
        self.assertFalse(os.path.isfile(filepath))

    def test_check4duplicates(self):
        uniqitems = self.manager.check4duplicates(self.rssitems)
        self.assertEqual(dict, type(uniqitems))
        self.assertGreater(len(uniqitems.keys()), 0)


if __name__ == '__main__':
    unittest.main()
