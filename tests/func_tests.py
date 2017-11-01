import unittest
import rssmodule


class FuncRSSTestCase(unittest.TestCase):
    def setUp(self):
        self.searchkey = 'devops'
        self.year = '2017'
        # self.provider = 'skytorrents.in'
        # self.searchphrase = self.searchkey + '%20' + self.year
        # self.rssurl = settings.rssproviders[self.provider].format(self.searchphrase)
        self.rssurl = 'testrss.xml'

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
        rssold.analyze()

        # Analyze another RSS feed
        rssnew = rssmodule.RSS(self.rssurl)
        rssnew.analyze()

        self.fail('Complete the test')

    @unittest.skip
    def test_rss_analyze(self):
        self.fail('Complete the test')

    @unittest.skip
    def test_several_rss_retieval(self):
        self.fail('Complete the test')

if __name__ == '__main__':
    pass
    # unittest.main()
