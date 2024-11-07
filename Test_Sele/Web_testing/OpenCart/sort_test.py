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

#Trường hợp sắp xếp theo giá tiền tăng
def test_sort(driver):
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
    
    #Sắp xếp theo giá 
    sort_select = Select(driver.find_element(By.ID, "input-sort"))
    sort_select.select_by_visible_text("Price (Low > High)")
    time.sleep(2)
    
    #Set để bao nhiêu sản phẩm có thể hiển thị
    products_limit = Select(driver.find_element(By.ID, "input-limit"))
    products_limit.select_by_visible_text("10")
    time.sleep(2)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.price-new"))
    )

    # Extract the prices from the sorted product list
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span.price-new")
    print("Number of price elements found:", len(price_elements))

    #Kiểm tra giá tiền có tăng không
    prices = []
    for price in price_elements:
        price_text = price.text.replace("$", "").replace(",", "")
        print("Found price:", price_text)  # Debug print for each price
        prices.append(float(price_text))

    # Print the entire list of prices for verification
    print("Sorted prices:", prices)
    assert prices == sorted(prices), "Prices are not sorted in ascending order."
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("sort=p.price&order=ASC")
    )
    assert "route=product/category" in driver.current_url
    assert "sort=p.price" in driver.current_url
    assert "order=ASC" in driver.current_url
    time.sleep(2)
    