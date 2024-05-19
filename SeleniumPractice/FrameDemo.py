from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
#driver.maximize_window()



#driver.switch_to.frame("singleFrame")
driver.switch_to.frame("SingleFrame") # class
# //div[@id='Single']/iframe
#single_Frame=driver.find_element( By.XPATH,"//div[@id='Single']/iframe")
#driver.switch_to.frame(single_Frame)

text=driver.find_element(By.TAG_NAME,"input")
text.send_keys("kishasnna")
