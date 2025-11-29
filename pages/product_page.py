from .base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART = "button.buy-button"

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)
