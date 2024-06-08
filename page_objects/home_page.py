from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    SLIDESHOW = (By.ID, 'slideshow0')
    LOGIN_ICON = (By.XPATH, "//a[@title='Личный кабинет']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class='btn btn-default btn-lg']")

    def click_slideshow(self):
        self.find_element(self.SLIDESHOW).click()

    def go_to_login_page(self):
        self.find_element(self.LOGIN_ICON).click()

    def search_for_item(self, item_name):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.click()
        search_input.send_keys(item_name)
        self.find_element(self.SEARCH_BUTTON).click()
