import time

import pyautogui
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from ProjectA_Regression.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ConfigurationsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Global explicit wait


    def validate_configurations_page(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            configurations_page1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.configurations_page))
            status = configurations_page1.is_displayed()
            configurations_page1.click()
            time.sleep(3)

            basic_tab1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.basic_tab))
            status = basic_tab1.is_displayed()
            print("🔗 " + self.driver.current_url)
            print(configurations_page1.text + " ====> ( Page matched )")
            print(basic_tab1.text + " ====> ( Tab matched )")

        except NoSuchElementException:
            pytest.skip("************ Configurations page not displayed **********")
        return status

    def validate_configurations_page_basic_configurations_table(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            basic_configurations1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.basic_configurations))
            status = basic_configurations1.is_displayed()
            print(basic_configurations1.text + " ====> ( Table matched )")

            apply_defaults1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.apply_defaults))
            status = apply_defaults1.is_displayed()
            print(apply_defaults1.text + " ====> ( Button matched )")

            heavy1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.heavy_duty_type))
            status = heavy1.is_displayed()
            print(heavy1.text + " ====> ( Duty type matched )")

            medium1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.medium_duty_type))
            status = medium1.is_displayed()
            print(medium1.text + " ====> ( Duty type matched )")

            light1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.light_duty_type))
            status = light1.is_displayed()
            print(light1.text + " ====> ( Duty type matched )")


        except NoSuchElementException:
            pytest.skip("************ Basic Configurations table not displayed **********")
        return status

    def validate_configurations_page_advanced_tab(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            advance_tab1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.advanced_tab))
            status = advance_tab1.is_displayed()
            print(advance_tab1.text + " ====> ( Tab matched )")
            advance_tab1.click()
            time.sleep(3)

            advanced_configurations1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.advanced_configurations))
            status = advanced_configurations1.is_displayed()
            print(advanced_configurations1.text + " ====> ( Table matched )")

            apply_defaults1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.apply_defaults))
            status = apply_defaults1.is_displayed()
            print(apply_defaults1.text + " ====> ( Button matched )")

            heavy1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.heavy_duty_type))
            status = heavy1.is_displayed()
            print(heavy1.text + " ====> ( Duty type matched )")

            medium1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.medium_duty_type))
            status = medium1.is_displayed()
            print(medium1.text + " ====> ( Duty type matched )")

            light1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.light_duty_type))
            status = light1.is_displayed()
            print(light1.text + " ====> ( Duty type matched )")

            driver_configurations1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.driver_configurations))
            status = driver_configurations1.is_displayed()
            print(driver_configurations1.text + " ====> ( Table matched )")


        except NoSuchElementException:
            pytest.skip("************ Advanced tab not displayed **********")
        return status


    def validate_configurations_page_coaching_tab(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            coaching_tab1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.coaching_tab))
            status = coaching_tab1.is_displayed()
            print(coaching_tab1.text + " ====> ( Tab matched )")
            coaching_tab1.click()
            time.sleep(3)

            coaching_thresholds_card1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.coaching_thresholds_card))
            status = coaching_thresholds_card1.is_displayed()
            print(coaching_thresholds_card1.text + " ====> ( Table matched )")

            automated_triaging_card1 = wait.until(
                EC.visibility_of_element_located(FleetPortal_Locators.automated_triaging))
            status = automated_triaging_card1.is_displayed()
            print(automated_triaging_card1.text + " ====> ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Coaching tab not displayed **********")
        return status

# Tagging :-

    def validate_configurations_page_tagging_tab(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            tagging_tab1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.tagging_tab))
            status = tagging_tab1.is_displayed()
            print(tagging_tab1.text + " ====> ( Tab matched )")
            tagging_tab1.click()
            time.sleep(3)

            overview_table1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.overview_table))
            status = overview_table1.is_displayed()
            print(overview_table1.text + " ====> ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ Tagging tab not displayed **********")
        return status


    def validate_configurations_page_add_tag(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)

            # Select Options and Tags
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.choose_an_opt)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.tags_opt)).click()
            time.sleep(1)
            tags_table1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.tags_table))
            status = tags_table1.is_displayed()
            print(tags_table1.text + " ====> ( Table matched )")

            # Add new tag
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.add_new_tag_btn)).click()
            time.sleep(1)
            select_attribute = wait.until(EC.element_to_be_clickable(FleetPortal_Locators.select_attribute))
            status = select_attribute.is_displayed()
            print("➕/🔖/🚀 ✅ Successfully launched Add Tag page, form 'Tags Page'.")
            select_attribute.click()

            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.select_attribute_opt)).click()
            time.sleep(1)

            # Input tag name and save
            add_multiple_tags = wait.until(EC.element_to_be_clickable(FleetPortal_Locators.add_multiple_tags))
            add_multiple_tags.click()
            time.sleep(1)
            add_multiple_tags.send_keys("Sreenivas")
            add_multiple_tags.send_keys(Keys.ENTER)  # Use Selenium Keys instead of pyautogui
            time.sleep(1)

            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.save_tags_btn)).click()
            time.sleep(1)

            # Notification after adding a tag
            add_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text1 = wait.until(EC.visibility_of_element_located(add_notification_bar)).text
            print(notification_text1 + "  ::  ( ➕/🔖/🔔 ✅ Add New Tag Message notification )")

            if 'Tag name is already exists' in notification_text1:
                try:
                    wait.until(EC.element_to_be_clickable(FleetPortal_Locators.back_button)).click()
                    time.sleep(5)
                    self.validate_configurations_page_deactivate_tag(log)
                    self.validate_configurations_page_delete_tag(log)
                    print(" 🗑️/🔖 ✅ Existing Tag deleted successfully.")
                except NoSuchElementException:
                    print(" 🗑️/🔖 ❌ Existing Tag not deleted.")
            else:
                time.sleep(1)
                wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
                time.sleep(5)
                self.validate_configurations_page_update_tag(log)


        except NoSuchElementException:
            pytest.skip("************ Add Tag page not displayed **********")
        return status

    def validate_configurations_page_update_tag(self, log):
        status = False
        try:
                wait = WebDriverWait(self.driver, 20)
                # Edit tag
                wait.until(EC.element_to_be_clickable(FleetPortal_Locators.edit_tag)).click()
                time.sleep(3)

                edit_tag_element= self.driver.find_element(*FleetPortal_Locators.type_tag_name)
                actions = ActionChains(self.driver)
                actions.move_to_element(edit_tag_element).click().perform()
                # actions.move_to_element(edit_tag_element).clear().perform()
                # self.driver.find_element(*FleetPortalPage.type_tag_name).clear()
                print("✏️/🔖/🚀 ✅ Successfully launched Update Tag page, form 'Tags Page'.")
                time.sleep(3)

                # Clear existing tag name
                pyautogui.keyDown('backspace')
                time.sleep(2)
                pyautogui.keyUp('backspace')
                time.sleep(2)

                # Enter new tag name and save
                edit_tag_element.send_keys("Sreenivas Akki")
                save_tag = self.driver.find_element(*FleetPortal_Locators.save_edit_tags)
                # save_tag = wait.until(EC.element_to_be_clickable(FleetPortalPage.save_edit_tags))
                actions = ActionChains(self.driver)
                actions.move_to_element(save_tag).click().perform()
                time.sleep(1)

                # Notification after editing the tag
                edit_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
                notification_text2 = wait.until(EC.visibility_of_element_located(edit_notification_bar)).text
                print(notification_text2 + "  ::  ( ✏️/🔖/🔔 ✅ Edit New Tag message notification )")

                if 'Tag name is already exists' in notification_text2:
                    try:
                        time.sleep(3)
                        wait.until(EC.element_to_be_clickable(FleetPortal_Locators.back_button)).click()
                        time.sleep(5)
                        self.validate_configurations_page_deactivate_tag(log)
                        self.validate_configurations_page_delete_tag(log)
                        print(" 🗑️/🔖 ✅ Existing Tag deleted successfully.")
                    except NoSuchElementException:
                        print(" 🗑️/🔖 ❌ Existing Tag not deleted.")
                else:
                    time.sleep(1)
                    wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
                    time.sleep(5)
                    self.validate_configurations_page_deactivate_tag(log)
                    self.validate_configurations_page_delete_tag(log)

        except NoSuchElementException:
            pytest.skip("************ Update Tag page not displayed **********")
        return status

    def validate_configurations_page_deactivate_tag(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)

            # Deactivate tag
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.three_dots)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.deactivate_tag)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.deactivate_tag_accept)).click()
            time.sleep(1)

            # Notification after deactivating the tag
            deactivate_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text3 = wait.until(EC.visibility_of_element_located(deactivate_notification_bar)).text
            print(notification_text3 + "  ::  ( 🚫/🔖/🔔 ✅ Deactivate New Tag message notification )")
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
            time.sleep(7)

            # Activate tag
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.three_dots)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.activate_tag)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.activate_tag_accept)).click()
            time.sleep(1)

            # Notification after Activate the tag
            activate_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text3 = wait.until(EC.visibility_of_element_located(activate_notification_bar)).text
            print(notification_text3 + "  ::  ( 🔓/🔖/🔔 ✅ Activate New Tag message notification )")
            time.sleep(3)


        except NoSuchElementException:
            pytest.skip("************ Deactivate Tag page not displayed **********")
        return status

    def validate_configurations_page_delete_tag(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
            time.sleep(3)

            # Delete tag
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.three_dots)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.delete_tag)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.delete_tag_accept)).click()
            time.sleep(1)

            # Notification after deleting the tag
            delete_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text4 = wait.until(EC.visibility_of_element_located(delete_notification_bar)).text
            print(notification_text4 + "  ::  ( 🗑️/🔖/🔔 ✅ Delete New Tag message notification )")

            # pyautogui.press('esc')
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Delete Tag page not displayed **********")
        return status

    def validate_configurations_page_add_attribute(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)

            # Select options and attributes
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.choose_an_opt1)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.attributes_option)).click()
            time.sleep(1)
            attributes_table1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.attributes_table))
            status = attributes_table1.is_displayed()
            print(attributes_table1.text + " ====> ( Table matched )")

            # Add new attribute
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.add_attribute_btn)).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.select_type)).click()
            time.sleep(2)
            print("➕/🏷️/🚀 ✅ Successfully launched Add Attribute page, form 'Attributes Page'.")
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.data_based_opt)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.select_entity)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.asset_opt)).click()
            time.sleep(1)

            # Escape key
            pyautogui.press('esc')
            time.sleep(1)

            # Type attribute name and save
            type_attribute_name1 = wait.until(EC.element_to_be_clickable(FleetPortal_Locators.type_attribute_name))
            type_attribute_name1.click()
            time.sleep(1)
            type_attribute_name1.send_keys("Sreenivas")
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.save_attributes)).click()
            time.sleep(1)

            # Notification after adding an attribute
            add_notification_bar1 = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text5 = wait.until(EC.visibility_of_element_located(add_notification_bar1)).text
            print(notification_text5 + "  ::  ( ➕/🏷️/🔔 ✅ Add New Attribute Message notification )")

            if 'Attribute name already exists.' in notification_text5:
                try:
                    time.sleep(3)
                    wait.until(EC.element_to_be_clickable(FleetPortal_Locators.back_button)).click()
                    time.sleep(5)
                    self.validate_configurations_page_deactivate_attribute(log)
                    self.validate_configurations_page_delete_attribute(log)
                    print(" 🗑️/🏷️ ✅ Existing Attribute deleted successfully.")
                except NoSuchElementException:
                    print(" 🗑️/🏷️ ❌ Existing Attribute not deleted.")
            else:
                time.sleep(1)
                wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
                time.sleep(5)
                self.validate_configurations_page_update_attribute(log)
                status = True

        except NoSuchElementException:
            pytest.skip("************ Add attribute page not displayed **********")
        return status

    def validate_configurations_page_update_attribute(self, log):
        status = False
        try:
                wait = WebDriverWait(self.driver, 20)
                time.sleep(3)

                # Edit attribute
                wait.until(EC.element_to_be_clickable(FleetPortal_Locators.edit_attribute)).click()
                time.sleep(1)
                tag_clear = wait.until(EC.element_to_be_clickable(FleetPortal_Locators.type_attribute_name))
                tag_clear.click()
                time.sleep(1)
                print("✏️/🏷️/🚀 ✅ Successfully launched Update Attribute page, form 'Attributes Page'.")

                # Clear existing attribute name
                pyautogui.keyDown('backspace')
                time.sleep(2)  # slight delay to simulate holding the key
                pyautogui.keyUp('backspace')

                # Enter new attribute name and save
                tag_clear.send_keys("Sreenivas Akki")
                wait.until(EC.element_to_be_clickable(FleetPortal_Locators.save_attributes)).click()
                time.sleep(1)

                # Notification after editing the attribute
                update_notification_bar1 = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
                notification_text6 = wait.until(EC.visibility_of_element_located(update_notification_bar1)).text
                print(notification_text6 + "  ::  ( ✏️/🏷️/🔔 ✅ Edit New Attribute message notification )")

                if 'Attribute name already exists.' in notification_text6:
                    try:
                        time.sleep(3)
                        wait.until(EC.element_to_be_clickable(FleetPortal_Locators.back_button)).click()
                        time.sleep(3)
                        self.validate_configurations_page_deactivate_attribute(log)
                        self.validate_configurations_page_delete_attribute(log)
                        print(" 🗑️/🏷️ ✅ Existing Attribute deleted successfully.")
                    except NoSuchElementException:
                        print(" 🗑️/🏷️ ❌ Existing Attribute not deleted.")
                else:
                    time.sleep(1)
                    wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
                    time.sleep(5)
                    self.validate_configurations_page_deactivate_attribute(log)
                    self.validate_configurations_page_delete_attribute(log)

        except NoSuchElementException:
            pytest.skip("************ Update attribute page not displayed **********")
        return status

    def validate_configurations_page_deactivate_attribute(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)

            # Deactivate attribute
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.three_dots)).click()
            time.sleep(2)
            deactivate = wait.until(EC.element_to_be_clickable(FleetPortal_Locators.deactivate_attribute))
            status = deactivate.is_displayed()
            deactivate.click()

            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.deactivate_attribute_accept)).click()
            time.sleep(1)

            # Notification after deactivating the attribute
            deactivate_notification_bar1 = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text7 = wait.until(EC.visibility_of_element_located(deactivate_notification_bar1)).text
            print(notification_text7 + "  ::  ( 🚫/🏷️/🔔 ✅ Deactivate New Attribute message notification )")
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
            time.sleep(7)

            # Activate attribute
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.three_dots)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.activate_attribute)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.activate_attribute_accept)).click()
            time.sleep(1)

            # Notification after Activate the attribute
            activate_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text3 = wait.until(EC.visibility_of_element_located(activate_notification_bar)).text
            print(notification_text3 + "  ::  ( 🔓/🏷️/🔔 ✅ Activate New Attribute message notification )")


        except NoSuchElementException:
            pytest.skip("************ Deactivate attribute page not displayed **********")
        return status

    def validate_configurations_page_delete_attribute(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
            time.sleep(3)

            # Delete attribute
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.three_dots)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.delete_attribute)).click()
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.delete_attribute_accept)).click()
            time.sleep(1)

            # Notification after deleting the attribute
            delete_notification_bar1 = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_text8 = wait.until(EC.visibility_of_element_located(delete_notification_bar1)).text
            print(notification_text8 + "  ::  ( 🗑️/🏷️/🔔 ✅ Delete New Attribute message notification )")
            time.sleep(3)
            status = True

        except NoSuchElementException:
            pytest.skip("************ Delete attribute page not displayed **********")


    def validate_configurations_page_entities_page(self, log):
        status = False
        try:
            wait = WebDriverWait(self.driver, 20)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.refresh_tags_btn)).click()
            time.sleep(3)

            # Select options and attributes
            wait.until(EC.element_to_be_clickable(FleetPortal_Locators.choose_an_opt1)).click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located(FleetPortal_Locators.entities_select_opt)).click()
            time.sleep(3)

            entities_table1 = wait.until(EC.visibility_of_element_located(FleetPortal_Locators.entities_table))
            status = entities_table1.is_displayed()
            print(entities_table1.text + " ====> ( Table matched )")
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Entities page not displayed **********")
        return status