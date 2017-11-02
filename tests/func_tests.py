import unittest
import os
import sys
sys.path.append(os.path.abspath('..'))
import rssmodule
import manager


class UsageTestCase(unittest.TestCase):
    def setUp(self):
        self.searchkey = 'devops'
        self.year = '2017'
        self.rssurl = 'testrss.xml'

        self.cachedir = os.path.join('..', 'cachetest')
        self.manager = manager.Manager(cachedir=self.cachedir)
        self.manager.clearcache()

    def tearDown(self):
        self.manager.clearcache()
        os.rmdir(self.cachedir)

    def test_read_rss_and_get_titles_and_links(self):
        # Read RSS and discover several items
        rss = rssmodule.RSS(url=self.rssurl)
        self.assertGreater(rss.count(), 0)

        # Get titles of the RSS items
        titles = rss.gettitles()
        self.assertGreater(len(titles), 0)

        # Check if the titles are relevant
        for title in titles:
            self.assertIn(self.searchkey, title.lower())
            self.assertIn(self.year, title.lower())

        # Get magnet links
        items = rss.getitems()
        for title in items.keys():
            link = items[title]
            self.assertIn('magnet:?xt=urn:btih:', link)

    def test_new_items_and_caching(self):
        # Analyze one RSS feed
        rssold = rssmodule.RSS(self.rssurl)
        olditems = rssold.getitems()
        oldrezults = self.manager.check4duplicates(items=olditems)

        self.assertGreater(len(oldrezults), 0)

        # Analyze the same RSS feed again
        rssnew = rssmodule.RSS(self.rssurl)
        newitems = rssnew.getitems()
        newrezults = self.manager.check4duplicates(items=newitems)

        self.assertEqual(0, len(newrezults))

    def test_several_rss_retievals(self):
        # Grab all configured feeds
        items = self.manager.checkproviders()
        self.assertEqual(dict, type(items))

        # Check if the titles are relevant
        for title in items.keys():
            self.assertIn(self.searchkey, title.lower())
            self.assertIn(self.year, title.lower())

        # Check if links are good
        for title in items.keys():
            link = items[title]
            self.assertIn('magnet:?xt=urn:btih:', link)

        # New items discovered and pushed to the master
        self.manager.pushnews(items=items)

if __name__ == '__main__':
    unittest.main()
