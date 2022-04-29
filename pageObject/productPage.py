from .locators import Locators
from .basePage import BasePage


class ProductPage(BasePage):

    def addToCart(self):
        self.click(Locators.addToCart)
