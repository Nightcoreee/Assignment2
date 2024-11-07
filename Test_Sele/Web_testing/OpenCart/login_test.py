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
def test_valid_login(driver):
    try:
        driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
        driver.find_element(By.ID, "input-email").send_keys("alexson6060@gmail.com")
        driver.find_element(By.ID, "input-password").send_keys("1234")
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
        # Đợi URL chứa 'route=account/account'
        WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
        # Kiểm tra URL hiện tại
        assert "route=account/account" in driver.current_url
        print("Đăng nhập thành công và đã chuyển hướng đến trang tài khoản người dùng.")
        time.sleep(5)
        
    except TimeoutException:
        pytest.fail("Không chuyển hướng đến trang tài khoản người dùng trong 10 giây.")
    except NoSuchElementException as e:
        pytest.fail(f"Không tìm thấy phần tử: {e}")

# Trường hợp đăng nhập sai mật khẩu
def test_invalid_login(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("alexson6060@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    time.sleep(5)
    error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
            )
    assert "No match for E-Mail Address and/or Password" in error_message.text

# Trường hợp để trống thông tin gmail và password
def test_empty_user_pass(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(3)
    error_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
            )
    assert "No match for E-Mail Address and/or Password" in error_message.text
    
    


    
   
 
    
       

    
