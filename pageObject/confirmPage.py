from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmPage:

    country_box = (By.XPATH, "//input[@id='country']")
    suggestions = (By.XPATH, "//div[@class='suggestions']/ul")
    country_to_select = (By.CSS_SELECTOR, "a")
    agree_terms = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button= (By.XPATH, "//input[@value='Purchase']")
    test_success = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def inputCountryInitials(self, timeout = 10):
        #Wait until elements are visible and clickable
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(ConfirmPage.country_box)
        ).send_keys("Sw")

    def selectCountry(self, timeout = 20):
        #Wait until suggestion list is visible and clickable
        suggestion_list = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(ConfirmPage.suggestions)
        )

        for suggestion in suggestion_list:
            if suggestion.text.strip() == 'Switzerland':
                suggestion.find_element(*ConfirmPage.country_to_select).click()

    def agreeTerms(self):
        self.driver.find_element(*ConfirmPage.agree_terms).click()

    def clickPurchase(self):
        self.driver.find_element(*ConfirmPage.purchase_button).click()

    def testSucces(self):
        return self.driver.find_element(*ConfirmPage.test_success).text
    
