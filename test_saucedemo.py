import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo(unittest.TestCase):

    def setUpClass(cls):
        cls.driver = webdriver.Chrome() 
        cls.driver.implicitly_wait(10)

    def testlogin(self):
        # Logueo
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Ordenar elementos por precio
        sort_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        )
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//option[@value='lohi']").click()

        # Verificar que los elementos estén ordenados
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(price.text.replace("$", "")) for price in prices]
        
        self.assertEqual(prices, sorted(prices), "Los elementos no están ordenados correctamente por precio.")

        # Incorporar todos los elementos al carrito
        add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for button in add_to_cart_buttons:
            button.click()

        # Ir al carrito
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verificar que todos los elementos están en el carrito
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(cart_items), len(add_to_cart_buttons), "No todos los elementos están en el carrito.")

        # Ir al checkout
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_Keys("Test")
        self.driver.find_element(By.ID, "continue").click()
        
        # Ingresar nombre y hacer clic en Continue
        self.driver.find_element(By.ID, "first-name").send_keys("Test")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Verificar que aparece el error "Error: Last Name is required"
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message.container").text
        self.assertEqual(error_message, "Error: Last Name is required")

        # Ingresar un apellido y hacer clic en Continue
        self.driver.find_element(By.ID, "last-name").send_keys("User")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # Verificar que aparece el error "Error: Postal Code is required"
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message.container").text
        self.assertEqual(error_message, "Error: Postal Code is required")
    
    def test_purchase_flow(self): 

        # Agregar un elemento al carrito
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click() 

        # Remover el artículo
        self.driver.find_element(By.CLASS_NAME, "cart_button").click()  

        # Verificar que no hay articulos
        Cart_items = self.driver.find_element(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(Cart_items), 0, "Aún hay elementos en el carrito.")

        # Ir a Continue Shopping
        self.driver.find_element(By.ID "continue-shopping").click()
        self.driver.find_element(By.CLASS_NAME, "btn_inventory")[0].click()
        self.driver.find_element(By.CLASS_NAME, "btn_inventory")[1].click()
        
        # Agregar dos elementos
        add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for button in add_to_cart_buttons[:2]:  # Agregar solo dos elementos
            button.click()

        # Ir al carrito
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()   

        # Verificar que los elementos existen
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(cart_items), 2, "No se encontraron los elementos en el carrito.") 

        # Ir a checkout
        self.driver.find_element(By.ID, "Checkout").click()

        # Finalizar la compra
        self.driver.find_element(By.ID, "first-name").send_keys("Test")
        self.driver.find_element(By.ID, "last-name").send_keys("User")
        self.driver.find_element(By.ID, "postal-code").send_keys("91218")
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()

        # verificar que la compra fue realizada

        success_message = driver.find_element(by.CLASS_NAME, "complete-header").text
        self.assertEqual(success_message, "Thank you for your order", "La compra no fue realizada correctamente.")

@classmethod
def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()










