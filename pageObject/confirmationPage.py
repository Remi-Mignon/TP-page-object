from .locators import Locators
from .basePage import BasePage


class ConfirmationPage(BasePage):

    def openCart(self):
        self.click(Locators.cart)
