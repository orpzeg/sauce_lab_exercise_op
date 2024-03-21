from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from testlibraries.Money import Money
from pages.InventoryDetailPage import InventoryDetailPage
from pages.components.BaseElement import BaseElement
from testlibraries.webtools import WebTools
from pages.components.CostElement import CostElement


class ProductsElement(BaseElement):
    driver: webdriver = None
    element: webdriver = None

    def __init__(self, driver: webdriver, element: webelement):
        self.driver = driver
        self.element = element
        self.xpath = WebTools.get_xpath_of_element(self.driver, self.element)

    def view_detail(self) -> InventoryDetailPage:
        inventory_item = self.find_element(self.driver, By.XPATH, self.xpath)
        inventory_item_name = self.find_element(inventory_item, By.CLASS_NAME, "inventory_item_name ")
        inventory_item_name.click()

        return InventoryDetailPage(self.driver)

    def get_cost(self):
        inventory_item = self.find_element(self.driver, By.XPATH, self.xpath)
        product_cost_element = CostElement(self.find_element(inventory_item, By.CLASS_NAME, "inventory_item_price"))

        return Money(product_cost_element.get_value(), product_cost_element.get_currency())

    def click_add_to_cart(self):
        inventory_item = self.find_element(self.driver, By.XPATH, self.xpath)
        add_element_button = inventory_item.find_element(By.TAG_NAME, "button")
        add_element_button.click()


