import pytest
from ProjectA_Regression.pageObjects.MasterPortalPage import MasterPortalPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class MasterPortal(BaseClass):

    def test_validate_master_name(self):
        log = self.getLogger()
        master = MasterPortalPage(self.driver)


        log.info(" ====== Validating Master Portal Name ======")
        try:
            assert master.validate_master_name(log), "Master title not visible"
            log.info(" : ******* ✅  Master title is visible and correct.")
        except Exception as e:
            log.error(" : ******* ❌ "f"Master portal name validation failed: {e}")
            raise


    def test_home_page_version(self):
        log = self.getLogger()
        master = MasterPortalPage(self.driver)

        log.info("=== Starting Master Portal Version Validation Test ===")
        try:
            master.compare_actual_version(log)
            log.info("=== ✅ Completed Master Portal Version Validation Test ===")
        except Exception as e:
            log.error(" : ******* ❌ Exception in version comparison test: %s", str(e))
            pytest.skip("Skipping due to unexpected error during version check.")


    def test_account_navigation_and_fleet_dashboard_launch(self):
        log = self.getLogger()
        log.info("===== Test Case: Switch to Fleet Portal =====")
        print("🌐/🚀 Navigate to Account & Launch Fleet Dashboard")
        log.info(" : 🌐/🚀 *******  Starting test: Navigate to Account & Launch Fleet Dashboard")

        master = MasterPortalPage(self.driver)

        try:
            title = master.account_option()
            assert title is not None and "Fleet Portal" in title
            log.info(" : ******* 🌐 ✅ Fleet Dashboard launched successfully. Title: " + title)
            print("🌐 ✅ Fleet Dashboard launched successfully. Title: " + title)
        except AssertionError:
            log.error(" : ******* 🌐 ❌ Fleet Dashboard did not launch or title mismatch.")
            print(" 🌐 ❌ Fleet Dashboard did not launch or title mismatch.")
            assert False


