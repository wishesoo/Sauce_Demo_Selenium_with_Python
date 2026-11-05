import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

#aaaa

@pytest.fixture
def driver():

    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    print("Browser launched")

    yield driver

    driver.quit()
    print("Browser closed")

#Defining Test Data
valid_username="standard_user"
valid_password="secret_sauce"     

#Defining Locators
username_field=(By.ID,"user-name")
password_field=(By.ID,"password")
login_button=(By.ID,"login-button")

       
# TEST CASE 1: Valid Username & Valid Password
 
def test_login_credentials_valid_username_valid_password(driver):
    driver.find_element(*username_field).send_keys(valid_username)
    time.sleep(1)
    driver.find_element(*password_field).send_keys(valid_password)
    time.sleep(1)
    driver.find_element(*login_button).click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
   
    assert "inventory.html" in driver.current_url, "Scenario 1: Login failed, incorrect redirection"
    print("Scenario 1: Login with valid username and valid password -> PASSED")