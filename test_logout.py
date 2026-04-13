
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time 


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()

options.add_argument("--disable-notifications")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()


driver.get("https://www.saucedemo.com")
time.sleep(2)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()
time.sleep(2)


driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(5)

driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)

assert "saucedemo.com" in driver.current_url, "LOGOUT FAILD"
print ("✅ Logout test PASSED")

time.sleep(4)
driver.quit()