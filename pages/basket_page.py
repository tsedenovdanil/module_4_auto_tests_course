from .base_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Basket not empty")

    def is_basket_message_present(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Message is not presented")
