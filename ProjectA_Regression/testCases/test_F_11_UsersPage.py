import pytest
from ProjectA_Regression.pageObjects.F_11_UsersPage import UsersPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_UsersPage_Test(BaseClass):


    def test_users_page(self):
        log = self.getLogger()
        users_page = UsersPage(self.driver)

        log.info("===== Validating Users Page presence =====")
        users_page_status = users_page.validate_users_page(log)

        if users_page_status:
            log.info(" :  ✅ Users Page is present.")
        else:
            log.error(" :  ❌ Users Page is NOT present.")
        assert users_page_status, "Users Page should be present."


    def test_users_tab(self):
        log = self.getLogger()
        users_page = UsersPage(self.driver)

        log.info("===== Validating Users Tab presence =====")
        users_tab_status = users_page.validate_users_page_users_tab(log)

        if users_tab_status:
            log.info(" :  ✅ Users Tab is present.")
        else:
            log.error(" :  ❌ Users Tab is NOT present.")
        assert users_tab_status, "Users Tab should be present."


    def test_manage_users_table_data(self):
        log = self.getLogger()
        users_page = UsersPage(self.driver)

        log.info("===== Validating Manage Users Table Data =====")
        manage_users_table_data_status = users_page.validate_users_page_manage_users_table_data(log)

        if manage_users_table_data_status:
            log.info(" :  ✅ Manage Users Table Data is present.")
        else:
            log.error(" :  ❌ Manage Users Table Data is NOT present.")
        assert manage_users_table_data_status, "Manage Users Table Data should be present."


    def test_users_page_roles_tab(self):
        log = self.getLogger()
        users_page = UsersPage(self.driver)

        log.info("===== Validating Roles Tab presence =====")
        roles_tab_status = users_page.validate_users_page_roles_tab(log)

        if roles_tab_status:
            log.info(" :  ✅ Roles Tab is present.")
        else:
            log.error(" :  ❌ Roles Tab is NOT present.")
        assert roles_tab_status, "Roles Tab should be present."


    def test_manage_roles_table_data(self):
        log = self.getLogger()
        users_page = UsersPage(self.driver)

        log.info("===== Validating Manage Roles Table Data =====")
        manage_roles_table_data_status = users_page.validate_users_page_manage_roles_table_data(log)

        if manage_roles_table_data_status:
            log.info(" :  ✅ Manage Roles Table Data is present.")
        else:
            log.error(" :  ❌ Manage Roles Table Data is NOT present.")
        assert manage_roles_table_data_status, "Manage Roles Table Data should be present."

    def test_users_page_user_activity_log_tab(self):
        log = self.getLogger()
        users_page = UsersPage(self.driver)

        log.info("===== Validating User Activity Log Tab presence =====")
        user_activity_log_tab_status = users_page.validate_users_page_user_activity_log_tab(log)

        if user_activity_log_tab_status:
            log.info(" :  ✅ User Activity Log Tab is present.")
        else:
            log.error(" :  ❌ User Activity Log Tab is NOT present.")
        assert user_activity_log_tab_status, "User Activity Log Tab should be present."

