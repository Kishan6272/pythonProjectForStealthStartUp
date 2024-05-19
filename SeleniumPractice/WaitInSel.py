import time
from telnetlib import EC

#from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/")
#driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("kishanpandey6272@gmail.com")
driver.find_element(By.ID,"enterimg").click()


# wait for 2 second
#time.sleep(2)

#wait is of two type Implicitwait and Explicit Wait
#driver.implicitly_wait(2)


wait =WebDriverWait(driver,5)
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='First Name']"))).send_keys("kishan Kumar")

#driver.find_element(By.XPATH,"//input[@placeholder='First Name`']").send_keys("Kishan")

#driver.implicitly_wait(2)



#wait =WebDriverWait(driver,5)
#wait.until(EC)