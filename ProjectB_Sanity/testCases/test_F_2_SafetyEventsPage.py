import pytest
from ProjectB_Sanity.utilities.BaseClass import BaseClass
from ProjectB_Sanity.pageObjects.F_2_SafetyEventsPage import SafetyEventsPage



@pytest.mark.usefixtures("setup")
class Fleet_SafetyEventsPage_Test(BaseClass):


    def test_safety_events_page_btn(self):
        log = self.getLogger()
        fleetportal = SafetyEventsPage(self.driver)

        log.info("===== Validating Safety Events Button presence =====")
        safety_events_btn_status = fleetportal.validate_safety_events(log)

        if safety_events_btn_status:
            log.info(" :  ✅ Safety Events button is present.")
        else:
            log.error(" :  ❌ Safety Events button is NOT present.")
        assert safety_events_btn_status, "Safety Events button should be present."

    def test_safety_events_page_events_view(self):
        log = self.getLogger()
        fleetportal = SafetyEventsPage(self.driver)

        log.info("===== Validating Events View card presence =====")
        events_view_status = fleetportal.validate_safety_events_view(log)

        if events_view_status:
            log.info(" :  ✅ Events View card is present.")
        else:
            log.error(" :  ❌ Events View card is NOT present.")
        assert events_view_status, "Events View card should be present."

    def test_safety_events_page_filters(self):
        log = self.getLogger()
        fleetportal = SafetyEventsPage(self.driver)

        log.info("===== Validating Safety Events filters presence =====")
        filters_status = fleetportal.validate_safety_events_filters(log)

        if filters_status:
            log.info(" :  ✅ View Safety Events filters is present.")
        else:
            log.error(" :  ❌ View Safety Events filters is NOT present.")
        assert filters_status, "View Safety Events filters should be present."
