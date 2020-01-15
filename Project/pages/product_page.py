from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_bucket(self):
        self.click_element(*ProductPageLocators.ADD_BUCKET), "Button 'Add Bucket' is not presented"

    def should_be_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_bucket = self.browser.find_element(*ProductPageLocators.PRICE_BUCKET).text
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_add_book = self.browser.find_element(*ProductPageLocators.NAME_ADD_BOOK).text
        assert price, "price not found"
        assert price_bucket == price, f"price_bucket{price_bucket} not equal price {price}"
        assert name_add_book == name_book, "name book not equal name add book"