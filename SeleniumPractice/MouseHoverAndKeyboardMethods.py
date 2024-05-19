import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://magento.softwaretestingboard.com/")

time.sleep(1)

women = driver.find_element(By.XPATH, "//a[@id='ui-id-4']")

action = ActionChains(driver)

action.move_to_element(women).perform()
#time.sleep(1)

top = driver.find_element(By.XPATH, "//a[@id='ui-id-9']")

action.move_to_element(top).perform()
#time.sleep(1)

jacket = driver.find_element(By.XPATH, "//a[@id='ui-id-11']")

action.move_to_element(jacket).perform()

action.click(jacket).perform()

time.sleep(3)

search = driver.find_element(By.ID, "search")
print("Kishan")
action.key_down(Keys.SHIFT).send_keys("Tewst").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()

#driver.maximize_window()
