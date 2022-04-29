from .locators import Locators
from .basePage import BasePage


class HomePage(BasePage):

    def openAllMenu(self):
        self.click(Locators.menu)

    def openBookCategory(self):
        self.click(Locators.booksMenu)

    def openAllBooks(self):
        self.click(Locators.allBooksMenu)
