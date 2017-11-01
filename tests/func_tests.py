import unittest
import settings
import rssmodule


class RSSTestCase(unittest.TestCase):
    def setUp(self):
        self.provider = 'skytorrents.in'
        self.searchkey = 'devops'
        self.year = '2017'
        self.searchphrase = self.searchkey + '%20' + self.year
        # self.rssurl = settings.rssproviders[self.provider].format(self.searchphrase)
        self.rssurl = 'testrss.xml'
        self.rss = rssmodule.RSS(self.rssurl)

    def test_read_rss_and_get_titles(self):
        # Read RSS and discover several items
        rss = rssmodule.RSS(url=self.rssurl)
        self.assertGreater(rss.count(), 0)

        # Get titles of the RSS items
        self.assertGreater(len(rss.titles()), 0)

        # Check if the titles are relevant
        for title in rss.titles():
            self.assertIn(self.searchkey, title.lower())

        # Get magnet links

        self.fail('Write the test')


if __name__ == '__main__':
    pass
    # unittest.main()
