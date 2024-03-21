from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webelement

from pages.InventoryPage import InventoryPage


class SauceDemoLoginPage:
    driver: webdriver = None

    def __init__(self, driver: webdriver):
        self.driver = driver

    def gotopage(self):
        self.driver.get("https://www.saucedemo.com/")

    def set_credentials(self, login: str, password: str):
        username_element = self.driver.find_element(By.NAME, "user-name")
        password_element = self.driver.find_element(By.NAME, "password")
        username_element.send_keys(login)
        password_element.send_keys(password)

    def clicklogin(self) -> InventoryPage:
        login_button: webelement = self.driver.find_element(By.NAME, "login-button")
        login_button.click()
        return InventoryPage(self.driver)
