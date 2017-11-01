import unittest
import settings
import rssmodule


class RSSTestCase(unittest.TestCase):
    def setUp(self):
        self.rssurl = 'testrss.xml'
        self.rss = rssmodule.RSS(self.rssurl)


    def test_init(self):
        self.assertIsInstance(self.rss, rssmodule.RSS)
        self.assertEqual(self.rssurl, self.rss.rssurl)

    def test_count(self):
        self.assertEqual(int, type(self.rss.count()))

    def test_titles(self):
        self.assertEqual(list, type(self.rss.titles()))


if __name__ == '__main__':
    unittest.main()
