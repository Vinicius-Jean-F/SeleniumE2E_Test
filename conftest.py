import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # Initialize the Chrome WebDriver
        service_obj = Service("/usr/bin/chromedriver") 
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        i = 0
    elif browser_name == "IE":
        i = 0
        
    # Navigate to the desired webpage
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()
