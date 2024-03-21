from selenium import webdriver
from chromedriver_py import binary_path


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser.lower()

    def get_web_driver_instance(self) -> webdriver:
        if self.browser == 'chrome':
            svc = webdriver.ChromeService(executable_path=binary_path)
            driver = webdriver.Chrome(service=svc)
            return driver
        elif self.browser == "edge":
            return webdriver.Edge()
        else:
            raise ValueError("Browser not supported: {}".format(self.browser))
