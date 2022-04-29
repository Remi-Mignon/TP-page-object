from .locators import Locators
from .basePage import BasePage


class BooksPage(BasePage):

    def selectFirstNewBook(self):
        self.click(Locators.firstNewBook)
