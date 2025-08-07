# this class contains operations for the website's home page.
# it inherits common functionality from the BasePage class.

from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//a[contains(text(), 'Company')]")
    COOKIE_BTN = (By.ID, "wt-cli-accept-all-btn")

    def go_to_company(self):
        self.click(self.COMPANY_MENU) #click on the “Company” menu.