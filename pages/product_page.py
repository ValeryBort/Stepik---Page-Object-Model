from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        basket_button.click()

    def should_be_product_name_in_message(self):
        get_name_of_the_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = get_name_of_the_product.text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME)
        assert product_name == message_name.text, "Chosen product is not added to the basket"

    def should_be_correct_price_in_basket(self):
        get_price_of_the_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = get_price_of_the_product.text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE)
        assert product_price == message_price.text, "The basket total is not correct"
