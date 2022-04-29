from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from .locators import Locators
from .basePage import BasePage


class CartPage(BasePage):

    def setQuantity(self, quantity):
        self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, Locators.quantitySelector)))
        Select(self.driver.find_element(By.CSS_SELECTOR, Locators.quantitySelector)).select_by_index(quantity)

    def getQuantity(self):
        return Select(self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, Locators.quantitySelector)))).first_selected_option.text
