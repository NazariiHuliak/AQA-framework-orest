from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = "div.cart-product__title"

    def get_items(self):
        return [el.text for el in self.find_all(self.CART_ITEMS)]
