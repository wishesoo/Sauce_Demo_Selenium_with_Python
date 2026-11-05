
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#aaaa

# FIXTURE: Browser Setup and Teardown

@pytest.fixture
def driver():

    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    print("Browser launched")

    yield driver

    driver.quit()
    print("Browser closed")


# REUSABLE FUNCTION: Login

def perform_login(driver, username, password):

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


# REUSABLE FUNCTION: Get Error Message

def get_error_message(driver):

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )

    return error_message.text


# TEST CASE 1: Valid Username and Valid Password

def test_valid_login(driver):

    perform_login(driver, "standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    print("TC-01: Valid login -> PASSED")


# TEST CASE 2: Locked Out User

def test_locked_out_user(driver):

    perform_login(driver, "locked_out_user", "secret_sauce")

    error_message = get_error_message(driver)

    assert "locked out" in error_message.lower()

    print("TC-02: Locked out user -> PASSED")


# TEST CASE 3: Empty Username and Empty Password

def test_empty_username_empty_password(driver):

    perform_login(driver, "", "")

    error_message = get_error_message(driver)

    assert "Username is required" in error_message

    print("TC-03: Empty username and password -> PASSED")


# TEST CASE 4: Empty Username and Valid Password

def test_empty_username_valid_password(driver):

    perform_login(driver, "", "secret_sauce")

    error_message = get_error_message(driver)

    assert "Username is required" in error_message

    print("TC-04: Empty username and valid password -> PASSED")


# TEST CASE 5: Empty Username and Invalid Password

def test_empty_username_invalid_password(driver):

    perform_login(driver, "", "sauce")

    error_message = get_error_message(driver)

    assert "Username is required" in error_message

    print("TC-05: Empty username and invalid password -> PASSED")


# TEST CASE 6: Invalid Username and Empty Password

def test_invalid_username_empty_password(driver):

    perform_login(driver, "demo", "")

    error_message = get_error_message(driver)

    assert "Password is required" in error_message

    print("TC-06: Invalid username and empty password -> PASSED")


# TEST CASE 7: Invalid Username and Invalid Password

def test_invalid_username_invalid_password(driver):

    perform_login(driver, "demo", "sauce")

    error_message = get_error_message(driver)

    assert "do not match any user" in error_message

    print("TC-07: Invalid username and password -> PASSED")


# TEST CASE 8: Verify Password Field Is Masked

def test_password_field_masked(driver):

    password = driver.find_element(By.ID, "password")

    password.send_keys("secret_sauce")

    password_type = password.get_attribute("type")

    assert password_type == "password"

    print("TC-08: Password field is masked -> PASSED")
