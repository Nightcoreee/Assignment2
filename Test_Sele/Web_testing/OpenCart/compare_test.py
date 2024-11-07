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
    
#Thêm 2 sản phẩm vào compare và kiểm tra nó 
def test_compare_pro(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("alexson6060@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1234")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
        # Kiểm tra URL hiện tại
    assert "route=account/account" in driver.current_url
    
    click_laptop = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Laptops & Notebooks"))
    )
    click_laptop.click()
    
    show_all_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Show All Laptops & Notebooks"))
    )
    show_all_link.click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb"))
    )

    # Find both product containersX 
    products = driver.find_elements(By.CLASS_NAME, "product-thumb")

    # Click the "Compare" button in each product container
    for product in products[:2]:  # Limit to the first two products
        time.sleep(1)
        compare_button = product.find_element(By.CSS_SELECTOR, "button[formaction*='compare.add']")
        time.sleep(1)
        compare_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "alert"))
    )
    alert_text = driver.find_element(By.ID, "alert").text
    print("Comparison alert:", alert_text)
    time.sleep(2)
    
    driver.find_element(By.ID, "compare-total").click()
    
    #Kiểm tra 2 sản phẩm vừa thêm
    hp_product_name = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[text()='HP LP3065']"))
    )
    print("Found element:", hp_product_name.text)
    
    macbook_name = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[text()='MacBook']"))
    )
    print("Found element:", macbook_name.text)
    time.sleep(2)
    
#Trường hợp remove sản phẩm khỏi compare
def test_remove_compare(driver):
    driver.get("http://localhost/OpenCart/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("alexson6060@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1234")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
        # Kiểm tra URL hiện tại
    assert "route=account/account" in driver.current_url
    
    click_laptop = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Laptops & Notebooks"))
    )
    click_laptop.click()
    
    show_all_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Show All Laptops & Notebooks"))
    )
    show_all_link.click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-thumb"))
    )

    # Find both product containersX 
    products = driver.find_elements(By.CLASS_NAME, "product-thumb")

    # Click the "Compare" button in each product container
    for product in products[:1]:  # Limit to the first two products
        time.sleep(1)
        compare_button = product.find_element(By.CSS_SELECTOR, "button[formaction*='compare.add']")
        time.sleep(1)
        compare_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "alert"))
    )
    alert_text = driver.find_element(By.ID, "alert").text
    print("Comparison alert:", alert_text)
    time.sleep(2)
    
    driver.find_element(By.ID, "compare-total").click()
    
    #Kiểm tra 2 sản phẩm vừa thêm
    hp_product_name = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[text()='HP LP3065']"))
    )
    print("Found element:", hp_product_name.text)
    
    driver.find_element(By.LINK_TEXT, "Remove").click()
    
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    alert_text = success_alert.text
    assert "Success: You have modified your product comparison!" in alert_text, "Unexpected alert message."
    time.sleep(2)