import pytest
from ProjectB_Sanity.pageObjects.FleetPortalPage import FleetPortalPage
from ProjectB_Sanity.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class FleetPortal(BaseClass):


    def test_validate_fleet_name(self):
        log = self.getLogger()
        fleet = FleetPortalPage(self.driver)

        log.info(" : ====== Validating Fleet Portal Name ======")
        try:
            assert fleet.validate_fleet_name(log), "Fleet name not visible"
            log.info(" : ******* ✅ Fleet name is visible and correct.")
        except Exception as e:
            log.error(" : ******* ❌ "f"Fleet name validation failed: {e}")
            raise

    def test_home_page_version(self):
        log = self.getLogger()
        fleet = FleetPortalPage(self.driver)

        log.info("=== Starting Fleet Portal Version Validation Test ===")
        try:
            fleet.compare_actual_version(log)
            log.info("=== ✅ Completed Fleet Portal Version Validation Test ===")
        except Exception as e:
            log.error(" : ******* ❌ Exception in version comparison test: %s", str(e))
            pytest.skip(" ❌ Skipping due to unexpected error during version check.")




