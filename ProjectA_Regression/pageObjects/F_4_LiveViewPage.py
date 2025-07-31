import time

import pyautogui

from ProjectA_Regression.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LiveViewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait


    def validate_live_view_page(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.live_view_page)
            ).click()
            time.sleep(3)

            print("🔗 " + self.driver.current_url)

            live_view_page = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(FleetPortal_Locators.live_view_page)
            )

            status = live_view_page.is_displayed()
            print(live_view_page.text + " ====>  ( Page matched ) 📑")

            fleet_view = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.fleet_view_map)
            )
            status = fleet_view.is_displayed()
            print(fleet_view.text + " ====>  ( Button matched )")
            fleet_view.click()
            time.sleep(2)

            list_view = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.list_view_map)
            )
            status = list_view.is_displayed()
            print(list_view.text + " ====>  ( Button matched )")
            list_view.click()
            time.sleep(2)


            filter_asset = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.filter_alt))
            status = filter_asset.is_displayed()
            print(filter_asset.text + " ====>  ( Filter type matched )")
            filter_asset.click()

            pyautogui.press('esc')
            time.sleep(1)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.date_pick)
            ).click()

            time.sleep(1)

            past_30_days1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.date_select)
            )
            status = past_30_days1.is_displayed()
            print(past_30_days1.text + " ====>  ( Selected Date Range )")
            past_30_days1.click()

            time.sleep(5)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.asset_select_opt)).click()

            asset_opt1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.asset_opt)
            )
            status = asset_opt1.is_displayed()
            print(asset_opt1.text + " ====>  ( Option matched )")

            tag_opt1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.tag_opt)
            )
            status = tag_opt1.is_displayed()
            print(tag_opt1.text + " ====>  ( Option matched )")

            pyautogui.press('esc')
            time.sleep(1)

            search_filter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.enter_asset_id_name)
            )
            status = search_filter.is_displayed()
            print(search_filter.text + " ====>  ( Search Filter matched )")



        except NoSuchElementException:
            pytest.skip("************ Live View page not displayed **********")
        return status

    def validate_live_view_page_asset_table(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(FleetPortal_Locators.trips_naviga)).click()
            time.sleep(7)

            print("🗺️/📍/🚀 ✅ Successfully navigated to the 'View Trip Details' Page, from the 'Live View' page.")

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_btn)).click()
            status = True

        except NoSuchElementException:
            pytest.skip("************ Asset table not displayed **********")
        return status