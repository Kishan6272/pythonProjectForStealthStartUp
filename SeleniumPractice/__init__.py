from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")
email_Text=driver.find_element(By.ID,"email")
email_Text.send_keys("Kishanpandey6272@gmail.com")
button=driver.find_element(By.ID,"enterimg").click()
# button.click()

driver.implicitly_wait(2000)

