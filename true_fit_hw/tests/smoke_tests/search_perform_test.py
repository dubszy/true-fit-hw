import unittest

from wdframework.session import Session

from tfhw_main.common.loadables.pageobjects.home_page import HomePage


class SearchPerformTest(unittest.TestCase):

    def test_search_perform(self):
        session = Session("chrome", "https://www.google.com")
        session.start()
        home_page = HomePage(session)
        search_results_page = home_page.perform_search("True Fit")

        self.assertTrue(
            search_results_page.is_results_present(), "Results container was not present on the search results page")

        self.assertTrue(
            search_results_page.is_at_least_one_result_present(), "No results present on the search results page")
