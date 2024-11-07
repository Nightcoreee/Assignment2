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
    
#Checkout
def test_checkout(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("alexson6060@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1234")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
        # Kiểm tra URL hiện tại
    assert "route=account/account" in driver.current_url
    
    driver.find_element(By.NAME, "search").send_keys("Iphone")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("route=product/search")
    )

    # Verify that the current URL is the search results page for "iPhone"
    assert "route=product/search" in driver.current_url
    
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(2)
    
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(2)
    
    #alert
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    
    # Check the text in the success alert
    alert_text = success_alert.text
    print("Alert Text:", alert_text)
    
    # Verify if the product is mentioned in the success message
    assert "iPhone" in alert_text, "Product was not added to the cart successfully."
    
    shopping_cart_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'route=checkout/cart')]"))
)
    shopping_cart_link.click()
    time.sleep(4)
    
    driver.find_element(By.LINK_TEXT, "Checkout").click()
    time.sleep(2)
    
    new_address_input = driver.find_element(By.ID, "input-shipping-new")
    new_address_input.click()
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-firstname").send_keys("HIHI")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-lastname").send_keys("haha")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-company").send_keys("ABC")
    time.sleep(2)

    driver.find_element(By.ID, "input-shipping-address-1").send_keys("số 5 TCĐ")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-address-2").send_keys("253 ADV")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-city").send_keys("TP.HCM")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-postcode").send_keys("70000")
    time.sleep(2)
    
    country_select = Select(driver.find_element(By.ID, "input-shipping-country"))
    country_select.select_by_visible_text("Viet Nam")
    time.sleep(2)
    
    region_select = Select(driver.find_element(By.ID, "input-shipping-zone"))
    region_select.select_by_visible_text("Ho Chi Minh City")
    time.sleep(2)
    
    driver.find_element(By.ID, "button-shipping-address").click()
    time.sleep(2)
    
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )

    # Check if the success message contains the correct text
    alert_text = success_alert.text
    print("Alert Text:", alert_text)

    # Assert that the message confirms the shipping address change
    assert "You have changed shipping address!" in alert_text, "Shipping address change message not found."
    
    driver.find_element(By.ID, "button-shipping-methods").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "button-shipping-method").click()
    time.sleep(1)
    
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )

    # Check if the success message contains the correct text
    alert_text = success_alert.text
    print("Alert Text:", alert_text)

    # Assert that the message confirms the shipping address change
    assert "Success: You have changed shipping method!" in alert_text
    # <div id="alert" class="toast-container position-fixed top-0 end-0 p-3"><div class="alert alert-success alert-dismissible" style="opacity: 0.830656;"><i class="fa-solid fa-circle-check"></i> Success: You have changed shipping method! <button type="button" class="btn-close" data-bs-dismiss="alert"></button></div></div>
    
    driver.find_element(By.ID, "button-payment-methods").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    time.sleep(1)
    
    driver.find_element(By.ID, "button-payment-method").click()
    time.sleep(1)
    
    alert_text = success_alert.text
    print("Alert Text:", alert_text)

    # Assert that the message confirms the shipping address change
    assert "Success: You have changed payment method!" in alert_text
    
    driver.find_element(By.ID, "button-confirm").click()
    time.sleep(1)
    
    checkout1_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your order has been placed!']"))
    )
    assert checkout1_message 
    
    checkout2_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Your order has been successfully processed!')]"))
    )
    assert checkout2_message
    time.sleep(3)
    
#Trường hợp để trống các trường 
def test_checkout2(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("alexson6060@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1234")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
        # Kiểm tra URL hiện tại
    assert "route=account/account" in driver.current_url
    
    driver.find_element(By.NAME, "search").send_keys("Iphone")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("route=product/search")
    )

    # Verify that the current URL is the search results page for "iPhone"
    assert "route=product/search" in driver.current_url
    
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(2)
    
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(2)
    
    #alert
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    
    # Check the text in the success alert
    alert_text = success_alert.text
    print("Alert Text:", alert_text)
    
    # Verify if the product is mentioned in the success message
    assert "iPhone" in alert_text, "Product was not added to the cart successfully."
    
    shopping_cart_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'route=checkout/cart')]"))
)
    shopping_cart_link.click()
    time.sleep(4)
    
    driver.find_element(By.LINK_TEXT, "Checkout").click()
    time.sleep(2)
    
    new_address_input = driver.find_element(By.ID, "input-shipping-new")
    new_address_input.click()
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-firstname").send_keys("")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-lastname").send_keys("")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-company").send_keys("")
    time.sleep(2)

    driver.find_element(By.ID, "input-shipping-address-1").send_keys("")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-address-2").send_keys("")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-city").send_keys("")
    time.sleep(2)
    
    driver.find_element(By.ID, "input-shipping-postcode").send_keys("")
    time.sleep(2)
    
    country_select = Select(driver.find_element(By.ID, "input-shipping-country"))
    country_select.select_by_visible_text("--- Please Select ---")
    time.sleep(2)
    
    region_select = Select(driver.find_element(By.ID, "input-shipping-zone"))
    region_select.select_by_visible_text("--- Please Select ---")
    time.sleep(2)
    
    driver.find_element(By.ID, "button-shipping-address").click()
    time.sleep(2)
    
    error_message_first = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-shipping-firstname"))
    )
    assert error_message_first.is_displayed(), "Error message for First Name is not displayed"
    assert "First Name must be between 1 and 32 characters!" in error_message_first.text, \
        f"Expected error message, but got: {error_message_first.text}"
      
        
    error_message_last = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-shipping-lastname"))
    )
    assert error_message_last.is_displayed(), "Error message for Last Name is not displayed"
    assert "Last Name must be between 1 and 32 characters!" in error_message_last.text, \
        f"Expected error message, but got: {error_message_last.text}"
        
        
    error_message_addr = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-shipping-address-1"))
    )
    assert error_message_addr.is_displayed(), "Error message for Address is not displayed"
    assert "Address 1 must be between 3 and 128 characters!" in error_message_addr.text, \
        f"Expected error message, but got: {error_message_addr.text}"
        
        
    error_message_city = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-shipping-city"))
    )
    assert error_message_city.is_displayed(), "Error message for City is not displayed"
    assert "City must be between 2 and 128 characters!" in error_message_city.text, \
        f"Expected error message, but got: {error_message_city.text}"
        
        
    error_message_region = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-shipping-zone"))
    )
    assert error_message_region.is_displayed(), "Error message for Region is not displayed"
    assert "Please select a region / state!" in error_message_region.text, \
        f"Expected error message, but got: {error_message_region.text}"
        
    time.sleep(1)