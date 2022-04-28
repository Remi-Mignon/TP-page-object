from pageObject.homePage import HomePage

from selenium import webdriver


def test_amazon():
    driver = webdriver.Chrome()
    driver.get("https://amazon.fr")
    driver.quit()


def test_page_object():
    driver = webdriver.Chrome()
    home = HomePage(driver)
    home.setup()
    home.openAllMenu()
    home.openBookCategory()
    home.openAllBooks()
    home.setdown()
