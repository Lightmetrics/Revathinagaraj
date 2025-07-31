import pytest
from ProjectA_Regression.pageObjects.F_6_VideoRequestsPage import VideoRequestsPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_VideoRequestsPage_Test(BaseClass):

    def test_video_requests_page(self):
        log = self.getLogger()
        fleetportal = VideoRequestsPage(self.driver)

        log.info("===== Validating Video Requests Page presence =====")
        video_requests_page_status = fleetportal.validate_video_requests_page(log)

        if video_requests_page_status:
            log.info(" :  ✅ Video Requests Page is present.")
        else:
            log.error(" :  ❌ Video Requests Page is NOT present.")
        assert video_requests_page_status, "Video Requests Page should be present."


    def  test_video_requests_page_table(self):
        log = self.getLogger()
        fleetportal = VideoRequestsPage(self.driver)

        log.info("===== Validating Video Requests Table presence =====")
        video_requests_table_status = fleetportal.validate_video_requests_page_table(log)

        if video_requests_table_status:
            log.info(" :  ✅ Video Requests Table is present.")
        else:
            log.error(" :  ❌ Video Requests Table is NOT present.")
        assert video_requests_table_status, "Video Requests Table should be present."


    def test_video_requests_page_video_request(self):
        log = self.getLogger()
        fleetportal = VideoRequestsPage(self.driver)

        log.info("===== Validating Request Video PopUp presence =====")
        video_requests_popUp_status = fleetportal.validate_video_requests_page_request_video_popUp(log)

        if video_requests_popUp_status:
            log.info(" :  ✅ Request Video PopUp is present.")
        else:
            log.error(" :  ❌ Request Video PopUp is NOT present.")
        assert video_requests_popUp_status, "Request Video PopUp should be present."


    def test_video_requests_page_filter(self):
        log = self.getLogger()
        fleetportal = VideoRequestsPage(self.driver)

        log.info("===== Validating Video Requests Filter presence =====")
        video_requests_filter_status = fleetportal.validate_video_requests_page_video_requests_filter(log)

        if video_requests_filter_status:
            log.info(" :  ✅ Video Requests Filter is present.")
        else:
            log.error(" :  ❌ Video Requests Filter is NOT present.")
        assert video_requests_filter_status, "Video Requests Filter should be present."


    def test_video_requests_page_panic_btn_filter(self):
        log = self.getLogger()
        fleetportal = VideoRequestsPage(self.driver)

        log.info("===== Validating Panic Button Filter presence =====")
        panic_button_filter_status = fleetportal.validate_video_requests_page_panic_btn_filter(log)

        if panic_button_filter_status:
            log.info(" :  ✅ Panic Button Filter is present.")
        else:
            log.error(" :  ❌ Panic Button Filter is NOT present.")
        assert panic_button_filter_status, "Panic Button Filter should be present."


    def test_video_requests_page_event_on_demand_filter(self):
        log = self.getLogger()
        fleetportal = VideoRequestsPage(self.driver)

        log.info("===== Validating Event On Demand Filter presence =====")
        event_on_demand_filter_status = fleetportal.validate_video_requests_page_event_on_demand_filter(log)

        if event_on_demand_filter_status:
            log.info(" :  ✅ Event On Demand Filter is present.")
        else:
            log.error(" :  ❌ Event On Demand Filter is NOT present.")
        assert event_on_demand_filter_status, "Event On Demand Filter should be present."




