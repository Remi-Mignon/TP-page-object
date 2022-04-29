
class Locators:
    #BasePapge
    amazonURL = "https://amazon.fr"
    cookie = "#sp-cc-accept"

    #HomePage
    menu = "a#nav-hamburger-menu"
    booksMenu = ".hmenu-item[data-menu-id='10']"
    allBooksMenu = "#hmenu-content > ul.hmenu.hmenu-visible.hmenu-translateX > li:nth-child(3) > a"

    #BooksPage
    firstNewBook = "li.octopus-pc-item:first-of-type"

    #ProductPage
    addToCart = "#add-to-cart-button"

    #ConfirmationPage
    cart = "#nav-cart"

    #CartPage
    quantitySelector = "#quantity"