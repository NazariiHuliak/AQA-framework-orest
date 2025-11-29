from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re, time

from .base_page import BasePage


class SearchResultsPage(BasePage):
    SORT_BUTTON = "#sort"
    PRODUCT_TITLES = ".tile-title.black-link.text-base"
    PRODUCT_PRICES = ".price.text-2xl.color-red"

    LANGUAGE_TOGGLE = "[data-testid='lang_btn']"
    LANGUAGE_RU = "//button[normalize-space()='RU']"

    def sort_by_price_asc(self):
        select_element = self.find(by=By.ID, value="sort")
        select = Select(select_element)
        select.select_by_value("cheap")

    def sort_by_price_desc(self):
        select_element = self.find(by=By.ID, value="sort")
        select = Select(select_element)
        select.select_by_value("expensive")

    def get_titles(self):
        return [el.text for el in self.find_all(self.PRODUCT_TITLES)]

    def get_prices(self):
        prices = [el.text for el in self.find_all(self.PRODUCT_PRICES)]
        return [int(re.sub(r"\D", "", p)) for p in prices]

    def change_language(self):
        time.sleep(2)
        self.click(self.LANGUAGE_TOGGLE)
        time.sleep(2)
        self.click(by=By.XPATH, value=self.LANGUAGE_RU)

    def get_language(self):
        return self.find(by=By.XPATH, value=self.LANGUAGE_RU).text
