import pytest
from ProjectB_Sanity.pageObjects.AdminPage import AdminPage
from ProjectB_Sanity.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class AdminPortal(BaseClass):

    def test_admin_login(self, config):
        log = self.getLogger()
        log.info("===== Test Case: Admin Portal Login =====")

        try:
            admin = AdminPage(self.driver)
            admin.loginToAdminPage(log)

            expected_title = "Admin Portal"
            actual_title = self.driver.title

            log.info(f"✅ Actual Title: {actual_title}")
            assert expected_title in actual_title, f" ❌ Expected title '{expected_title}' not found."

        except Exception as e:
            log.error(f" ❌ Exception during login test: {str(e)}")
            assert False, "Test failed due to exception."

    def test_customer_selection_and_master_portal(self, config):
        log = self.getLogger()
        log.info("===== Test Case: Switch to Master Portal =====")

        try:
            admin = AdminPage(self.driver)
            admin.customer_tsp(log, config)

            expected_title = "Master Portal"
            actual_title = self.driver.title

            log.info(f"✅ Actual Title after switch: {actual_title}")
            assert expected_title in actual_title, f"❌ Expected title '{expected_title}' not found."

        except Exception as e:
            log.error(f" ❌ Exception during Master Portal switch: {str(e)}")
            assert False, "Test failed due to exception."


