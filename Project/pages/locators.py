from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.col-sm-6.login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "div.col-sm-6.register_form")

class ProductPageLocators():
    ADD_BUCKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BUCKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_ADD_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")