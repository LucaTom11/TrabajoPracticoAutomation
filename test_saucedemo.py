import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado
    yield driver
    driver.quit()

def test_login_and_sort(browser):
    # Paso 1: Logueo
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.XPATH, "//input[@type='submit']").click()

    # Paso 2: Ordenar elementos por precio
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )
    sort_dropdown = browser.find_element(By.CLASS_NAME, "product_sort_container")
    sort_dropdown.click()
    sort_dropdown.find_element(By.XPATH, "//option[@value='lohi']").click()

    # Paso 3: Verificar que los elementos estén ordenados
    prices = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(price.text.replace("$", "")) for price in prices]

    assert prices == sorted(prices), "Los elementos no están ordenados correctamente por precio."

if __name__ == "__main__":
    pytest.main(["--html=report.html"])
