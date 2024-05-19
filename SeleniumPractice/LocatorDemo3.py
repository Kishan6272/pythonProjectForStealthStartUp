from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")
driver.maximize_window()
email_Text=driver.find_element(By.ID,"email")
email_Text.send_keys("Kishanpandey6272@gmail.com")
button=driver.find_element(By.ID,"enterimg").click()

driver.find_element(By.XPATH,"//input[@value='Male']").click()
# button.click()

li =driver.find_elements(By.XPATH,"//input[@type='checkbox']")





select_web = driver.find_element(By.ID,'Skills')

sel=Select(select_web)

sel.select_by_index(7)


driver.implicitly_wait(2000)

# //input[@placeholder="First Name"]
# //input[@placeholder="First Name"]
#//label[contains(text(),'Full ')]


# ans and or
# ng-model="FirstName"
# //*[@placeholder="First Name" and @ng-model="FirstName"]
# parent child thing 

#id="checkbox1
# //input[@id="checkbox1"]//following-sibling::label