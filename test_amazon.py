from pageObject.homePage import HomePage
from pageObject.basePage import BasePage
from pageObject.booksPage import BooksPage
from pageObject.confirmationPage import ConfirmationPage
from pageObject.cartPage import CartPage
from pageObject.productPage import ProductPage

from selenium import webdriver


def test_amazon():
    driver = webdriver.Chrome()
    driver.get("https://amazon.fr")
    driver.quit()


def test_page_object():
    driver = webdriver.Chrome()
    base = BasePage(driver)
    base.setup()

    home = HomePage(driver)
    home.openAllMenu()
    home.openBookCategory()
    home.openAllBooks()

    books = BooksPage(driver)
    books.selectFirstNewBook()

    product = ProductPage(driver)
    product.addToCart()

    confirmation = ConfirmationPage(driver)
    confirmation.openCart()

    quantity = "2"
    cart = CartPage(driver)
    cart.setQuantity(quantity)

    assert cart.getQuantity() == quantity

    base.setdown()