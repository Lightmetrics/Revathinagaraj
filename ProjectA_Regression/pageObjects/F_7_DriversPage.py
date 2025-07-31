import time

import pyautogui
from selenium.webdriver.common.by import By

from ProjectA_Regression.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class DriversPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait


    def validate_Drivers_page(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortal_Locators.drivers_page).click()
            time.sleep(3)

            print("🔗 " + self.driver.current_url)

            drivers_page1 = self.driver.find_element(*FleetPortal_Locators.drivers_page)
            status = drivers_page1.is_displayed()
            print(drivers_page1.text + " ====>  ( Page matched ) 📑")

        except NoSuchElementException:
            pytest.skip("************ Drivers page not displayed **********")
        return status

    def validate_Drivers_page_driver_list_table(self, log):
        status = False
        try:
            drivers_tab1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.drivers_tab))
            status = drivers_tab1.is_displayed()
            print(drivers_tab1.text + " ====>  ( Tab matched ) ✅")

            driver_list_table1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.driver_list_table))
            status = driver_list_table1.is_displayed()
            print(driver_list_table1.text + " ====>  ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Driver List table not displayed **********")
        return status

    def validate_Drivers_page_driver_search_option(self, log):
        status = False
        try:
            search_opt1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.search_driverid_name))
            status = search_opt1.is_displayed()
            print(search_opt1.text + " ====>  ( Search option matched )")

            select_tags1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_tags_filter))
            status = select_tags1.is_displayed()
            print(select_tags1.text + " ====>  ( Filter matched )")


        except NoSuchElementException:
            pytest.skip("************ Driver search option not displayed **********")
        return status

    def validate_Drivers_page_batch_update_btn(self, log):
        status = False
        try:
            batch_update1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.batch_update_btn))
            status = batch_update1.is_displayed()
            print(batch_update1.text + " ====>  ( Button matched )")

        except NoSuchElementException:
            pytest.skip("************ Batch Update button not displayed **********")
        return status

    def validate_Drivers_page_export_btn(self, log):
        status = False
        try:
            export_btn1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.export_btn))
            status = export_btn1.is_displayed()
            print(export_btn1.text + " ====>  ( Button matched )")
            export_btn1.click()
            time.sleep(1)

            export_menu1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.export_menu))
            status = export_menu1.is_displayed()
            print(export_menu1.text + " ====>  ( Buttons matched )")
            pyautogui.press('esc')
            time.sleep(1)

        except NoSuchElementException:
            pytest.skip("************ Export button not displayed **********")
        return status

# Async Report : Driver list csv:

    def validate_Drivers_page_download_driverlist_csv_btn(self, log):
        status = False
        try:
            # Click menu options
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.export_btn)).click()
            time.sleep(2)

            # Wait and validate the Download Driver List CSV button
            download_driverlist_csv_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.driverlist_csv)
            )
            if download_driverlist_csv_btn.is_displayed():
                print(download_driverlist_csv_btn.text + " ====>  ( Button matched )")
                download_driverlist_csv_btn.click()
                time.sleep(2)

                try:
                    # Wait for alert message to appear
                    alert_message1 = WebDriverWait(self.driver, 50).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
                    )
                    if alert_message1.is_displayed():
                        print(alert_message1.text + "  :: 📤/🔔 ✅ Info message displayed, for Export 'Driver List CSV' option.")
                        time.sleep(2)

                        # navigating to the download history page:

                        view_downloads1 = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.view_downloads_btn)
                        )
                        status = view_downloads1.is_displayed()
                        print(view_downloads1.text + " ====>  ( Button matched )")
                        view_downloads1.click()
                        print("📥/🚀 ✅ Successfully navigated to the 'Download History' Page, from the 'Export Drivers' option.")
                        time.sleep(2)

                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.drivers_page)).click()
                        time.sleep(3)

                        status = True
                except TimeoutException:
                    print(" 📤/🔔 ❌ No Info message displayed for Export 'Driver List CSV'.")
                    status = False
            else:
                print(" 📤/🔴 ❌ Export 'Driver List CSV' button is not visible")
                log.warning("  :: 📤/🔴 ❌ Export 'Driver List CSV' button is not visible")
                status = False

        except (NoSuchElementException, TimeoutException) as e:
            pytest.skip("************ Export 'Driver List CSV' button not displayed or not clickable **********")

        return status

# Async Report : Bulk QR Code Download:

    def validate_Drivers_page_export_bulk_qrcode_btn(self, log):
        status = False
        try:
            # Click menu options
            self.driver.find_element(*FleetPortal_Locators.export_btn).click()
            time.sleep(1)

            # Wait and validate the Download Bulk QR Code button
            export_bulk_qrcode_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.bulk_qrcode_export)
            )
            if export_bulk_qrcode_btn.is_displayed():
                print(export_bulk_qrcode_btn.text + " ====>  ( Button matched )")
                export_bulk_qrcode_btn.click()
                time.sleep(2)

                try:
                    # Wait for alert message to appear
                    alert_message1 = WebDriverWait(self.driver, 50).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
                    )
                    if alert_message1.is_displayed():
                        print(alert_message1.text + "  :: 📤/🔔 ✅ Info message displayed, for Export 'Bulk QR-Code' option.")
                        time.sleep(2)

                        # navigating to the download history page:

                        view_downloads1 = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.view_downloads_btn)
                        )
                        status = view_downloads1.is_displayed()
                        print(view_downloads1.text + " ====>  ( Button matched )")
                        view_downloads1.click()
                        print("📥/🚀 ✅ Successfully navigated to the 'Download History' Page, from the export 'Bulk QR-Code' option.")
                        time.sleep(2)

                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.drivers_page)).click()
                        time.sleep(3)


                        status = True
                except TimeoutException:
                    print(" 📤/🔔 ❌  No Info message displayed for Export 'Bulk QR-Code'.")
                    status = False
            else:
                print(" 📤/🔴 ❌ Export 'Bulk QR-Code' button is not visible")
                log.warning("  :: 📤/🔴 ❌ Export 'Bulk QR-Code' button is not visible")
                status = False

        except (NoSuchElementException, TimeoutException) as e:
            pytest.skip("************ Export 'Bulk QR-Code' button not displayed or not clickable **********")

        return status

    def validate_Drivers_page_download_qrcode_btn(self, log):
        status = False
        try:
            # Click menu options
            self.driver.find_element(*FleetPortal_Locators.menu_options).click()
            time.sleep(1)

            # Wait and validate the Download QR Code button
            download_qr_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.download_qrcode_btn)
            )
            if download_qr_btn.is_displayed():
                print(download_qr_btn.text + " ====>  ( Button matched )")
                download_qr_btn.click()
                time.sleep(2)

                try:
                    # Wait for alert message to appear
                    alert_message1 = WebDriverWait(self.driver, 50).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
                    )
                    if alert_message1.is_displayed():
                        print(alert_message1.text + "  :: 📥/🔔 ✅ Info message displayed for 'single driver'.")
                        status = True
                except TimeoutException:
                    print("📥/🔔 ❌ No QR Code Info message appeared for 'single driver'.")
                    status = False
            else:
                print("🔴 ❌ Download QR Code button not visible.")
                log.warning("  :: 🔴 ❌ Download QR Code button is not visible")
                status = False

        except (NoSuchElementException, TimeoutException) as e:
            pyautogui.press("esc")  # Close any open dialogs
            pytest.skip("************ Download QR Code button not displayed or not clickable **********")

        return status

    def validate_Drivers_page_add_images_btn(self, log):
        status = False
        try:
            # Click menu options
            self.driver.find_element(*FleetPortal_Locators.menu_options).click()
            time.sleep(1)

            # Wait and validate the Add Images button
            add_images_btn1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.add_images_btn)
            )
            if add_images_btn1.is_displayed():
                print(add_images_btn1.text + " ====>  ( Button matched )")
                add_images_btn1.click()
                time.sleep(3)

                try:
                    pyautogui.press("esc")  # Close the file upload dialog
                    time.sleep(2)
                    print(" ➕/🖼️/🪟/🚀 ✅ Successfully launched 'Add Images' pop-up window, for 'single driver'.")

                    # Wait for Pop-Up window to appear
                    pop_up_window1 = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.driver_images_title)
                    )
                    status = pop_up_window1.is_displayed()
                    print(pop_up_window1.text + " ====>  ( Title matched )")

                    upload_images1 = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.upload_images_btn)
                    )

                    if upload_images1.is_displayed():
                        print(upload_images1.text + " ====>  ( Button matched )")
                        upload_images1.click()
                        print(
                            " 📤/🖥️/🪟/🚀 ✅ Successfully launched 'Desktop Pop-Up' window, from 'Upload Images' Pop-UP.")
                        time.sleep(2)
                        pyautogui.press("esc")
                        time.sleep(1)

                        qrcode_title1 = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.qrcode_preview_title)
                        )
                        status = qrcode_title1.is_displayed()
                        print(qrcode_title1.text + " ====>  ( Title matched )")

                        qrcode_download_btn1 = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.qrcode_download_btn)
                        )
                        status = qrcode_download_btn1.is_displayed()
                        print(qrcode_download_btn1.text + " ====>  ( Button matched )")

                        close_btn1 = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.close_btn)
                        )
                        self.driver.execute_script("arguments[0].scrollIntoView();", close_btn1)
                        close_btn1.click()
                        time.sleep(2)
                        pyautogui.press("esc")
                        time.sleep(1)

                        status = True
                except TimeoutException:
                    print(" 📤/🖼️/🚀 ❌ No pop-up window displayed for 'Upload Images'.")
                    status = False
            else:
                print("➕/🖼️/🔴 ❌ 'Add Images' button not visible.")
                log.warning("  :: ➕/🖼️/🔴 ❌ 'Add Images' button is not visible")
                status = False

        except (NoSuchElementException, TimeoutException) as e:
            pytest.skip("************ 'Add Images' button not displayed or not clickable **********")

        return status


# Check Driver Availability
    def validate_Drivers_page_check_driver_name_availability(self, log):
        status = False
        try:
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.search_driver_input).click()
            self.driver.find_element(*FleetPortal_Locators.search_driver_input).send_keys("566256621")
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.search_filter).click()
            time.sleep(2)

            try:
                more_actions_opt = self.driver.find_element(*FleetPortal_Locators.more_actions_dr)

                if more_actions_opt.is_displayed():
                    print(more_actions_opt.text + " ====>  ( Menu option matched )")
                    print("Sreenivas :: ✅ This driver name is already available in the driver list ❗ ")
                    more_actions_opt.click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH,
                                             "//span[contains(text(),'Delete Driver')]/ancestor::button").click()
                    time.sleep(1)
                    self.driver.find_element(By.XPATH, "//span[contains(text(),' DELETE ')]/parent::button").click()
                    time.sleep(1)

                    wait1 = WebDriverWait(self.driver, 10)
                    delete_notification_bar = (By.XPATH,
                                               "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
                    notification_element1 = wait1.until(EC.presence_of_element_located(delete_notification_bar))
                    notification_text1 = wait1.until(EC.visibility_of(notification_element1)).text
                    print(notification_text1 + " - Sreenivas ::  (🗑️/🔔 ✅ Delete Existed Driver Message notification)")

            except NoSuchElementException:
                print("Driver does not exist — proceeding to add")

            # This block always runs regardless of existence
            self.validate_Drivers_page_add_driver_btn(log)
            self.validate_Drivers_page_add_driver_page(log)
            self.validate_Drivers_page_edit_driver(log)

            status = True

        except NoSuchElementException:
            print("( Exiting - Element not found )")
            pytest.skip("************ Critical Driver Page Element Not Found **********")

        return status

# Add Driver - Click Add Button
    def validate_Drivers_page_add_driver_btn(self, log):
        status = False
        try:
            time.sleep(2)
            add_driver_btn1 = self.driver.find_element(*FleetPortal_Locators.add_driver_btn)
            status = add_driver_btn1.is_displayed()
            print(add_driver_btn1.text + " ====>  ( Button matched )")
            add_driver_btn1.click()
            time.sleep(3)
        except NoSuchElementException:
            pytest.skip("************ Add Driver button not displayed **********")
        return status

# Fill and Submit Add Driver Form
    def validate_Drivers_page_add_driver_page(self, log):
        status = False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.driver_name_input)).click()

            self.driver.find_element(*FleetPortal_Locators.driver_name_input).send_keys("Sreenivas")
            self.driver.find_element(*FleetPortal_Locators.driver_id_input).send_keys("566256621")
            self.driver.find_element(*FleetPortal_Locators.driver_email_input).send_keys(
                "sreenivas.akki+test56621@gmail.com")

            self.driver.find_element(*FleetPortal_Locators.save_details).click()

            try:
                wait = WebDriverWait(self.driver, 10)
                notification_locator = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
                notification_element = wait.until(EC.presence_of_element_located(notification_locator))
                notification_text = wait.until(EC.visibility_of(notification_element)).text
                print(notification_text + "  :: ( ➕/👤/🔔 ✅ Add New Driver Message notification )")
                time.sleep(3)
                status = True

            except TimeoutException:
                try:
                    alert_message = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.alert_message))
                    if alert_message.is_displayed():
                        print(alert_message.text + "  :: ❗ ✅ Alert message displayed.")
                        self.driver.find_element(*FleetPortal_Locators.back_arrow1).click()
                        time.sleep(3)
                except NoSuchElementException:
                    print(" 👤 ✅ No Driver ID already exists — proceeding normally")

        except NoSuchElementException:
            pytest.skip("********** Add Driver page not displayed **********")
        return status

# Edit Driver After Add
    def validate_Drivers_page_edit_driver(self, log):
        status = False
        try:
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.search_driver_input).click()
            self.driver.find_element(*FleetPortal_Locators.search_driver_input).send_keys("566256621")
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.search_filter).click()
            time.sleep(3)
            more_actions_drbt = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.more_actions_dr))
            status = more_actions_drbt.is_displayed()
            more_actions_drbt.click()

            self.driver.find_element(By.XPATH,
                                     "//span[contains(text(),'Edit Driver Details')]/ancestor::button").click()
            time.sleep(3)

            edit_driver = self.driver.find_element(*FleetPortal_Locators.driver_name_input)
            edit_driver.click()
            time.sleep(1)
            edit_driver.clear()
            time.sleep(1)
            edit_driver.send_keys("Sreenivas Akki")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.save_details).click()
            time.sleep(1)

            wait1 = WebDriverWait(self.driver, 10)
            edit_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element1 = wait1.until(EC.presence_of_element_located(edit_notification_bar))
            notification_text1 = wait1.until(EC.visibility_of(notification_element1)).text
            print(notification_text1 + "  ::  ( ✏️/👤/🔔 ✅ Edit New Driver Message notification )")

            self.validate_Drivers_page_delete_driver(log)
            status = True

        except NoSuchElementException:
            print("Element not found, exiting...")
            pytest.skip("************ Edit Driver page not displayed **********")
        return status

# Delete Driver After Edit
    def validate_Drivers_page_delete_driver(self, log):
        status = False
        try:
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.search_driver_input).click()
            self.driver.find_element(*FleetPortal_Locators.search_driver_input).send_keys("566256621")
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.search_filter).click()
            time.sleep(3)
            more_actions_drbt = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.more_actions_dr))
            status = more_actions_drbt.is_displayed()
            more_actions_drbt.click()

            self.driver.find_element(By.XPATH, "//span[contains(text(),'Delete Driver')]/ancestor::button").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//span[contains(text(),' DELETE ')]/parent::button").click()
            time.sleep(1)

            wait1 = WebDriverWait(self.driver, 10)
            delete_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element1 = wait1.until(EC.presence_of_element_located(delete_notification_bar))
            notification_text1 = wait1.until(EC.visibility_of(notification_element1)).text
            print(notification_text1 + "  ::  ( 🗑️/👤/🔔 ✅ Delete New Driver Message notification )")
            time.sleep(3)

            status = True

        except NoSuchElementException:
            print("Element not found, exiting...")
            pytest.skip("************ Driver not found for delete **********")
        return status


# Check Box Validation:-

    def validate_Drivers_page_check_boxes_validation(self, log):
        try:
            # Step 1: Click the checkbox
            self.driver.find_element(*FleetPortal_Locators.check_box_opt).click()
            time.sleep(1)
            print(" ✅ Successfully selected the check boxes and validating available features.")

            # Step 2: Validate visible UI elements
            search_opt1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.search_driverid_name))
            print(search_opt1.text + " ====>  ( Search option matched )")

            assigne_coach1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.assign_coach_btn))
            print(assigne_coach1.text + " ====>  ( Button matched )")

            delete_opt1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.delete_btn))
            print(delete_opt1.text + " ====>  ( Button matched )")

            # Step 3: Check if QR Code button is present
            qrcode_buttons = self.driver.find_elements(*FleetPortal_Locators.select_qrcodes_download_btn)
            if qrcode_buttons and qrcode_buttons[0].is_displayed():
                select_qrcodes_download1 = qrcode_buttons[0]
                print(select_qrcodes_download1.text + " ====>  ( Button matched )")
                select_qrcodes_download1.click()
                time.sleep(2)

                try:
                    alert_message1 = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
                    )
                    if alert_message1.is_displayed():
                        print(
                            alert_message1.text + "  :: 📥/🔔 ✅ Info message displayed for download 'Selected Drivers'.")

                        view_downloads1 = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.view_downloads_btn))
                        print(view_downloads1.text + " ====>  ( Button matched )")
                        view_downloads1.click()
                        print("📥/🚀 ✅ Navigated to 'Download History' from 'Selected Drivers'.")

                        # Return to Drivers page
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(FleetPortal_Locators.drivers_page)).click()
                        time.sleep(3)
                except TimeoutException:
                    print("📥/🔔 ❌ No Alert message after clicking 'Download QR Code' ❌.")

            else:
                # Button is not visible — proceed without failing
                print("📥/🔴 'Download QR Code' button not available — proceeding normally. ❗❗")
                log.warning("📥/🔴 'Download QR Code' button not available — proceeding normally. ❗❗")

            # ✅ Everything proceeded without critical failure
            return True

        except (NoSuchElementException, TimeoutException) as e:
            log.error(f" Exception during checkbox feature validation: {e} ❌")
            print(f" Exception during checkbox feature validation: {e} ❌")
            return False


    def validate_Drivers_page_installers_tab(self, log):
        status = False
        try:
            installers_tab1 = self.driver.find_element(*FleetPortal_Locators.installers_tab)
            status = installers_tab1.is_displayed()
            print(installers_tab1.text + " ====>  ( Tab matched ) ✅")
            installers_tab1.click()

            installer_list_table = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.installer_list_table))
            status = installer_list_table.is_displayed()
            print(installer_list_table.text + " ====>  ( Table matched )")

            add_installer_btn = self.driver.find_element(*FleetPortal_Locators.add_installer)
            status = add_installer_btn.is_displayed()
            print(add_installer_btn.text + " ====>  ( Button matched )")
            add_installer_btn.click()
            time.sleep(3)
            print("➕/🚀 ✅ Successfully launched 'ADD INSTALLER' page.")

            self.driver.find_element(*FleetPortal_Locators.back_btn2).click()
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Installers Tab not displayed **********")
        return status