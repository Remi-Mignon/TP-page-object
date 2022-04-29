from pageObject.homePage import HomePage
from pageObject.basePage import BasePage
from pageObject.booksPage import BooksPage

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

    base.setdown()

    """
    ConfirmationPage
    openCart()
    
    CartPage
    changeQuantity(int
    quantity)
    getQuantity()
    
    assert 2 == (WebElement)
    quantity.text
    
    HomePage.openAllMenu()
    HomePage.openBookCategory()
    HomePage.openAllBooks()
    BooksPage.selectFirstBookNouveautes()
    ProductPage.addToCart()
    ConfirmationPage.openCart()
    CartPage.changeQuantity(2)
    
    assert 2 == CartPage.getQuantity()
    """