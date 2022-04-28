from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from .locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def setup(self):
        self.driver.get(Locators.amazonURL)
        self.clic(Locators.cookie)

    def setdown(self):
        self.driver.quit()

    def clic(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator))).click()
