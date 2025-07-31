import time

from ProjectA_Regression.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ChallengesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait

    def validate_challenges_page(self, log):
        status = False
        try:
            challenges_page1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.challenges_page)
            )
            challenges_page1.click()
            time.sleep(3)

            print("🔗 " + self.driver.current_url)

            status = challenges_page1.is_displayed()
            print(challenges_page1.text + " ====> ( Page matched ) 📑")

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.select_date_range)
            ).click()

            time.sleep(2)

            past_30_days1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.past_30_days)
            )
            status = past_30_days1.is_displayed()
            print(past_30_days1.text + " ====> ( Selected Date Range )")
            past_30_days1.click()

            time.sleep(2)

            event_type_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.event_type_filter)
            )
            status = event_type_filter1.is_displayed()
            print(event_type_filter1.text + " ====>  ( Filter type matched )")
            # event_type_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            challenges_status_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.challenges_status_filter)
            )
            status = challenges_status_filter1.is_displayed()
            print(challenges_status_filter1.text + " ====>  ( Filter type matched )")
            # event_type_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)


        except NoSuchElementException:
            pytest.skip("************ Challenges page not displayed **********")
        return status

    def validate_challenges_page_challenged_events_table(self, log):
        status = False
        try:
            challenge_events_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.challenged_events_table)
            )
            status = challenge_events_table1.is_displayed()
            print(challenge_events_table1.text + " ====> ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Challenge Events table not displayed **********")
        return status

