import unittest
import rssmodule


class RSSTestCase(unittest.TestCase):
    def setUp(self):
        self.searchkey = 'devops'
        self.year = '2017'
        # self.provider = 'skytorrents.in'
        # self.searchphrase = self.searchkey + '%20' + self.year
        # self.rssurl = settings.rssproviders[self.provider].format(self.searchphrase)
        self.rssurl = 'testrss.xml'
        self.rss = rssmodule.RSS(self.rssurl)

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

    def test_caching(self):
        self.fail('Complete the test')


if __name__ == '__main__':
    pass
    # unittest.main()
