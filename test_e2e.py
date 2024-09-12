import pytest
from utilities.BaseClass import BaseClass
from pageObject.homePage import HomePage
from pageObject.checkoutPage import CheckoutPage

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestOne(BaseClass):
    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        #cards = self.driver.find_elements(By.XPATH, "//app-card/div[@class='card h-100']")
        checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()

        for card in cards:
            card_name = card
            
            if card_name == 'Blackberry':
                #card.find_element(By.XPATH, "div/button").click()
                checkoutPage.clickCardFooter()
            
            

        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        checkoutPage.clickCheckoutButton()

        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        checkoutPage.clickSuccessButton()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='country']"))
        ).send_keys("Sw")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='suggestions']"))
        )

        suggestion_list = self.driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul")


        for suggestion in suggestion_list:
            if suggestion.text.strip() == 'Switzerland':
                suggestion.find_element(By.CSS_SELECTOR, "a").click()
                

        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText

