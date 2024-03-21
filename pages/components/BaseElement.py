import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def find_element(self, driver: webdriver, by: str, descriptor: str):
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((by, descriptor)))
            return element
        except Exception as e:
            print(f"Caught an error: {e}")
            raise Exception(e)
