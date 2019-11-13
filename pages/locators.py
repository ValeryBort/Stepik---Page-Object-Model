from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form [type='email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#register_form [type='password']")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#register_form [name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form  .btn")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_NAME = (By.CSS_SELECTOR, "#messages>:nth-child(1) .alertinner > strong:nth-child(1)")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages>:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1) .alertinner")


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    YOUR_BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")






