from selenium.webdriver.support import expected_conditions as ExpectedCondition
from wdframework.loadables.page import Page
from wdframework.selector import Selector
from wdframework.session import Session

from .search_results_page import SearchResultsPage


class HomePage(Page):
    """
    The Google home page.
    """

    def __init__(self, session: Session):
        super().__init__(session)

        # Selectors #
        self.__main_content  = Selector(session, "#main")
        self.__listbox       = Selector(session, "[role='listbox']")
        self.__logo          = Selector(session, "#hplogo")
        self.__search_input  = Selector(session, "[name='q']")
        # These are a little brittle, but there are two of each of these buttons on the page, and all the class names
        # and other identifying factors are randomly generated, so these are the only selectors we can rely on
        # Note that 'btnK' and 'btnI' are /not/ randomly generated
        self.__search_button = Selector(session, "form > div > div > div > center > input[name='btnK']")
        self.__lucky_button  = Selector(session, "form > div > div > div > center > input[name='btnI']")

    def is_logo_present(self):
        """
        Get whether the Google logo is present on this page.

        :return: True if the logo is present, False otherwise
        """
        return self.__logo.is_present()

    def is_search_input_present(self):
        """
        Get whether the search input field is present on this page.

        :return: True if the search input field is present, False otherwise
        """
        return self.__search_input.is_present()

    def get_search_input_text(self):
        """
        Get the text currently in the search input field on this page.

        :return: The text currently in the search input field
        """
        self.__search_input.wait_until(ExpectedCondition.visibility_of_element_located)
        return self.__search_input.get_text()

    def type_in_search(self, text):
        """
        Type into the search input field. This does not perform a search.

        :param text: The text to type

        :return: This instance
        """
        self.__search_input.wait_until(ExpectedCondition.visibility_of_element_located)
        self.__search_input.send_keys(text)
        self.__search_input.wait_until(ExpectedCondition.text_to_be_present_in_element_value, text)
        return self

    def perform_search(self, text):
        """
        Type into the search input field and perform a search.

        :param text: The text to type

        :return: A new instance of SearchResultsPage
        """
        self.type_in_search(text)
        self.__listbox.wait_until(ExpectedCondition.visibility_of_element_located)  # Wait until the listbox is present
        self.type_in_search("\ue00c")  # Send 'esc' to get rid of the suggestions listbox
        self.__listbox.wait_until(ExpectedCondition.invisibility_of_element_located)  # Wait until the listbox is gone
        self.__search_button.wait_until(ExpectedCondition.element_to_be_clickable)
        self.__search_button.click()
        return SearchResultsPage(self.get_session())

    def im_feeling_lucky(self, text):
        """
        Type into the search input field and perform an "I'm Feeling Lucky" search.

        :param text: The text to type

        :return: A new instance of Page (this is as specific as possible, since the page this method sends the browser
        to is unknown)
        """
        self.type_in_search(text)
        self.__listbox.wait_until(ExpectedCondition.visibility_of_element_located)  # Wait until the listbox is present
        self.type_in_search("\ue00c")  # Send 'esc' to get rid of the suggestions listbox
        self.__listbox.wait_until(ExpectedCondition.invisibility_of_element_located)  # Wait until the listbox is gone
        self.__lucky_button.wait_until(ExpectedCondition.element_to_be_clickable)
        self.__lucky_button.click()
        # We have no idea where we'll end up, so the most specific page we can return is Page
        return Page(self.get_session())
