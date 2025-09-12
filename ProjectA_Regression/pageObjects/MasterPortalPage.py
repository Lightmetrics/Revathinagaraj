import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MasterPortalPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait

    master_portal_version = (By.XPATH, "//mat-chip-list[@class='mat-chip-list ng-star-inserted']/div/mat-chip")
    lisa_close_btn = (By.XPATH, "//app-chatbot-widget/section[contains(@class,'widget')]/div/div[2]/button[2]")
    master_portal_name = (By.XPATH, "//mat-chip-list[@class='mat-chip-list ng-star-inserted']/preceding-sibling::button/parent::div/following-sibling::div/span")
    toolbar_menu = (By.XPATH, "//app-home[@class='ng-star-inserted']//app-header/mat-toolbar/div[2]/span")
    account_btn = (By.XPATH, "//mat-nav-list[@role='navigation']/a[2]")
    account_search = (By.XPATH, "//input[@data-placeholder='Search for an account']")
    fleetdashboard = (By.XPATH, "(//mat-icon[contains(text(),'open_in_new')])[1]/ancestor::button[1]")


    def validate_master_name(self, log):
        status = False
        try:
            master_title = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MasterPortalPage.master_portal_name)
            )
            print("🔗 " + self.driver.current_url)
            status = master_title.is_displayed()
            log.info("****** 🌐 Master portal Name : " + master_title.text + " ✅")
            print("🌐 Master portal Name  : " + master_title.text + " ✅")
        except NoSuchElementException:
            pytest.skip("************* Master portal Name name not displayed *************")
        return status


    def extract_version_number(self, version):
        # Extract the numbers after 'v'
        version_numbers = version.split('v')[-1]
        version_numbers = [int(num) for num in version_numbers.split('.')]
        return version_numbers

    def compare_versions(self, version1, version2):
        version1_numbers = self.extract_version_number(version1)
        version2_numbers = self.extract_version_number(version2)
        compare = False
        for num1, num2 in zip(version1_numbers, version2_numbers):
            if num1 == num2:
                compare = True
            else:
                compare = False
                break
        return compare

    def compare_actual_version(self, log):
        try:
            version_element = self.driver.find_element(*MasterPortalPage.master_portal_version)
            text_version_str = version_element.text.strip()
            manual_version_str = "v5.27.0"  # Expected version

            log.info("************ Master Portal Version ************ :: %s " % text_version_str)
            print("Master Portal Version :: %s " % text_version_str)
            log.info("************ Manual Version ************ :: %s " % manual_version_str)
            print("Manual Version :: %s " % manual_version_str)

            result = self.compare_versions(text_version_str, manual_version_str)
            log.info(" *********** Version result ******* :: %s " % result)
            print("Version result :: %s " % result)

            if not result:
                log.warning("************ Master portal version NOT matched ************ ❌")
                print("Master portal version NOT matched ❌")
                log.warning("********* Expected: %s | Actual: %s ❗❗" % (manual_version_str, text_version_str))
                print("Expected: %s | Actual: %s ❗❗" % (manual_version_str, text_version_str))
            else:
                print("************ Master portal version matched ************ ✅")
                log.info("Master portal version matched ✅")

        except Exception as e:
            log.error("************ Exception while comparing version ************")
            log.error(str(e))


    def account_option(self):
        try:
            time.sleep(2)

            lisa_close = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(MasterPortalPage.lisa_close_btn))
            lisa_close.click()
            time.sleep(2)

            # Click the account button
            account_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(MasterPortalPage.account_btn)
            )
            account_button.click()

            # Click the account search field
            search_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(MasterPortalPage.account_search)
            )
            search_field.click()

            # Enter search term
            search_field.send_keys('Acme Transport')
            time.sleep(5)

            # Click the fleet dashboard button
            fleet_dashboard_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(MasterPortalPage.fleetdashboard)
            )
            fleet_dashboard_button.click()


            # Wait for new windows to open and switch to the third window
            self.wait.until(lambda driver: len(driver.window_handles) > 2)
            third_window_handle = [handle for handle in self.driver.window_handles if handle != self.driver.current_window_handle][1]
            self.driver.switch_to.window(third_window_handle)

            print("🔗 " + self.driver.current_url)


            return self.driver.title
        except TimeoutException:
            print("Timeout occurred while waiting for elements.")
        except NoSuchElementException as e:
            print(f"Element not found: {e}")


