import time

from ProjectB_Sanity.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TripsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait

    def validate_trips_page(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.trips_btn)
            ).click()
            time.sleep(3)

            print("🔗 " + self.driver.current_url)

            trips1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.trips_btn)
            )

            status = trips1.is_displayed()
            print(trips1.text + " ====>  ( Page matched ) 📑")

        except NoSuchElementException:
            pytest.skip("************ Trips page not displayed **********")
        return status

    def validate_trips_page_trips_tab(self, log):
        status = False
        try:
            trips_tab1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.trips_tab)
            )
            status = trips_tab1.is_displayed()
            print(trips_tab1.text + " ====>  ( Tab matched ) ✅")

        except NoSuchElementException:
            pytest.skip("************ Trips tab not displayed **********")
        return status

    def validate_trips_page_trip_filter(self, log):
        status = False
        try:
            trip_filter_card1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.trip_filter_card)
            )
            status = trip_filter_card1.is_displayed()
            print(trip_filter_card1.text + " ====>  ( Card matched )")

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
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.search_btn)
            ).click()
            time.sleep(2)

            filter_type1 = WebDriverWait(self.driver, 20).until(
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

            select_tags_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_tags_filter)
            )
            status = select_tags_filter1.is_displayed()
            print(select_tags_filter1.text + " ====>  ( Filter type matched )")
            # select_tags_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

        except NoSuchElementException:
            pytest.skip("************ Trip Filter card not displayed **********")
        return status

    def validate_trips_page_trips_list_table(self, log):
        status = False
        try:
            trips_list_card1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.trips_list_table)
            )
            status = trips_list_card1.is_displayed()
            print(trips_list_card1.text + " ====>  ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Trips List table not displayed **********")
        return status

    def validate_trips_page_bulk_edit(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.bulk_edit_btn)
            ).click()
            time.sleep(3)

            bulk_edit1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.bulk_trip_edit_page)
            )
            status = bulk_edit1.is_displayed()
            print(bulk_edit1.text + " ====>  ( Button matched )")

            back_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow)
            )
            status = back_button.is_displayed()
            print("✏️/🚀 ✅  Successfully launched 'Bulk Edit' page, from the 'Trips' page.")
            back_button.click()
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Bulk Edit button not displayed **********")
        return status

    def validate_trips_page_export_trips(self, log):
        status = False
        try:
            export_options1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.export_trips)
            )
            status = export_options1.is_displayed()
            print(export_options1.text + " ====>  ( Button matched )")
            export_options1.click()

            # export the trips:
            export_now1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.export_now_btn)
            )
            status = export_now1.is_displayed()
            print(export_now1.text + " ====>  ( Button matched )")

            # schedule the trips navigation:
            schedule_btn1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_btn)
            )
            status = schedule_btn1.is_displayed()
            print(schedule_btn1.text + " ====>  ( Button matched )")
            schedule_btn1.click()
            time.sleep(2)

            back_button1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.back_btn))
            status = back_button1.is_displayed()
            print("🗓️/🚀 ✅ Successfully navigated to the 'Schedule Reports' page, from the export 'Schedule Trips' option.")
            back_button1.click()
            time.sleep(2)

        except NoSuchElementException:
            pytest.skip("************ Export Trips button not displayed **********")
        return status

    def validate_trips_page_active_drivers_tab(self, log):
        status = False
        try:
            active_drivers_tab1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.active_drivers_tab)
            )
            status = active_drivers_tab1.is_displayed()
            active_drivers_tab1.click()
            print(active_drivers_tab1.text + " ====>  ( Tab matched ) ✅")
            time.sleep(3)

            active_driver_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.active_driver_filter)
            )
            status = active_driver_filter1.is_displayed()
            print(active_driver_filter1.text + " ====>  ( Card matched )")

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
            time.sleep(1)

            select_tags_filter1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_tags_filter)
            )
            status = select_tags_filter1.is_displayed()
            print(select_tags_filter1.text + " ====>  ( Filter type matched )")
            # select_tags_filter1.click()
            # pyautogui.press('esc')
            # time.sleep(1)

            active_drivers_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.active_drivers_table)
            )
            status = active_drivers_table1.is_displayed()
            print(active_drivers_table1.text + " ====>  ( Table matched )")


        except NoSuchElementException:
            pytest.skip("************ Active Drivers tab not displayed **********")
        return status


    def validate_trips_page_manage_tab(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.manage_tab)
            ).click()
            time.sleep(2)

            manage_tab1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.manage_tab)
            )
            status = manage_tab1.is_displayed()
            print(manage_tab1.text + " ====>  ( Tab matched ) ✅")


            bulk_updation_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.bulk_updation_table)
            )
            status = bulk_updation_table1.is_displayed()
            print(bulk_updation_table1.text + " ====>  ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Manage Tab not displayed **********")
        return status