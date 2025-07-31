import pytest
from ProjectB_Sanity.pageObjects.F_4_LiveViewPage import LiveViewPage
from ProjectB_Sanity.utilities.BaseClass import BaseClass


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