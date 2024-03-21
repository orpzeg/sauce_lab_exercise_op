from selenium.webdriver.remote import webelement


class CostElement:
    element: webelement = None

    def __init__(self, element: webelement):
        self.element = element

    def get_value(self):
        return self.element.text.lstrip("$")

    def get_currency(self):
        pass
