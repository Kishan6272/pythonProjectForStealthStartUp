import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def launchBrowse():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    driver.quit()


@pytest.fixture(scope="class")
def launchBrowserClass(request):
    global driver
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    request.cls.driver.quit()



def test_printTheUrl(launchBrowse):
    driver.get("https://magento.softwaretestingboard.com/")
    #print(driver.current_url)


def test_printTheUrl(launchBrowse):
    #driver.get("https://magento.softwaretestingboard.com/")
    print(driver.current_url)



@pytest.mark.usefixtures("launchBrowserClass")
class Test_Magento:
    def test_entreTheUrl(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
