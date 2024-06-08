import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class TestRunner:
    def __init__(self):
        self.test_suite = unittest.TestSuite()

    def add_tests(self, tests):
        for test in tests:
            self.test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test))

    def run_tests(self, browser='chrome'):
        if browser == 'chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise ValueError("Unsupported browser!")

        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(self.test_suite)
        driver.quit()

if __name__ == '__main__':
    from tests.test_add_to_wishlist import AddToWishlistTest
    from tests.test_add_camera_to_cart import AddCameraToCartTest
    from tests.test_add_tablet_to_cart import AddTabletToCartTest
    from tests.test_add_htc_to_cart import AddHtcToCartTest
    from tests.test_write_review import WriteReviewTest

    runner = TestRunner()
    runner.add_tests([
        AddToWishlistTest,
        AddCameraToCartTest,
        AddTabletToCartTest,
        AddHtcToCartTest,
        WriteReviewTest
    ])
    
    # Запуск тестов в Chrome
    runner.run_tests(browser='chrome')

    # Запуск тестов в Firefox
    runner.run_tests(browser='firefox')
