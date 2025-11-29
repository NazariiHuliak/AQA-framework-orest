from .base_page import BasePage

class HomePage(BasePage):

    URL = "https://rozetka.com.ua/"

    SEARCH_FIELD = "input[name='search']"
    SEARCH_BUTTON = "button[type='submit']"

    CATEGORY_LINK = "a.menu-categories__link[href*='computers-notebooks']"

    def open_home(self):
        self.open(self.URL)

    def search(self, query):
        self.type(self.SEARCH_FIELD, query)
        self.click(self.SEARCH_BUTTON)



    def open_category(self):
        self.click(self.CATEGORY_LINK)
