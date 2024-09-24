import pytest
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":

        """
        # Initialize the Chrome WebDriver
        service_obj = Service("/usr/bin/chromedriver") 
        driver = webdriver.Chrome(service=service_obj)
        """

        # Init Chromium driver
        # Set up Chrome options to use Chromium and run in headless mode
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium"  # Path to Chromium browser
        chrome_options.add_argument('--headless')  # Ensure GUI is off in environments like Docker
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')


        # Initialize the Chromium WebDriver
        service = ChromiumService(executable_path="/usr/bin/chromedriver")  # Path to ChromiumDriver
        driver = webdriver.Chrome(service=service, options=chrome_options)

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

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

