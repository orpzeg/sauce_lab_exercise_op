from selenium import webdriver
from selenium.webdriver.common.by import By

from testlibraries.CurrencyParser import CurrencyParser


class CheckoutStepTwoPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_total_cost(self):
        cost_element = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label")

        return CurrencyParser.parse_currency_and_value(cost_element.text)
