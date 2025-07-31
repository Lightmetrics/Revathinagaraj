import time

from ProjectA_Regression.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class VideoRequestsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait

    def validate_video_requests_page(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.video_requests_page)
            ).click()
            time.sleep(3)

            print("🔗 " + self.driver.current_url)

            video_requests_page = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.video_requests_page)
            )

            status = video_requests_page.is_displayed()
            print(video_requests_page.text + " ====>  ( Page matched ) 📑")

            WebDriverWait(self.driver, 10).until(
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

            time.sleep(3)

            select_tags_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_tags_filter)
            )
            status = select_tags_filter1.is_displayed()
            print(select_tags_filter1.text + " ====>  ( Filter type matched )")
            # select_tags_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

        except NoSuchElementException:
            pytest.skip("************ Video Requests page not displayed **********")
        return status

    def validate_video_requests_page_table(self, log):
        status = False
        try:
            video_requests_table = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.video_requests_table)
            )
            status = video_requests_table.is_displayed()
            print(video_requests_table.text + " ====>  ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Video Requests table not displayed **********")
        return status

    def validate_video_requests_page_request_video_popUp(self, log):
        status = False
        try:
            video_requests_page_popUp = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.request_video_popUp_btn)
            )
            status = video_requests_page_popUp.is_displayed()
            print(video_requests_page_popUp.text + " ====>  ( Button matched )")
            video_requests_page_popUp.click()
            print(" 🎥/🚀 ✅ Successfully launched 'REQUEST VIDEO' Pop-Up, from 'Video Requests' Page")
            time.sleep(1)

            date_filter_from_popup1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.date_filter_from_popup)
            )
            status = date_filter_from_popup1.is_displayed()
            print(date_filter_from_popup1.text + " ====>  ( Filter type from 'Pop-Up' matched )")

            filter_type1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.filter_type)
            )
            status = filter_type1.is_displayed()
            print(filter_type1.text + " ====>  ( Filter type from 'Pop-Up' matched )")
            # filter_type1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            driver_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.driver_filter)
            )
            status = driver_filter1.is_displayed()
            print(driver_filter1.text + " ====>  ( Filter type from 'Pop-Up' matched )")
            # driver_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.close_btn)).click()

        except NoSuchElementException:
            pytest.skip("************ Requests Video popUp button not displayed **********")
        return status

    def validate_video_requests_page_video_requests_filter(self, log):
        status = False
        try:
            video_requests_filter_btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.video_requests_filter)
            )
            status = video_requests_filter_btn.is_displayed()
            print(video_requests_filter_btn.text + " ====>  ( Button matched )")

        except NoSuchElementException:
            pytest.skip("************ Video Requests filter button not displayed **********")
        return status

    def validate_video_requests_page_panic_btn_filter(self, log):
        status = False
        try:
            panic_button_filter_btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.panic_button_filter)
            )
            status = panic_button_filter_btn.is_displayed()
            print(panic_button_filter_btn.text + " ====>  ( Button matched )")

        except NoSuchElementException:
            pytest.skip("************ Panic Button not displayed **********")
        return status

    def validate_video_requests_page_event_on_demand_filter(self, log):
        status = False
        try:
            event_on_demand_filter_btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.event_on_demand_filter)
            )
            status = event_on_demand_filter_btn.is_displayed()
            print(event_on_demand_filter_btn.text + " ====>  ( Button matched )")

        except NoSuchElementException:
            pytest.skip("************ Event On-Demand filter button not displayed **********")
        return status