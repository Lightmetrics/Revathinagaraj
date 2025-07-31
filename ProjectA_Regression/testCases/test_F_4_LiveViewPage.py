import pytest
from ProjectA_Regression.pageObjects.F_4_LiveViewPage import LiveViewPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_LiveViewPage_Test(BaseClass):

    def test_live_view_page_btn(self):
        log = self.getLogger()
        fleetportal = LiveViewPage(self.driver)

        log.info("===== Validating Live View Button presence =====")
        live_view_status = fleetportal.validate_live_view_page(log)

        if live_view_status:
            log.info(" :  ✅ Live View page button is present.")
        else:
            log.error(" :  ❌ Live View page button is NOT present.")
        assert live_view_status, "Live View page button should be present."

    def test_live_view_page_asset_table(self):
        log = self.getLogger()
        fleetportal = LiveViewPage(self.driver)

        log.info("===== Validating Asset Table presence =====")
        asset_table_status = fleetportal.validate_live_view_page_asset_table(log)

        if asset_table_status:
            log.info(" :  ✅ Asset Table is present.")
        else:
            log.error(" :  ❌ Asset Table is NOT present.")
        assert asset_table_status, "Asset Table should be present."