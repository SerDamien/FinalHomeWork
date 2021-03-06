from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_bucket(self): #проверка на наличие кнопки "Добавить в корзину"
        self.click_element(*ProductPageLocators.ADD_BUCKET), "Button 'Add Bucket' is not presented"

    def should_be_price(self): #проверка на наличие цены, и соответствия итоговой цены и цены товара, проверка на соответствие наименования товара
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_bucket = self.browser.find_element(*ProductPageLocators.PRICE_BUCKET).text
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_add_book = self.browser.find_element(*ProductPageLocators.NAME_ADD_BOOK).text
        assert price, "price not found"
        assert price_bucket == price, f"price_bucket{price_bucket} not equal price {price}"
        assert name_add_book == name_book, "name book not equal name add book"

    def should_not_be_success_message(self): #проверка на отсутствие сообщения
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_2(self): #проверка на отсутствие сообщения 2
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappeared"

