
class Locators:
    amazonURL = "https://amazon.fr"
    cookie = "#sp-cc-accept"

    #HomePage
    menu = "a#nav-hamburger-menu"
    booksMenu = ".hmenu-item[data-menu-id='10']"
    allBooksMenu = "#hmenu-content > ul.hmenu.hmenu-visible.hmenu-translateX > li:nth-child(3) > a"

    #BooksPage
    firstNewBook = "#a-page > div.a-container > div.a-row.apb-browse-two-col-center-pad > div.a-column.a-span12.aok-float-right.apb-browse-col-pad-left.apb-browse-two-col-center-margin-right > div:nth-child(4) > div > div.a-section.octopus-pc-card.octopus-best-seller-card > div.a-section.octopus-pc-card-content > ul > li:nth-child(2)"

    #ProductPage
    addToCart = "#add-to-cart-button"

    #ConfirmationPage
    cart = "#nav-cart"