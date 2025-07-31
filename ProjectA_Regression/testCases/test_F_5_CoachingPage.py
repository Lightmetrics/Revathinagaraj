import pytest
from ProjectA_Regression.pageObjects.F_5_CoachingPage import CoachingPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_CoachingPage_Test(BaseClass):

    def test_coaching_page_btn(self):
        log = self.getLogger()
        fleetportal = CoachingPage(self.driver)

        log.info("===== Validating Coaching Page Button presence =====")
        coaching_page_status = fleetportal.validate_coaching_page(log)

        if coaching_page_status:
            log.info(" :  ✅ Coaching page button is present.")
        else:
            log.error(" :  ❌ Coaching page button is NOT present.")
        assert coaching_page_status, "Coaching page button should be present."


    def test_coaching_page_coachable_drivers_table(self):
        log = self.getLogger()
        fleetportal = CoachingPage(self.driver)

        log.info("===== Validating Coachable Drivers Table presence =====")
        coachable_drivers_table_status = fleetportal.validate_coaching_page_coachable_drivers_table(log)

        if coachable_drivers_table_status:
            log.info(" :  ✅ Coachable Drivers Table is present.")
        else:
            log.error(" :  ❌ Coachable Drivers Table is NOT present.")
        assert coachable_drivers_table_status, "Coachable Drivers Table should be present."


    def test_coaching_page_completed_coaching_sessions_table(self):
        log = self.getLogger()
        fleetportal = CoachingPage(self.driver)

        log.info("===== Validating Completed Coaching Sessions Table presence =====")
        completed_coaching_sessions_table_status = fleetportal.validate_coaching_page_completed_coaching_sessions_table(log)

        if completed_coaching_sessions_table_status:
            log.info(" :  ✅ Completed Coaching Sessions Table is present.")
        else:
            log.error(" :  ❌ Completed Coaching Sessions Table is NOT present.")
        assert completed_coaching_sessions_table_status, "Completed Coaching Sessions Table should be present."

