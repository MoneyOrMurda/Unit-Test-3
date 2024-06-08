from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, 'table.table-bordered tbody tr')
    
    def get_cart_items(self):
        return self.find_elements(self.CART_ITEMS)
