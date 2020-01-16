import faker

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "URL not contains 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Login registration is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONF_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()
