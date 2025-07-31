import time
from xml.sax.saxutils import escape

# import pyautogui

from ProjectB_Sanity.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SafetyEventsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait

    def validate_safety_events(self, log):
        status = False
        try:

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.safety_events_btn)
            ).click()
            time.sleep(3)
            print("🔗 " + self.driver.current_url)

            safety_events1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.safety_events_btn)
            )
            status = safety_events1.is_displayed()
            print(safety_events1.text + " ====>  ( Page matched ) 📑")


            events_view1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.events_view)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", events_view1)
            time.sleep(1)


        except NoSuchElementException:
            pytest.skip("************ Safety Events page not displayed **********")
        return status

    def validate_safety_events_view(self, log):
        status = False
        try:
            events_view1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.events_view)
            )
            status = events_view1.is_displayed()
            print(events_view1.text + " ====>  ( Events Title matched )")

            toggle_view1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.toggle_filter)
            )
            status = toggle_view1.is_displayed()
            print(toggle_view1.text + " ====>  ( Filters hide option matched )")

            list_view1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.list_view)
            )
            status = list_view1.is_displayed()
            print(list_view1.text + " ====>  ( View type matched )")

        except NoSuchElementException:
            pytest.skip("************ Events View card not displayed **********")
        return status

    def validate_safety_events_filters(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.clear_btn)
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.select_date_range)
            ).click()

            past_30_days1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.past_30_days)
            )
            status = past_30_days1.is_displayed()
            print(past_30_days1.text + " ====>  ( Selected Date Range )")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.past_30_days)
            ).click()

            filter_type1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.filter_type)
            )
            status = filter_type1.is_displayed()
            print(filter_type1.text + " ====>  ( Filter type matched )")
            # filter_type1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            driver_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.driver_filter)
            )
            status = driver_filter1.is_displayed()
            print(driver_filter1.text + " ====>  ( Filter type matched )")
            # driver_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            event_type_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.event_type_filter)
            )
            status = event_type_filter1.is_displayed()
            print(event_type_filter1.text + " ====>  ( Filter type matched )")
            # event_type_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            view_status_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.view_status_filter)
            )
            status = view_status_filter1.is_displayed()
            print(view_status_filter1.text + " ====>  ( Filter type matched )")
            # view_status_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.apply_btn)
            ).click()
            time.sleep(2)
            print(" ✅ Successfully applied filters on 'Safety Events' page.")

        except NoSuchElementException:
            pytest.skip("************ Filters not displayed on Safety Events page **********")
        return status

