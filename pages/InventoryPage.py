from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.CartPage import CartPage
from pages.components.ProductsElement import ProductsElement


class InventoryPage:
    driver: webdriver = None

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_products(self) -> list[ProductsElement]:
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        product_elements_result: list[ProductsElement] = []
        for element in elements:
            product_elements_result.append(ProductsElement(self.driver, element))

        return product_elements_result

    def click_cart(self) -> CartPage:
        cart_button = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()

        return CartPage(self.driver)
