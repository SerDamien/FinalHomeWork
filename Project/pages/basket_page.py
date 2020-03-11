from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self): #проверка на наличие продукта в корзине
        assert self.is_not_element_present(*BasketPageLocators.GET_PRODUCT), \
        "Product in basket"

    def should_text_empty_basket(self): #проверка на то, что корзина не пустая
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
        "Basket not empty"