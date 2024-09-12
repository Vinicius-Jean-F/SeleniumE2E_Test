from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.checkoutPage import CheckoutPage

class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self, timeout=10):
        # Wait until the element is present and clickable
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(HomePage.shop)
        ).click()

        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage