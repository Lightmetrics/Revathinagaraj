import pytest
from ProjectB_Sanity.utilities.BaseClass import BaseClass
from ProjectB_Sanity.pageObjects.F_1_HomePage import Fleet_HomePage



@pytest.mark.usefixtures("setup")
class Fleet_HomePage_Test(BaseClass):


    def test_validate_select_date_range(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Select Date Range =====")
        try:
            assert fleet.validate_select_date_range(log), "Select Date Range is not working"
            log.info(" :  ✅ Select Date Range is functioning correctly.")
        except Exception as e:
            log.error(f" :  ❌ Select Date Range validation failed: {e}")
            raise

    def test_validate_trips_card_present(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Trips Card =====")
        try:
            assert fleet.validate_trips_card_present(log), "Trips card not displayed"
            log.info(" :  ✅ Trips card is present and displayed.")
        except Exception as e:
            log.error(f" :  ❌ Trips card validation failed: {e}")
            raise

    def test_validate_distance_card(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Distance Card =====")
        try:
            assert fleet.validate_distance(log), "Distance card not displayed"
            log.info(" :  ✅ Distance card is displayed correctly.")
        except Exception as e:
            log.error(f" :  ❌ Distance card validation failed: {e}")
            raise

    def test_validate_event_per_100_miles_card(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Events Per 100 Miles Card =====")
        try:
            assert fleet.validate_event_per_100_miles(log), "Events card not displayed"
            log.info(" :  ✅ Events Per 100 Miles card is visible and validated.")
        except Exception as e:
            log.error(f" :  ❌ Events Per 100 Miles card validation failed: {e}")
            raise

    def test_home_page_duration(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Duration (Hours) Card =====")
        try:
            assert fleet.validate_duration(log), "Duration (Hours) card not displayed"
            log.info(" :  ✅ Duration (Hours) card is displayed correctly.")
        except Exception as e:
            log.error(f" :  ❌ Duration card validation failed: {e}")
            raise

    def test_home_page_recommended_events(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Recommended for Coaching Card =====")
        try:
            assert fleet.validate_recommended_for_coaching(log), "Recommended for Coaching card not displayed"
            log.info(" :  ✅ Recommended for Coaching card is displayed.")
        except Exception as e:
            log.error(f" :  ❌ Recommended for Coaching card validation failed: {e}")
            raise

    def test_home_page_top_drivers_card(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Top Drivers Card =====")
        try:
            assert fleet.validate_top_drivers(log), "Top Drivers card not displayed"
            log.info(" :  ✅ Top Drivers card is visible and validated.")
        except Exception as e:
            log.error(f" :  ❌ Top Drivers card validation failed: {e}")
            raise

    def test_home_page_coachable_drivers_card(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Coachable Drivers Card =====")
        try:
            assert fleet.validate_coachable_drivers(log), "Coachable Drivers card not displayed"
            log.info(" :  ✅ Coachable Drivers card is present and validated.")
        except Exception as e:
            log.error(f" :  ❌ Coachable Drivers card validation failed: {e}")
            raise

    def test_home_page_event_summary_card(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Event Summary Card =====")
        try:
            assert fleet.validate_event_summary(log), "Event Summary card not displayed"
            log.info(" :  ✅ Event Summary card is displayed and validated.")
        except Exception as e:
            log.error(f" :  ❌ Event Summary card validation failed: {e}")
            raise

    def test_home_page_event_trend_card(self):
        log = self.getLogger()
        fleet = Fleet_HomePage(self.driver)

        log.info(" : ===== Validating Event Trend Card =====")
        try:
            assert fleet.validate_event_trend(log), "Event Trend card not displayed"
            log.info(" :  ✅ Event Trend card is present and validated.")
        except Exception as e:
            log.error(f" :  ❌ Event Trend card validation failed: {e}")
            raise
