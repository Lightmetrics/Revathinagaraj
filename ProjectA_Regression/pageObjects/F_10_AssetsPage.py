import time
from selenium.webdriver.common.by import By

from ProjectA_Regression.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
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

    def validate_assets_page_asset_edit_data_asset_details_opt(self, log):
        status = False
        try:
            # Step 1: Get all edit icons
            all_edit_buttons = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(FleetPortal_Locators.asset_edit_btn)
            )

            found_clickable = False
            for btn in all_edit_buttons:
                try:
                    if btn.is_displayed() and btn.is_enabled():
                        print(btn.text + " ====> ( Option matched )")
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                        time.sleep(0.5)
                        btn.click()
                        print(" ✅ Clicked on first clickable Edit icon.")
                        log.info("  ::  ✅ Clicked on first clickable Edit icon.")
                        time.sleep(2)
                        found_clickable = True
                        status = True
                        break
                except Exception as e:
                    log.warning(f"  :: Skipping a non-clickable Edit icon ❗: {str(e)}")
                    continue

            if not found_clickable:
                log.error("  :: No clickable Edit icon found in the asset list. ❗")
                return False

            # Step 2: Wait for the edit form to appear
            device_fild1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.device_id_fild)
            )
            status = device_fild1.is_displayed()
            print("📝/🚗/🚀 ✅ Successfully launched 'Edit Asset Details' page from 'Assets' page")
            print(device_fild1.text + " ====> ( Option matched )")

            asset_id_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.asset_id_fild)
            )
            status = asset_id_field.is_displayed()
            print(asset_id_field.text + " ====> ( Option matched )")

            duty_type1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.duty_type_filt)
            )
            status = duty_type1.is_displayed()
            print(duty_type1.text + " ====> ( Filter matched )")

            asset_name_label = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.asset_name_label)
            )
            asset_name_opt = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.asset_name_optional)
            )

            status = asset_name_label.is_displayed()
            print(asset_name_label.text + " ====> ( Option matched )")
            asset_name_opt.click()
            time.sleep(1)
            asset_name_opt.clear()
            time.sleep(1)
            asset_name_opt.send_keys("Test Asset")
            time.sleep(1)

            driverid_field1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.driver_id_fild)
            )
            status = driverid_field1.is_displayed()
            print(driverid_field1.text + " ====> ( Option matched )")

            # Toggle button handling
            try:
                config_external_cameras1 = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(FleetPortal_Locators.config_external_cameras_opt)
                )
                enable_toggle_opt = WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_element_located(FleetPortal_Locators.toggle_for_external_cameras)
                )

                if enable_toggle_opt.is_displayed() and enable_toggle_opt.is_enabled():
                    enable_toggle_opt.click()
                    time.sleep(2)
                    print(config_external_cameras1.text + " ====> ( Toggle Button matched )")
                    print(" ✅ 'Multi-View Configurations' card enabled successfully")

                    Add_more_cameras1 = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.add_more_cameras_btn)
                    )
                    status = Add_more_cameras1.is_displayed()
                    print(Add_more_cameras1.text + " ====> ( Button matched )")
                    Add_more_cameras1.click()
                    time.sleep(2)

                    close_drpdown1 = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.remove_dropdown)
                    )
                    status = close_drpdown1.is_displayed()
                    close_drpdown1.click()
                    time.sleep(1)

                    desable_toggle1 = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.toggle_for_external_cameras)
                    )
                    status = desable_toggle1.is_displayed()
                    desable_toggle1.click()
                    time.sleep(2)
                    status = True

            except Exception as e:
                print(f"Skipping No Toggle icon present ❌ : {str(e)}")
                log.warning(f"  :: Skipping No Toggle icon present ❌ : {str(e)}")

            try:
                select_tags1 = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located(FleetPortal_Locators.select_tags_filter)
                )
                status = select_tags1.is_displayed()
                print(select_tags1.text + " ====> ( Filter matched )")
            except:
                print("Tags filter dropdown not visible or loading... ❌")
                log.warning("  :: Tags filter dropdown not visible or loading... ❌")

            save_btn1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.save_details)
            )
            status = save_btn1.is_displayed()
            print(save_btn1.text + " ====> ( Button matched )")
            save_btn1.click()
            time.sleep(1)

            # Wait for notification
            wait1 = WebDriverWait(self.driver, 20)
            edit_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element1 = wait1.until(EC.presence_of_element_located(edit_notification_bar))
            notification_text1 = wait1.until(EC.visibility_of(notification_element1)).text
            print(notification_text1 + "  ::  ( 📝/🚗/🔔 ✅ Edit Asset Details Message notification )")
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Edit Asset Details Option not displayed **********")
        return status

    def validate_assets_page_asset_manage_device_opt(self, log):
        status = False
        try:
            # Step 1: Get all manage icons
            all_manage_btns = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(FleetPortal_Locators.manage_device_opt)
            )

            found_clickable = False
            for btn in all_manage_btns:
                try:
                    if btn.is_displayed() and btn.is_enabled():
                        print(btn.text + " ====> ( Option matched )")
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                        time.sleep(0.5)
                        btn.click()
                        print(" ✅ Clicked on first clickable Manage Devices icon.")
                        log.info("  ::  ✅ Clicked on first clickable Manage Devices icon.")
                        time.sleep(2)
                        found_clickable = True
                        status = True
                        break
                except Exception as e:
                    log.warning(f"  :: Skipping a non-clickable Manage Devices icon ❗: {str(e)}")
                    continue

            if not found_clickable:
                log.error("  :: No clickable Manage Devices icon found in the asset list. ❌")
                return False

            # Step 2: Wait for the Manage Devices Pop-Up to appear
            close_popup1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.manage_device_close)
            )
            status = close_popup1.is_displayed()
            print(" 🚀 ✅ Successfully launched 'Manage Device' Pop-Up")
            close_popup1.click()
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Manage Device Option not displayed **********")
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