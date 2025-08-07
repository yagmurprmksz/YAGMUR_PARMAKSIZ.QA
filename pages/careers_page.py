# this class represents the Careers page and contains operations to interact with it
# it inherits from BasePage and provides methods to verify key sections like Locations, Teams, and Life at Insider

from selenium.webdriver.common.by import By
from .base_page import BasePage

class CareersPage(BasePage):
    CAREERS_LINK = (By.XPATH, "//a[contains(text(), 'Careers')]")
    LOCATIONS_SECTION = (By.XPATH, "//*[contains(text(), 'Locations')]")
    TEAMS_SECTION = (By.XPATH, "//*[contains(text(), 'Teams')]")
    LIFE_SECTION = (By.XPATH, "//*[contains(text(), 'Life')]")

    def go_to_careers(self):
        self.click(self.CAREERS_LINK)

    def has_locations_section(self):
        try:
            self.find(self.LOCATIONS_SECTION)
            return True
        except:
            return False

    def has_teams_section(self):
        try:
            self.find(self.TEAMS_SECTION)
            return True
        except:
            return False

    def has_life_section(self):
        try:
            self.find(self.LIFE_SECTION)
            return True
        except:
            return False