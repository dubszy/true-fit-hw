from wdframework.loadables.page import Page
from wdframework.selector import Selector
from wdframework.session import Session


class SearchResultsPage(Page):
    """
    The Google search results page.
    """

    def __init__(self, session: Session):
        super().__init__(session)

        # Selectors #
        self.__results_container = Selector(session, "#search")
        self.__result            = Selector(session, ".g")

    def is_results_present(self):
        """
        Get whether the search results container is present on this page.

        :return: True if the search results container is present, False otherwise
        """
        return self.__results_container.is_present()

    def is_at_least_one_result_present(self):
        """
        Get whether at least one search result is present on the page.

        :return: True if at least one search result is present, False otherwise
        """
        return self.__result.is_present()
