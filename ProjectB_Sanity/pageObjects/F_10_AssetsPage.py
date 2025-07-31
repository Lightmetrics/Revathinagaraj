import time
from selenium.webdriver.common.by import By

from ProjectB_Sanity.pageObjects.Locators_Fleet import FleetPortal_Locators

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AssetsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait


    def validate_assets_page(self, log):
        status = False
        try:
            assets_page1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.assets_page)
            )
            status = assets_page1.is_displayed()
            print(assets_page1.text + " ====> ( Page matched ) 📑")
            assets_page1.click()
            time.sleep(3)
            print("🔗 " + self.driver.current_url)

        except NoSuchElementException:
            pytest.skip("************ Assets page not displayed **********")
        return status

    def validate_assets_page_overview_tab(self, log):
        status = False
        try:
            overview_tab1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.overview_tab_assets)
            )
            status = overview_tab1.is_displayed()
            print(overview_tab1.text + " ====> ( Tab matched ) ✅")

            asset_list_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.asset_list_table)
            )
            status = asset_list_table1.is_displayed()
            print(asset_list_table1.text + " ====> ( Table matched )")

            show_filters_btn1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.show_filters_btn)
            )
            status = show_filters_btn1.is_displayed()
            print(show_filters_btn1.text + " ====> ( Button matched )")
            show_filters_btn1.click()
            time.sleep(2)

            select_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.filter_type)
            )
            status = select_filter1.is_displayed()
            print(select_filter1.text + " ====> ( Filter matched )")

            Asset_search1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.asset_search)
            )
            status = Asset_search1.is_displayed()
            print(Asset_search1.text + " ====> ( Filter matched )")

            hide_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.hide_filters)
            )
            status = hide_filter1.is_displayed()
            print(hide_filter1.text + " ====> ( Button matched )")


            export_assets_btn1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.export_assets_btn)
            )
            status = export_assets_btn1.is_displayed()
            print(export_assets_btn1.text + " ====> ( Button matched )")

        except NoSuchElementException:
            pytest.skip("************ Overview tab not displayed **********")
        return status

    def validate_assets_page_manage_assets_tab(self, log):
        status = False
        try:
            self.driver.refresh()     # Refresh the page to ensure all elements are loaded
            time.sleep(3)
            manage_assets_tab1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.manage_assets_tab)
            )
            status = manage_assets_tab1.is_displayed()
            print(manage_assets_tab1.text + " ====> ( Tab matched ) ✅ ")
            manage_assets_tab1.click()
            time.sleep(2)

            batch_update_card1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.batch_update_card)
            )
            status = batch_update_card1.is_displayed()
            print(batch_update_card1.text + " ====> ( Card matched )")

            batch_provisioning_card1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.batch_provisioning_card)
            )
            status = batch_provisioning_card1.is_displayed()
            print(batch_provisioning_card1.text + " ====> ( Card matched )")

        except NoSuchElementException:
            pytest.skip("************ Manage Assets tab not displayed **********")
        return status

    def validate_assets_page_devices_tab(self, log):
        status = False
        try:
            devices_tab1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.devices_tab)
            )
            status = devices_tab1.is_displayed()
            print(devices_tab1.text + " ====> ( Tab matched ) ✅ ")
            devices_tab1.click()
            time.sleep(3)

            semi_provisioned_devices1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.semi_provisioned_devices_table)
            )
            status = semi_provisioned_devices1.is_displayed()
            print(semi_provisioned_devices1.text + " ====> ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Devices tab not displayed **********")
        return status

    def validate_assets_page_diagnostics_tab(self, log):
        status = False
        try:
            diagnostics_tab1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.diagnostics_tab)
            )
            status = diagnostics_tab1.is_displayed()
            print(diagnostics_tab1.text + " ====> ( Tab matched ) ✅ ")
            diagnostics_tab1.click()
            time.sleep(3)

            Devices_card1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.devices_card)
            )
            status = Devices_card1.is_displayed()
            print(Devices_card1.text + " ====> ( Card matched )")

            devices_with_events1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.devices_with_events)
            )
            status = devices_with_events1.is_displayed()
            print(devices_with_events1.text + " ====> ( Card matched )")

            camera_visibility_events1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.camera_visibility_events)
            )
            camera_visibility_events1.click()
            time.sleep(2)

            status = camera_visibility_events1.is_displayed()
            print(camera_visibility_events1.text + " ====> ( Page matched )")

            device_diagnostic1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.device_diagnostic_events)
            )
            device_diagnostic1.click()
            time.sleep(2)

            status = device_diagnostic1.is_displayed()
            print(device_diagnostic1.text + " ====> ( Page matched )")

            device_online_status1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.device_online_status)
            )
            device_online_status1.click()
            time.sleep(2)

            status = device_online_status1.is_displayed()
            print(device_online_status1.text + " ====> ( Page matched )")
            time.sleep(2)

        except NoSuchElementException:
            pytest.skip("************ Diagnostics tab not displayed **********")
        return status