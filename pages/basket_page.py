from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "There are products in basket, but should not be"

    def should_be_your_basket_is_empty_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.YOUR_BASKET_IS_EMPTY_MESSAGE)
        assert "Your basket is empty" in empty_message.text, "The basket is not empty"