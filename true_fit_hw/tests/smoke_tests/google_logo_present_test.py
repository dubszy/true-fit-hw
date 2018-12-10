import unittest

from wdframework.session import Session

from tfhw_main.common.loadables.pageobjects.home_page import HomePage


class GoogleLogoPresentTest(unittest.TestCase):

    def test_google_logo_present(self):
        session = Session("chrome", "https://www.google.com")
        session.start()
        home_page = HomePage(session)

        self.assertTrue(home_page.is_logo_present(), "Google logo was not present on home page")

        session.close()

