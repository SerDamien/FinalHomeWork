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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")

class BasketPageLocators():
    GET_PRODUCT = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")