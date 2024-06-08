import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.home_page import HomePage
from page_objects.product_page import ProductPage

class AddCameraToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.home_page.go_to_site()

    def test_add_camera_to_cart(self):
        self.home_page.search_for_item('Camera')
        self.product_page.add_to_cart()
        # Добавьте проверку успешного добавления в корзину

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
