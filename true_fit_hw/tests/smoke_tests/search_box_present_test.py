import unittest

from wdframework.session import Session

from tfhw_main.common.loadables.pageobjects.home_page import HomePage


class SearchBoxPresentTest(unittest.TestCase):

    def test_search_box_present(self):
        session = Session("chrome", "https://www.google.com")
        session.start()
        home_page = HomePage(session)

        self.assertTrue(home_page.is_search_input_present(), "Search box was not present on home page")

        session.close()
