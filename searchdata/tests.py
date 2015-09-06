import os
from django.test import TestCase
from searchdata.utils import search


class SearchTestCase(TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), 'testfile.csv')
        self.first_name = "James"
        self.first_name_bad = "James333"
        self.last_name = "Butt"
        self.phone = "504-621-8927"
        self.address = "6649 N Blue Gum St"

    def test_data_found(self):
        """Data found according to search"""
        status = search(self.path, self.first_name, self.last_name, self.phone, self.address)
        assert status

    def test_data_not_found(self):
        """Data found according to search"""
        status = search(self.path, self.first_name_bad, self.last_name, self.phone, self.address)
        assert not status
