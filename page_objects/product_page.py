from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, "//button[@data-original-title='Add to Wish List']")
    ADD_TO_CART_BUTTON = (By.ID, 'button-cart')
    WRITE_REVIEW_LINK = (By.LINK_TEXT, 'Write a review')
    REVIEW_NAME_INPUT = (By.ID, 'input-name')
    REVIEW_TEXTAREA = (By.ID, 'input-review')
    REVIEW_SUBMIT_BUTTON = (By.ID, 'button-review')

    def add_to_wishlist(self):
        self.find_element(self.ADD_TO_WISHLIST_BUTTON).click()

    def add_to_cart(self):
        self.find_element(self.ADD_TO_CART_BUTTON).click()

    def write_review(self, name, review_text):
        self.find_element(self.WRITE_REVIEW_LINK).click()
        self.find_element(self.REVIEW_NAME_INPUT).send_keys(name)
        self.find_element(self.REVIEW_TEXTAREA).send_keys(review_text)
        self.find_element(self.REVIEW_SUBMIT_BUTTON).click()
