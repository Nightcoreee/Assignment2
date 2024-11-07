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
    
#Trường hợp thêm sản phẩm cách thông thường
def test_search(driver):
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
    
   
    product_in_cart = driver.find_element(By.XPATH, "//a[contains(text(),'iPhone')]")
    print(product_in_cart)

#Thêm sản phẩm bằng compare
def test_add_wc(driver):
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
    time.sleep(2)
    driver.find_element(By.ID, "button-confirm").click()
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
    assert "HP LP3065" in alert_text, "Product was not added to the cart successfully."
    
    
    shopping_cart_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'route=checkout/cart')]"))
)
    shopping_cart_link.click()
    time.sleep(4)
    
   
    product_in_cart = driver.find_element(By.XPATH, "//a[contains(text(),'HP LP3065')]")
    print(product_in_cart)


#Thêm sản phẩm bằng wishlist
def test_add_wwl(driver):
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
        wishlist_button = product.find_element(By.CSS_SELECTOR, "button[formaction*='wishlist.add']")
        time.sleep(1)
        wishlist_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "alert"))
    )
    alert_text = driver.find_element(By.ID, "alert").text
    print("Wishlist alert:", alert_text)
    time.sleep(5)
    
    driver.find_element(By.ID, "wishlist-total").click()
    time.sleep(2)
    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)
    
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(2)
    
    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    
    # Check the text in the success alert
    alert_text = success_alert.text
    print("Alert Text:", alert_text)
    
    # Verify if the product is mentioned in the success message
    assert "HP LP3065" in alert_text, "Product was not added to the cart successfully."
    
    shopping_cart_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'route=checkout/cart')]"))
)
    shopping_cart_link.click()
    time.sleep(4)
    
   
    product_in_cart = driver.find_element(By.XPATH, "//a[contains(text(),'HP LP3065')]")
    print(product_in_cart)