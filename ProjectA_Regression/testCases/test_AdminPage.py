import pytest
from ProjectA_Regression.pageObjects.AdminPage import AdminPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class AdminPortal(BaseClass):


    def test_admin_login(self):
        log = self.getLogger()
        log.info("===== Test Case: Admin Portal Login =====")
        print("===== Starting Admin Portal Login Test =====")

        try:
            admin = AdminPage(self.driver)
            admin.loginToAdminPage(log)

            expected_title = "Admin Portal"
            actual_title = self.driver.title

            log.info(" : ******* "f" ✅ Actual Title: {actual_title}")
            print(f"Expected Title: {expected_title}")
            print(f"🌐 ✅ Actual Title: {actual_title}")
            assert expected_title in actual_title, f" ❌ Expected title '{expected_title}' not found."

        except Exception as e:
            log.error(" : ******* "f" ❌ Exception during login test: {str(e)}")
            print(f" ❌ Exception during login test: {str(e)}")
            assert False, "Test failed due to exception."


    def test_customer_selection_and_master_portal(self):
        log = self.getLogger()
        log.info("===== Test Case: Switch to Master Portal =====")
        print("===== Starting Customer Selection and Master Portal Switch Test =====")

        try:
            admin = AdminPage(self.driver)
            admin.customer_tsp(log)

            expected_title = "Master Portal"
            actual_title = self.driver.title

            log.info(" : ******* "f" ✅ Actual Title after switch: {actual_title}")
            print(f"Expected Title after switch: {expected_title}")
            print(f" ✅ Actual Title after switch: {actual_title}")
            assert expected_title in actual_title, f"❌ Expected title '{expected_title}' not found."

        except Exception as e:
            log.error(" : ******* "f" ❌ Exception during Master Portal switch: {str(e)}")
            print(f" ❌ Exception during Master Portal switch: {str(e)}")
            assert False, "Test failed due to exception."
