from .base_page import BasePage

class SearchResultsPage(BasePage):
    SORT_BUTTON = "select[name='sort']"
    PRODUCT_TITLES = ".tile-title.black-link.text-base"

    def sort_by_price(self):
        self.driver.select_option_by_value(self.SORT_BUTTON, "1")

    def get_titles(self):
        return [el.text for el in self.find_all(self.PRODUCT_TITLES)]
