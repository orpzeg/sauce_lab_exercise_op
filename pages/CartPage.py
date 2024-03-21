from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.CheckoutStepOnePage import CheckoutStepOnePage


class CartPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def click_checkout(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

        return CheckoutStepOnePage(self.driver)

