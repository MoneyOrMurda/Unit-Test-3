import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.home_page import HomePage
from page_objects.product_page import ProductPage

class AddToWishlistTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.home_page.go_to_site()

    def test_add_to_wishlist(self):
        self.home_page.search_for_item('MacBook')
        self.product_page.add_to_wishlist()
        # Добавьте проверку успешного добавления в вишлист

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
