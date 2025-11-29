import time

from seleniumbase import BaseCase
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(BaseCase):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        time.sleep(3)

    def find(self, value, by=By.CSS_SELECTOR, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_all(self, value, timeout=60):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, value))
        )

    def click(self, value, by=By.CSS_SELECTOR, timeout=60):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def type(self, selector, text):
        self.driver.type(selector, text)

    def close(self):
        self.driver.quit()
