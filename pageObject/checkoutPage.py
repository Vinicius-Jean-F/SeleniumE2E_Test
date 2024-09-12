from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pageObject.confirmPage import ConfirmPage
class CheckoutPage:

    cardtitles = (By.XPATH, "//app-card/div[@class='card h-100']/div[@class='card-body']/h4/a")
    cardfooter = (By.XPATH, "div/button")
    checkoutbutton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    successbutton = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardtitles)
    
    def clickCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardfooter).click()
        
    def clickCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton).click()
    
    def clickSuccessButton(self):
        self.driver.find_element(*CheckoutPage.successbutton).click()
        confirmPage = ConfirmPage(self.driver)

        return confirmPage


    


    