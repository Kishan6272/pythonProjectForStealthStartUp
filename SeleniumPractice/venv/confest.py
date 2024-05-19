import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_html_report_title(report):
    report.title = "AutomationReport"

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
@pytest.fixture(scope="session",autouse=True)
def browse():
    global driver
    if driver is None:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver
