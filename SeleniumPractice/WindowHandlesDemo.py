from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
#driver.maximize_window()

parent =driver.current_window_handle
print(parent)

driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']").click()

widows=driver.window_handles

for win in widows:
    if win!=parent:
        driver.switch_to.window(win)

driver.find_element(By.XPATH,"//span[contains(text(),'Downloads')]").click()
der=driver.title
print(der)


driver.close()


#driver.quit()


