from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.CheckoutStepTwoPage import CheckoutStepTwoPage


class CheckoutStepOnePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def set_my_information(self, first_name, last_name, zip_code):
        first_name_element = self.driver.find_element(By.ID, "first-name")
        last_name_element = self.driver.find_element(By.ID, "last-name")
        zip_code_element = self.driver.find_element(By.ID, "postal-code")

        first_name_element.send_keys(first_name)
        last_name_element.send_keys(last_name)
        zip_code_element.send_keys(zip_code)

    def click_continue(self):
        continue_button_element = self.driver.find_element(By.ID, "continue")
        continue_button_element.click()

        return CheckoutStepTwoPage(self.driver)