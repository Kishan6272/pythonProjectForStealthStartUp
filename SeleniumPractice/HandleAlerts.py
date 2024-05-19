import time

from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Alerts.html")
#driver.maximize_window()

driver.find_element(By.ID,'OKTab').click()


time.sleep(1)
# ok means assert

driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@href='#CancelTab']").click()
driver.find_element(By.ID,'CancelTab').click()

driver.switch_to.alert.dismiss()



driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()
driver.find_element(By.ID,'Textbox').click()

tx=driver.switch_to.alert.text
print(tx)

driver.switch_to.alert.send_keys("Kishan kimamm")
driver.switch_to.alert.accept()
Str=driver.find_element(By.ID,'demo1').get_attribute()
print(str)




time.sleep(1)
#time.sleep(2)

driver.quit()
