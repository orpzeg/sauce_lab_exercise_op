from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

class InventoryDetailPage:
    driver: webdriver = None

    def __init__(self, driver: webdriver):
        self.driver = driver

    def click_back_to_products(self):
        back_to_products_button: webelement = self.driver.find_element(By.ID, "back-to-products")
        back_to_products_button.click()

    def get_price(self) -> str:
        price_element: webelement = self.driver.find_element(By.CLASS_NAME, "inventory_details_price")
        return price_element.text

    def click_add_to_cart(self):
        add_to_card_button: webelement = self.driver.find_element(By.XPATH, f"//*[contains(@id, 'add-to-cart')]")
        add_to_card_button.click()

    def get_count_products_incart(self) -> int:
        shopping_cart_link: webelement = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")

        return int(shopping_cart_link.text)
