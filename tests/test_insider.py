import pytest
from selenium import webdriver
import os
from datetime import datetime

from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage


class TestInsiderSimple:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def take_screenshot(self, test_name):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{test_name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        print(f"✗ Screenshot saved: {filename}")

    def test_1_careers_page_sections(self):
        try:
            self.driver.get("https://useinsider.com/")
            home = HomePage(self.driver)
            home.accept_cookies()
            home.go_to_company()
            careers = CareersPage(self.driver)
            careers.go_to_careers()

            # Verify sections
            locations_found = careers.has_locations_section()
            teams_found = careers.has_teams_section()
            life_found = careers.has_life_section()

            print("✓ Locations section found" if locations_found else "✗ Locations section not found")
            print("✓ Teams section found" if teams_found else "✗ Teams section not found")
            print("✓ Life at Insider section found" if life_found else "✗ Life at Insider section not found")

            # Assert all sections are found
            assert locations_found, "Locations section not found"
            assert teams_found, "Teams section not found"
            assert life_found, "Life at Insider section not found"

        except Exception as e:
            self.take_screenshot("test_1_careers_page_sections_failed")
            raise e

    def test_2_qa_jobs_filtering_and_application(self):
        try:
            self.driver.get("https://useinsider.com/careers/quality-assurance/")
            qa_jobs = QAJobsPage(self.driver)
            qa_jobs.accept_cookies()
            qa_jobs.click_see_all_qa_jobs()

            qa_jobs.filter_location()
            qa_jobs.filter_department()

            job_cards = qa_jobs.get_job_cards()
            assert job_cards, "✗ no job cards found after filtering"
            print(f"✓ Found {len(job_cards)} job cards after filtering")

            qa_jobs.verify_job_details(job_cards)

            assert qa_jobs.click_first_job_and_apply(), "✗ failed to redirect to Lever application page"
            print("✓succes redirected to the Lever application page")

        except Exception as e:
            self.take_screenshot("test_2_qa_jobs_filtering_failed")
            raise e