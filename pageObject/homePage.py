from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

from .locators import Locators
from .basePage import BasePage


class HomePage(BasePage):

    def openAllMenu(self):
        self.clic(Locators.menu)

    def openBookCategory(self):
        self.clic(Locators.booksMenu)

    def openAllBooks(self):
        self.clic(Locators.allBooksMenu)
