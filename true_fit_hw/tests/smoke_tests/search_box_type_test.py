import unittest

from wdframework.session import Session

from tfhw_main.common.loadables.pageobjects.home_page import HomePage


class SearchBoxTypeTest(unittest.TestCase):

    def test_search_box_type(self):
        session = Session("chrome", "https://www.google.com")
        session.start()
        home_page = HomePage(session)
        home_page.type_in_search("True Fit")

        self.assertEqual(home_page.get_search_input_text(), "True Fit")
