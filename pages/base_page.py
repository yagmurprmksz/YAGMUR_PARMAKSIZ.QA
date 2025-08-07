#it is the base class from which all page classes inherit.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20) #takes wd instance and creates wait object with 20sec(a safe upper limit)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click() #waits until the given item is clickable and then clicks it

    def find(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator)) #waits for the element to exist on the page and returns

    def find_all(self, by_locator):
        return self.driver.find_elements(*by_locator)#returns the specified items directly

    def wait_for_visibility(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))#waits for the element to become visible

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args) #executes JS commands

    def accept_cookies(self):
        return self.click((By.ID, "wt-cli-accept-all-btn")) #click accept button because there are too many cookies
