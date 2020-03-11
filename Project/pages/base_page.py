import math
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Формула из учебного задания. Была дана именно из курса.
def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")

#Базовый класс, содержащий все основные методы
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): #открыть url
        self.browser.get(self.url)

    def is_element_present(self, how, what): #проверка на наличие элемента
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return  False
        return True

    def click_element(self, how, what): #клик по элементу
        try:
            self.browser.find_element(how, what).click()
        except (NoSuchElementException):
            return  False
        return True

    def is_not_element_present(self, how, what, timeout=4): #проверка на отсутствие элемента
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4): #ожидание отсутствия элемента
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self): #переход на стартовую страницу
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self): #проверка ссылки в адресной строке
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self): #переход на страницу корзины
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK_INVALID)
        link.click()

    def should_be_authorized_user(self): #проверка на авторизацию пользователя через наличие иконки юзера
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"