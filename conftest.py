import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    # Initialize the Chrome WebDriver
    service_obj = Service("/usr/bin/chromedriver") 
    driver = webdriver.Chrome(service=service_obj)

    # Navigate to the desired webpage
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()
