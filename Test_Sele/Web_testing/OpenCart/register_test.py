import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Trường hợp đăng nhập thành công
def test_register(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
    driver.find_element(By.ID, "input-firstname").send_keys("hihi")
    driver.find_element(By.ID, "input-lastname").send_keys("haha")
    driver.find_element(By.ID, "input-email").send_keys("haha6060@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1234")
    
    checkbox_sub = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-newsletter"))
    )
    
    # Kiểm tra nếu checkbox chưa được chọn
    if not checkbox_sub.is_selected():
        checkbox_sub.click()  # Chọn checkbox
        print("Checkbox đã được chọn.")
    else:
        print("Checkbox đã được chọn sẵn.")
    #Kiểm tra checkbox đã được chọn chưa
    assert checkbox_sub.is_selected() == True, "Checkbox chưa được chọn"
    
    checkbox_privacy = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "agree"))
    )
    
    # Kiểm tra nếu checkbox chưa được chọn
    if not checkbox_privacy.is_selected():
        checkbox_privacy.click()  # Chọn checkbox
        print("Checkbox đã được chọn.")
    else:
        print("Checkbox đã được chọn sẵn.")
    #Kiểm tra checkbox đã được chọn chưa
    assert checkbox_privacy.is_selected() == True, "Checkbox chưa được chọn"
    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    # Verify the presence of a success message after registration
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your Account Has Been Created!']"))
    )

    assert success_message is not None, "Đăng ký không thành công hoặc không có thông báo xác nhận."
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
    time.sleep(3)
        
#Trường hợp bỏ trống các trường
def test_empty_regis(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
    driver.find_element(By.ID, "input-firstname").send_keys("")
    driver.find_element(By.ID, "input-lastname").send_keys("")
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    #Lỗi không nhập firstname
    error_message_first = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-firstname"))
    )
    assert error_message_first.is_displayed(), "Error message for First Name is not displayed"
    assert "First Name must be between 1 and 32 characters!" in error_message_first.text, \
        f"Expected error message, but got: {error_message_first.text}"
    
    #Lỗi không nhập lastname
    error_message_last = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-lastname"))
    )
    assert error_message_last.is_displayed(), "Error message for First Name is not displayed"
    assert "Last Name must be between 1 and 32 characters!" in error_message_last.text, \
        f"Expected error message, but got: {error_message_last.text}"
        
    #Lỗi không nhập Email
    error_message_email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-email"))
    )
    assert error_message_email.is_displayed(), "Error message for First Name is not displayed"
    assert "E-Mail Address does not appear to be valid!" in error_message_email.text, \
        f"Expected error message, but got: {error_message_email.text}"
        
    #Lỗi không nhập password
    error_message_pass = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-password"))
    )
    assert error_message_pass.is_displayed(), "Error message for First Name is not displayed"
    assert "Password must be between 4 and 20 characters!" in error_message_pass.text, \
        f"Expected error message, but got: {error_message_pass.text}"
    
    #Lỗi không ấn checkbox
    warning_message_privacy = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # Assert that the warning message is displayed and contains the expected text
    assert warning_message_privacy.is_displayed(), "Privacy Policy warning message is not displayed"
    assert "You must agree to the Privacy Policy!" in warning_message_privacy.text, \
        f"Expected warning message, but got: {warning_message_privacy.text}"
    
    time.sleep(3)
    

#Trường hợp nhập sai email không đúng định dạng @gmail.com
def test_wrong_email(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
    driver.find_element(By.ID, "input-firstname").send_keys("saa")
    driver.find_element(By.ID, "input-lastname").send_keys("haha")
    driver.find_element(By.ID, "input-email").send_keys("haha6060@hihi")
    driver.find_element(By.ID, "input-password").send_keys("1234")
    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    checkbox_sub = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-newsletter"))
    )
    
    if not checkbox_sub.is_selected():
        checkbox_sub.click()
    assert checkbox_sub.is_selected() == True, "Checkbox chưa được chọn"
    
    
    checkbox_privacy = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "agree"))
    )
    
    if not checkbox_privacy.is_selected():
        checkbox_privacy.click()
    assert checkbox_privacy.is_selected() == True, "Checkbox chưa được chọn"
    
    # Locate and click the "Continue" button (submit button)
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()

    # Wait for the error message for email validation
    error_message_email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-email"))
    )

    # Assert that the email error message is displayed
    assert error_message_email.is_displayed(), "Error message for First Name is not displayed"
    assert "E-Mail Address does not appear to be valid!" in error_message_email.text, \
        f"Expected error message, but got: {error_message_email.text}"

    # Optionally, wait a bit longer to observe the result
    time.sleep(3)
    
#Trường hợp nhập pass không đủ thiểu số là 4 trở lên
def test_fill_pass(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
    driver.find_element(By.ID, "input-firstname").send_keys("saa")
    driver.find_element(By.ID, "input-lastname").send_keys("haha")
    driver.find_element(By.ID, "input-email").send_keys("haha60@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    checkbox_sub = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-newsletter"))
    )
    
    if not checkbox_sub.is_selected():
        checkbox_sub.click()
    assert checkbox_sub.is_selected() == True, "Checkbox chưa được chọn"
    
    
    checkbox_privacy = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "agree"))
    )
    
    if not checkbox_privacy.is_selected():
        checkbox_privacy.click()
    assert checkbox_privacy.is_selected() == True, "Checkbox chưa được chọn"
    
    error_message_pass = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-password"))
    )
    assert error_message_pass.is_displayed(), "Error message for First Name is not displayed"
    assert "Password must be between 4 and 20 characters!" in error_message_pass.text, \
        f"Expected error message, but got: {error_message_pass.text}"
        
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    
    time.sleep(3)
    
#Trường hợp nhập tài khoản đã đăng ký
def test_acc_exists(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
    driver.find_element(By.ID, "input-firstname").send_keys("hihi")
    driver.find_element(By.ID, "input-lastname").send_keys("huhu")
    driver.find_element(By.ID, "input-email").send_keys("alexson6060@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123")
    
    checkbox_sub = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-newsletter"))
    )
    
    if not checkbox_sub.is_selected():
        checkbox_sub.click()
    assert checkbox_sub.is_selected() == True, "Checkbox chưa được chọn"
    
    
    checkbox_privacy = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "agree"))
    )
    
    if not checkbox_privacy.is_selected():
        checkbox_privacy.click()
    assert checkbox_privacy.is_selected() == True, "Checkbox chưa được chọn"
    
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    continue_button.click()
    
    warning_message_account = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger"))
    )

    # Assert that the warning message is displayed and contains the expected text
    assert warning_message_account.is_displayed(), "Privacy Policy warning message is not displayed"
    assert "E-Mail Address is already registered!" in warning_message_account.text, \
        f"Expected warning message, but got: {warning_message_account.text}"
    time.sleep(3)
    