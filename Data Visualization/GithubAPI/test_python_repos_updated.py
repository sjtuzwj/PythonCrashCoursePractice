import unittest
import requests
url = 'https://api.github.com/search/repositories?q=javascript&sort=stars'
class Test(unittest.TestCase):
    def setUp(self):
        self.r=requests.get(url)
        self.response_dict = self.r.json()
        self.incompletecode=self.response_dict['incomplete_results']
        self.total_count=self.response_dict['total_count']
    def test_status(self):
        self.assertEqual(self.r.status_code,200)
    def test_incomplete(self):
        self.assertFalse(self.incompletecode)
    def test_total_count(self):
        self.assertLess(self.total_count,50000)
unittest.main()
