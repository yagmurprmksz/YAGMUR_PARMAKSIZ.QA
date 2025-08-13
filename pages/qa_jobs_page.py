# this class handles operations on the QA Jobs page
# it provides methods to filter QA positions by location and department. job card validate,verify lever appl. page

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class QAJobsPage(BasePage):
    SEE_ALL_QA = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    LOCATION_CONTAINER = (By.ID, "select2-filter-by-location-container")
    DEPT_CONTAINER = (By.ID, "select2-filter-by-department-container")
    OPTIONS = (By.XPATH, "//li[contains(@class, 'select2-results__option')]")
    JOB_CARDS = (By.XPATH, "//div[contains(@class, 'position')]")

    def click_see_all_qa_jobs(self):
        try:
            self.click(self.SEE_ALL_QA)
        except:
            alt_btns = self.find_all((By.XPATH, "//*[contains(text(), 'See all QA jobs')]") )
            if alt_btns:
                self.execute_script("arguments[0].click();", alt_btns[0])
            else:
                raise Exception("✗ 'See all QA jobs' buttons cant found")

    def filter_location(self):
        self.click(self.LOCATION_CONTAINER)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='select2-results__options']")))
        all_options = self.find_all((By.XPATH, "//li[contains(@class, 'select2-results__option')]"))
        for option in all_options:
            option_text = option.text.strip()
            if option_text == "Istanbul, Turkiye":
                option.click()
                return
        raise Exception("✗ 'Istanbul, Turkiye' seçeneği bulunamadı")

    def filter_department(self):
        self.click(self.DEPT_CONTAINER)
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(self.OPTIONS))
        all_options = self.find_all(self.OPTIONS)
        for option in all_options:
            option_text = option.text.strip()
            if option_text == "Quality Assurance":
                option.click()
                return
        raise Exception("✗ ''Quality Assurance' option not found")

    def get_job_cards(self):
        return self.wait.until(
            lambda d: d.find_elements(*self.JOB_CARDS)
        )

    def click_first_job_and_apply(self):
        job_cards = self.get_job_cards()
        assert job_cards, "✗ Job card not found after filtering"
        first_job = job_cards[0]
        self.execute_script("arguments[0].scrollIntoView(true);", first_job)
        ActionChains(self.driver).move_to_element(first_job).perform()
        all_links = first_job.find_elements(By.TAG_NAME, "a")
        all_buttons = first_job.find_elements(By.TAG_NAME, "button")
        view_role_button = None
        for elem in all_links + all_buttons:
            text = elem.text.lower()
            if "view role" in text or "apply" in text or "apply now" in text:
                view_role_button = elem
                break
        if view_role_button:
            try:
                view_role_button.click()
            except:
                self.execute_script("arguments[0].click();", view_role_button)
            current_url = self.driver.current_url
            if "lever.co" in current_url:
                return True
            else:
                current_url = self.driver.current_url
                if "lever.co" in current_url:
                    return True
                else:
                    all_windows = self.driver.window_handles
                    if len(all_windows) > 1:
                        self.driver.switch_to.window(all_windows[-1])
                        if "lever.co" in self.driver.current_url:
                            return True
        else:
            raise Exception("✗ No 'View Role' or 'Apply' button found")
        return False

    def verify_job_details(self, job_cards): #verify job cards on the QA Jobs page meet the filtering results
        for index, job in enumerate(job_cards, 1):
            try:
                full_text = job.text.lower()

                if not ("quality" in full_text or "qa" in full_text):
                    print(f"Skipping Job #{index} (not a QA position): {full_text.strip()[:50]}...")
                    continue

                assert "istanbul" in full_text, f"✗ Job #{index} location does not contain 'istanbul': {full_text.strip()}"
                print(f"✓ Job #{index} passed detail checks")

            except Exception as e:
                raise AssertionError(f"✗ Job #{index} error: {e}")
