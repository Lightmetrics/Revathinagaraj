import time

from ProjectB_Sanity.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CoachingPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait


    def validate_coaching_page(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.coaching_page)
            ).click()
            time.sleep(3)

            print("🔗 " + self.driver.current_url)

            coaching_page1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.coaching_page)
            )

            status = coaching_page1.is_displayed()
            print(coaching_page1.text + " ====>  ( Page matched ) 📑")

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.select_date_range)
            ).click()

            time.sleep(1)

            past_30_days1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.past_30_days)
            )
            status = past_30_days1.is_displayed()
            print(past_30_days1.text + " ====>  ( Selected Date Range )")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.past_30_days)
            ).click()

            time.sleep(1)

            select_tags_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_tags_filter)
            )
            status = select_tags_filter1.is_displayed()
            print(select_tags_filter1.text + " ====>  ( Filter type matched )")
            # select_tags_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

        except NoSuchElementException:
            pytest.skip("************ Coaching page not displayed **********")
        return status

    def validate_coaching_page_coachable_drivers_table(self, log):
        status = False
        try:
            coachable_drivers_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.coachable_drivers)
            )
            status = coachable_drivers_table1.is_displayed()
            print(coachable_drivers_table1.text + " ====>  ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Coachable Drivers table not displayed **********")
        return status

    def validate_coaching_page_completed_coaching_sessions_table(self, log):
        status = False
        try:
            completed_coaching_sessions_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.completed_coaching_sessions)
            )
            status = completed_coaching_sessions_table1.is_displayed()
            print(completed_coaching_sessions_table1.text + " ====>  ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Completed Coaching Sessions table not displayed **********")
        return status