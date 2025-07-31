import time

import pyautogui
from selenium.webdriver.common.by import By

from ProjectB_Sanity.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class UsersPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait


    def validate_users_page(self, log):
        status = False
        try:
            users_page1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.users_page)
            )
            status = users_page1.is_displayed()
            print(users_page1.text + " ====> ( Page matched ) 📑")
            users_page1.click()
            time.sleep(3)
            print("🔗 " + self.driver.current_url)

        except NoSuchElementException:
            pytest.skip("************ User page not displayed **********")
        return status

    def validate_users_page_users_tab(self, log):
        status = False
        try:
            users_tab1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.users_tab)
            )
            status = users_tab1.is_displayed()
            print(users_tab1.text + " ====> ( Tab matched ) ✅ ")

            manage_users_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.manage_users_table)
            )
            status = manage_users_table1.is_displayed()
            print(manage_users_table1.text + " ====> ( Table matched )")

            add_user1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.add_user_btn)
            )
            status = add_user1.is_displayed()
            print(add_user1.text + " ====> ( Button matched )")

        except NoSuchElementException:
            pytest.skip("************ Users Tab not displayed **********")
        return status

    def validate_users_page_manage_users_table_data(self, log):
        status = False
        try:
            # add_user
            self.driver.find_element(*FleetPortal_Locators.add_user_btn).click()
            add_user_page1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.email_address1)
            )
            status = add_user_page1.is_displayed()
            print("➕/👤/🚀 ✅ Successfully launched Add Users page, from 'Users Page'.")
            add_user_page1.click()

            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.email_address1).send_keys("akkisrinivassri+123@gmail.com")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.select_role).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.administrator).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.name).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.name).send_keys("Sreenivas Akki")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.save_btn).click()
            time.sleep(1)

            wait1 = WebDriverWait(self.driver, 10)
            add_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element1 = wait1.until(EC.presence_of_element_located(add_notification_bar))

            # Once the notification element is present, wait for it to be visible
            notification_text1 = wait1.until(EC.visibility_of(notification_element1)).text
            print(notification_text1 + "  ::  ( ➕/👤/🔔 ✅ Add New User Message notification )")

            # update_user
            time.sleep(3)
            self.driver.find_element(*FleetPortal_Locators.refresh).click()
            time.sleep(3)

            search_user1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.search_user)
            )
            status = search_user1.is_displayed()
            search_user1.click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_user).send_keys("akkisrinivassri+123@gmail.com")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_btn).click()

            time.sleep(3)

            edit_user_btn1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.edit)
            )
            status = edit_user_btn1.is_displayed()
            print(edit_user_btn1.text + " ====> ( Button matched )")
            edit_user_btn1.click()
            time.sleep(3)

            edit_user_name1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.edit_user_name)
            )
            status = edit_user_name1.is_displayed()
            print("✏️/👤/🚀 ✅ Successfully launched Edit User page, from 'Users Page'.")
            edit_user_name1.click()

            # Press and hold the backspace key for 2 seconds
            pyautogui.keyDown('backspace')
            time.sleep(2)
            pyautogui.keyUp('backspace')

            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.edit_user_name).send_keys("Sreenivasulu Akki")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.save_btn).click()
            time.sleep(1)

            wait2 = WebDriverWait(self.driver, 10)
            edit_notification_bar2 = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element2 = wait2.until(EC.presence_of_element_located(edit_notification_bar2))

            # Once the notification element is present, wait for it to be visible
            notification_text2 = wait2.until(EC.visibility_of(notification_element2)).text
            print(notification_text2 + "  ::  ( ✏️/👤/🔔 ✅ Edit New User message notification )")
            # resend_temporary_password
            time.sleep(3)
            self.driver.find_element(*FleetPortal_Locators.refresh).click()
            time.sleep(5)

            search_user2 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.search_user)
            )
            status = search_user2.is_displayed()
            search_user2.click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_user).send_keys("akkisrinivassri+123@gmail.com")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_btn).click()

            time.sleep(3)

            self.driver.find_element(*FleetPortal_Locators.three_dots).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.resend_temporary_password).click()
            time.sleep(1)

            wait3 = WebDriverWait(self.driver, 15)
            user_temporary_password = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element3 = wait3.until(EC.presence_of_element_located(user_temporary_password))

            # Once the notification element is present, wait for it to be visible
            notification_text3 = wait3.until(EC.visibility_of(notification_element3)).text
            print(notification_text3 + "  ::  ( 📩/👤/🔔 ✅ User 'Resend Temporary Password' message notification )")
            # delete_user
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.three_dots).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.delete_user_opt).click()
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.delete_user_pop_up).click()
            time.sleep(2)

            # Wait for the notification element to be present
            alert_message2 = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
            )
            status = alert_message2.is_displayed()
            print(alert_message2.text + "  ::  ( 🗑️/🧑‍💼/🔔 ✅ Info message displayed for 'Delete User' )")
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.close_pop_up).click()
            time.sleep(3)




        except NoSuchElementException:
            pytest.skip("************ Manage Users Table not displayed **********")
        return status

    def validate_users_page_roles_tab(self, log):
        status = False
        try:
            self.driver.find_element(*FleetPortal_Locators.roles_tab).click()
            time.sleep(3)
            roles_tab1 = self.driver.find_element(*FleetPortal_Locators.roles_tab)
            status = roles_tab1.is_displayed()
            print(roles_tab1.text + " ====> ( Tab matched ) ✅ ")

            manage_roles_table1 = self.driver.find_element(*FleetPortal_Locators.manage_roles_table)
            status = manage_roles_table1.is_displayed()
            print(manage_roles_table1.text + " ====> ( Table matched )")

            view_hierarchy_btn1 = self.driver.find_element(*FleetPortal_Locators.view_hierarchy_btn)
            status = view_hierarchy_btn1.is_displayed()
            print(view_hierarchy_btn1.text + " ====> ( Button matched )")

            add_role_btn1 = self.driver.find_element(*FleetPortal_Locators.add_role_btn)
            status = add_role_btn1.is_displayed()
            print(add_role_btn1.text + " ====> ( Button matched )")

        except NoSuchElementException:
            pytest.skip("************ Roles tab not displayed **********")
        return status

    def validate_users_page_manage_roles_table_data(self, log):
        status = False
        try:
        # add_role
            self.driver.find_element(*FleetPortal_Locators.add_role_btn).click()
            time.sleep(3)
            select_temp1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.choose_template)
            )
            status = select_temp1.is_displayed()
            select_temp1.click()
            self.driver.find_element(*FleetPortal_Locators.select_template_btn).click()
            time.sleep(2)
            role_name1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.role_name)
            )
            status = role_name1.is_displayed()
            print("➕/🧑‍💼/🚀 ✅ Successfully launched Add Role page, from 'Roles Page'.")
            role_name1.click()

            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.role_name).send_keys("Sreenivas Akki Role")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.select_hierarchy_leve_opt).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.hierarchy_level).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.save_btn).click()
            time.sleep(1)

            wait1 = WebDriverWait(self.driver, 10)
            add_notification_bar = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element1 = wait1.until(EC.presence_of_element_located(add_notification_bar))

            # Once the notification element is present, wait for it to be visible
            notification_text1 = wait1.until(EC.visibility_of(notification_element1)).text
            print(notification_text1 + "  ::  ( ➕/🧑‍💼/🔔 ✅ Add New Role Message notification )")

        # update_role
            time.sleep(3)
            self.driver.find_element(*FleetPortal_Locators.refresh).click()
            time.sleep(3)

            search_role1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.search_role)
            )
            status = search_role1.is_displayed()
            search_role1.click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_role).send_keys("Sreenivas Akki Role")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_btn).click()

            time.sleep(3)

            edit_role_btn1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.edit)
            )
            status = edit_role_btn1.is_displayed()
            print(edit_role_btn1.text + " ====> ( Button matched )")
            edit_role_btn1.click()
            time.sleep(3)

            edit_role_name1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.role_name)
            )
            status = edit_role_name1.is_displayed()
            print("✏️/🧑‍💼/🚀 ✅ Successfully launched Edit Role page, from 'Roles Page'.")
            edit_role_name1.click()

            # Press and hold the backspace key for 2 seconds
            pyautogui.keyDown('backspace')
            time.sleep(2)
            pyautogui.keyUp('backspace')

            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.role_name).send_keys("Sreenivas Role")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.save_btn).click()
            time.sleep(1)

            wait2 = WebDriverWait(self.driver, 10)
            edit_notification_bar2 = (By.XPATH, "//simple-snack-bar[contains(@class,'mat-simple-snackbar')]/span")
            notification_element2 = wait2.until(EC.presence_of_element_located(edit_notification_bar2))

            # Once the notification element is present, wait for it to be visible
            notification_text2 = wait2.until(EC.visibility_of(notification_element2)).text
            print(notification_text2 + "  ::  ( ✏️/🧑‍💼/🔔 ✅ Edit New Role message notification )")
            # resend_temporary_password
            time.sleep(3)
            self.driver.find_element(*FleetPortal_Locators.refresh).click()
            time.sleep(5)

            search_role2 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.search_role)
            )
            status = search_role2.is_displayed()
            search_role2.click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_role).send_keys("Sreenivas Role")
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.search_btn).click()
            time.sleep(3)

        # deactivate_role
            self.driver.find_element(*FleetPortal_Locators.three_dots).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.deactivate_role).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.deactivate_btn).click()
            time.sleep(3)

            # Wait for the notification element to be present
            alert_message1 = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
            )
            status = alert_message1.is_displayed()
            print(alert_message1.text + "  ::  ( 🚫/🧑‍💼/🔔 ✅ Info message displayed for 'deactivate role' )")
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.close_pop_up).click()
            time.sleep(2)

        # activate_role
            three_dots1 = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(FleetPortal_Locators.three_dots)
            )
            status = three_dots1.is_displayed()
            three_dots1.click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.activate_role).click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.activate_btn).click()
            time.sleep(3)

            # Wait for the notification element to be present
            alert_message2 = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
            )
            status = alert_message2.is_displayed()
            print(alert_message2.text + "  ::  ( 🔓/🧑‍💼/🔔 ✅ Info message displayed for 'Activate Role' )")
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.close_pop_up).click()
            time.sleep(3)


        # delete_role
            three_dots2 = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(FleetPortal_Locators.three_dots)
            )
            status = three_dots2.is_displayed()
            three_dots2.click()
            time.sleep(1)
            self.driver.find_element(*FleetPortal_Locators.delete_role_opt).click()
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.delete_role_pop_up).click()
            time.sleep(5)

            # Wait for the notification element to be present
            alert_message2 = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located(FleetPortal_Locators.alert_message)
            )
            status = alert_message2.is_displayed()
            print(alert_message2.text + "  ::  ( 🗑️/🧑‍💼/🔔 ✅ Info message displayed for 'Delete Role' )")
            time.sleep(2)
            self.driver.find_element(*FleetPortal_Locators.close_pop_up).click()
            time.sleep(3)


        except NoSuchElementException:
            pytest.skip("************ Manage Roles table data not displayed **********")
        return status

    def validate_users_page_user_activity_log_tab(self, log):
        status = False
        try:
            activity_log1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FleetPortal_Locators.activity_log_tab)
            )
            status = activity_log1.is_displayed()
            print(activity_log1.text + " ====> ( Tab matched ) ✅ ")
            activity_log1.click()
            time.sleep(2)

            user_activity_log_table1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FleetPortal_Locators.activity_log_table)
            )
            status = user_activity_log_table1.is_displayed()
            print(user_activity_log_table1.text + " ====> ( Table matched )")

        except NoSuchElementException:
            pytest.skip("************ User Activity Log tab not displayed **********")
        return status