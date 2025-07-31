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
    master_portal_name = (By.XPATH, "//mat-chip-list[@class='mat-chip-list ng-star-inserted']/preceding-sibling::button/parent::div/following-sibling::div/span")
    toolbar_menu = (By.XPATH, "//app-home[@class='ng-star-inserted']//app-header/mat-toolbar/div[2]/span")
    account_btn = (By.XPATH, "//mat-nav-list[@role='navigation']/a[2]")
    account_search = (By.XPATH, "//input[@data-placeholder='Search for an account']")
    next_page = (By.XPATH, "//button[contains(@aria-label,'Next Page') or contains(@aria-label,'Next page')]")
    fleetdashboard = (By.XPATH, "//button[@mattooltip='Launch fleet dashboard']")


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
            manual_version_str = "v5.0.0"  # Expected version

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

    def account_option(self, log):
        try:
            # Step 1: Click the account button
            account_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(MasterPortalPage.account_btn)
            )
            account_button.is_displayed()
            account_button.click()
            time.sleep(7)

            # # Step 2: Enter search keyword
            # search_field = WebDriverWait(self.driver, 20).until(
            #     EC.element_to_be_clickable(MasterPortalPage.account_search)
            # )
            # search_field.click()
            # time.sleep(1)
            # search_field.send_keys('Sreenivas-Fleet')
            # time.sleep(3)


            # Step 3: Loop through pages until fleet icon is found or pagination ends
            while True:
                log.info("🔄 Waiting for Fleet dashboard icons...")
                fleet_buttons = WebDriverWait(self.driver, 25).until(
                    EC.presence_of_all_elements_located(MasterPortalPage.fleetdashboard)
                )

                for btn in fleet_buttons:
                    if btn.is_displayed() and btn.is_enabled():
                        log.info(f"✅ Found clickable fleet: {btn.text}")
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(btn)).click()
                        log.info("🖱️ Clicked on Fleet Portal icon")

                        # Step 4: Wait for Fleet Portal tab to open
                        WebDriverWait(self.driver, 25).until(lambda d: len(d.window_handles) >= 3)
                        new_window = self.driver.window_handles[-1]
                        self.driver.switch_to.window(new_window)
                        log.info("🔁 Switched to Fleet Portal tab")

                        # Step 5: Validate Fleet Portal loaded
                        WebDriverWait(self.driver, 20).until(EC.title_contains("Fleet Portal"))
                        final_title = self.driver.title
                        log.info(f"✅ Fleet Portal launched. Title: {final_title}")
                        return final_title

                # Step 6: If not found, try clicking Next page
                try:
                    next_button = self.driver.find_element(*MasterPortalPage.next_page)
                    if next_button.is_enabled():
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                        next_button.click()
                        log.info("➡️ Clicked on 'Next Page' button to check more fleets")
                        WebDriverWait(self.driver, 10).until(
                            EC.presence_of_all_elements_located(MasterPortalPage.fleetdashboard)
                        )
                    else:
                        log.warning(" :: 'Next Page' button is disabled. No more pages to search. ❗❗")
                        break
                except Exception as next_ex:
                    log.warning(f" ::  Exception checking 'Next Page' button: {next_ex} ❗❗")
                    break

            log.error(" :: No clickable Fleet Navigation icons found after checking all pages. ❌")
            return None

        except Exception as e:
            log.error(f" :: Exception occurred in account_option: {e} ❌")
            return None







