from .locators import Locators
from .basePage import BasePage


class ProductPage(BasePage):

    def addToCart(self):
        self.clic(Locators.addToCart)
