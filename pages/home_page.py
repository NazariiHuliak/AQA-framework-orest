from .base_page import BasePage

class HomePage(BasePage):

    URL = "https://rozetka.com.ua/"

    SEARCH_FIELD = "input[name='search']"
    SEARCH_BUTTON = "button[type='submit']"
    LANGUAGE_TOGGLE = "button.header__lang"

    CATEGORY_LINK = "a.menu-categories__link[href*='computers-notebooks']"

    def open_home(self):
        self.open(self.URL)

    def search(self, query):
        self.type(self.SEARCH_FIELD, query)
        self.click(self.SEARCH_BUTTON)

    def change_language(self):
        self.click(self.LANGUAGE_TOGGLE)

    def open_category(self):
        self.click(self.CATEGORY_LINK)
