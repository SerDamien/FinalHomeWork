from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.col-sm-6.login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "div.col-sm-6.register_form")