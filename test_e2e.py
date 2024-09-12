import pytest
from utilities.BaseClass import BaseClass
from pageObject.homePage import HomePage
from pageObject.confirmPage import ConfirmPage
import time

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestOne(BaseClass):
    def test_e2e(self):

        #Create homepage object
        homePage = HomePage(self.driver)

        #Go to checkoutPage
        checkoutPage = homePage.shopItems()

        #Get name of the cards in the page
        cards = checkoutPage.getCardTitles()

        for card in cards:
            card_name = card
            
            if card_name == 'Blackberry':
                checkoutPage.clickCardFooter()

        #Click in the checkout button
        checkoutPage.clickCheckoutButton()

        #Click in the green button
        confirmPage = checkoutPage.clickSuccessButton()

        #Send the first letters of the country name
        confirmPage.inputCountryInitials()

        #Get the list of suggestions in the site
        confirmPage.selectCountry()

        #Agree with the terms
        confirmPage.agreeTerms()

        #Click in the purchase button
        confirmPage.clickPurchase()
        
        #Grab succes purchase string
        successText = confirmPage.testSucces()

        assert "Success! Thank you!" in successText

