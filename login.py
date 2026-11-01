from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select

#create an instance of web driver for a browser to launch a browser window
driver=webdriver.Edge()

#Visit a URL
driver.get("https://www.saucedemo.com")

#Login with valid credentials
username= driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password= driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button=driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

#Login with empty username and empty password

username= driver.find_element(By.ID, "user-name")
username.send_keys("")

password= driver.find_element(By.ID, "password")
password.send_keys("")

login_button=driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

#Login with empty username and valid password
username= driver.find_element(By.ID, "user-name")
username.send_keys("")

password= driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button=driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

#Login with empty username and invalid password
username= driver.find_element(By.ID, "user-name")
username.send_keys("")

password= driver.find_element(By.ID, "password")
password.send_keys("sauce")

login_button=driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

#Login with invalid username and empty password
username= driver.find_element(By.ID, "user-name")
username.send_keys("demo")

password= driver.find_element(By.ID, "password")
password.send_keys("")

login_button=driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)   #Error message should be username is invalid

#Login with invalid username and invalid password
username= driver.find_element(By.ID, "user-name")
username.send_keys("demo")

password= driver.find_element(By.ID, "password")
password.send_keys("sauce")

login_button=driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

#Verify password field is masked
password = driver.find_element(By.ID, "password")

password.send_keys("secret_sauce")

password_type = password.get_attribute("type")

assert password_type == "password"

print("Test Passed: Password field is masked")
time.sleep(3)

#...............................................
#To validtate "Show Password" icon is working
# Locate password field
# password = driver.find_element(By.ID, "password")
# password.send_keys("secret_sauce")

# Step 1: Verify Show Password icon is visible
#show_password = driver.find_element(By.ID, "show-password")

# assert show_password.is_displayed()
# print("Pass: Show Password icon is visible")

# # Step 2: Verify icon is clickable
# assert show_password.is_enabled()
# print("Pass: Show Password icon is clickable")

# # Step 3: Click the Show Password icon
# show_password.click()

# # Verify password is unmasked
# password_type = password.get_attribute("type")

# assert password_type == "text"
# print("Pass: Password is unmasked")