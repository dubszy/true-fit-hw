import unittest

from wdframework.session import Session

from tfhw_main.common.loadables.pageobjects.home_page import HomePage


class SearchNoInputTest(unittest.TestCase):

    def test_search_no_input(self):
        session = Session("chrome", "https://www.google.com")
        session.start()
        home_page = HomePage(session)
        search_results_page = home_page.perform_search("")

        self.assertFalse(search_results_page.is_results_present(), "Results container was present, even though search "
                                                                   "should not have been performed")

        self.assertFalse(search_results_page.is_at_least_one_result_present(), "At least one search result was present,"
                                                                               " even though search should not have "
                                                                               "been performed")

        self.assertTrue(home_page.is_logo_present(), "Logo was not present on the home page")

        self.assertTrue(home_page.is_search_input_present(), "Search input was not present on the home page")

        session.close()
