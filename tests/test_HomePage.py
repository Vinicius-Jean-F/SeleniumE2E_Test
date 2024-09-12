from utilities.BaseClass import BaseClass
from pageObject.homePage import HomePage
import pytest
from testData.HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        homepage= HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheckBox().click()

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[("Vinicius","Ferreira","Male"),("Rahul","Shetty","Male")])
    def getData(self, request):
        return request.param

