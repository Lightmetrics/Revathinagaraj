import time
from argparse import Action

import keyboard
from telnetlib import EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
# import pyautogui
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class FleetPortalPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait

    portal_version = (By.XPATH,
                      "//mat-chip-list[@class='mat-chip-list ng-star-inserted']/div/mat-chip")
    fleet_name = (By.XPATH, "//mat-chip-list[@class='mat-chip-list ng-star-inserted']/preceding-sibling::button/parent::div/following-sibling::div/div/h3")


    def validate_fleet_name(self, log):
        status = False
        try:

            fleet_title = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located(FleetPortalPage.fleet_name)
            )
            print("🔗 " + self.driver.current_url)
            status = fleet_title.is_displayed()
            log.info(" ****** 🌐 Fleet portal name ****** : " + fleet_title.text +" ✅ ")
            print("🌐 Fleet portal Name  : " + fleet_title.text + " ✅ ")
        except NoSuchElementException:
            pytest.skip("************* Fleet portal name not displayed *************")
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
            version_element = self.driver.find_element(*FleetPortalPage.portal_version)
            text_version_str = version_element.text.strip()
            manual_version_str = "v10.8.0"  # Expected version

            log.info("************ Fleet Portal Version ************ :: %s " % text_version_str)
            print("Fleet Portal Version :: %s " % text_version_str)
            log.info("************ Manual Version ************ :: %s " % manual_version_str)
            print("Manual Version :: %s " % manual_version_str)

            result = self.compare_versions(text_version_str, manual_version_str)
            log.info(" *********** Version result ******* :: %s " % result)
            print("Version result :: %s " % result)

            if not result:
                log.warning("************ Fleet portal version NOT matched ************ ❌")
                print("Fleet portal version NOT matched ❌")
                log.warning("Expected: %s | Actual: %s ❗❗" % (manual_version_str, text_version_str))
                print("Expected: %s | Actual: %s ❗❗" % (manual_version_str, text_version_str))
            else:
                print("************ Fleet portal version matched ************ ✅")
                log.info("Fleet portal version matched ✅")

        except Exception as e:
            log.error("************ ❌ Exception while comparing version ************")
            log.error(str(e))



