from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class WebTools:
    @staticmethod
    def get_xpath_of_element(driver: webdriver, element: WebElement) -> str:
        # JavaScript function to find the XPath
        script = """
        function getElementXPath(elt){
            var path = '';
            for (; elt && elt.nodeType == 1; elt = elt.parentNode){
                idx = getElementIdx(elt);
                xname = elt.tagName;
                if (idx > 1) xname += '[' + idx + ']';
                path = '/' + xname + path;
            }
            return path;
        }
        function getElementIdx(elt){
            var count = 1;
            for (var sib = elt.previousSibling; sib ; sib = sib.previousSibling){
                if(sib.nodeType == 1 && sib.tagName == elt.tagName) count++
            }
            return count;
        }
        return getElementXPath(arguments[0]);
        """
        return driver.execute_script(script, element)