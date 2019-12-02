class Locator(object):
    # Login Page
    LOGIN_MENU = "//*[@id='__next']/div/header/div[3]/div/div[2]/div[2]/span/span"
    LOGIN_SUBMENU = "#__next > div > header > div.Container-sc-1fnsswg-0.itgICN > div > div.Userstyle__Root-xrezqc-0.fRWDhU > div:nth-child(3) > div > button:nth-child(1)"
    EMAIL_FIELD = "#email"
    PASSWORD_FIELD = "#password"
    LOGIN_BTN = "//button[@class='UserModalstyle__RightButton-uq4a18-8 jpHvvv']"

    # Home Page
    CLICK_SEARCHBOX = "#__next > div > header > div.Container-sc-1fnsswg-0.itgICN > div > div.Middle__LeftContainer-sc-1poi789-2.iXVTaA > div.FormSearch__Root-hwmlek-0.eqgiix > div > input"
    INPUT_KEYWORD = "#__next > div > header > div.Container-sc-1fnsswg-0.itgICN > div > div.Middle__LeftContainer-sc-1poi789-2.iXVTaA > div.FormSearch__Root-hwmlek-0.eqgiix > div > button"
    CLICK_SEARCHBTN = "#ants-product-list > div:nth-child(1) > a > div.content > span > img"
    ADD_TO_CART = "#\#mainAddToCart"
    SELECT_TO_REMOVE_FROM_CART = "#header-cart > a > div > button"
    REMOVE_CARTBTN = "#shopping-cart > div > div.col-right > div.box-info-product > p.action > a.btn.btn-link.btn-item-delete"
