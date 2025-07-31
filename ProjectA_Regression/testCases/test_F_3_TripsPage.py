import pytest
from ProjectA_Regression.pageObjects.F_3_TripsPage import TripsPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_TripsPage_Test(BaseClass):


    def test_trips_page_btn(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Trips Button presence =====")
        trips_status = fleetportal.validate_trips_page(log)

        if trips_status:
            log.info(" :  ✅ Trips page button is present.")
        else:
            log.error(" :  ❌ Trips page button is NOT present.")
        assert trips_status, "Trips page button should be present."


    def test_trips_page_trips_tab(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Trips Tab presence =====")
        trips_tab_status = fleetportal.validate_trips_page_trips_tab(log)

        if trips_tab_status:
            log.info(" :  ✅ Trips Tab is present.")
        else:
            log.error(" :  ❌ Trips Tab is NOT present.")
        assert trips_tab_status, "Trips Tab should be present."


    def test_trips_page_trip_filter_card(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Trips Filter Card presence =====")
        trips_filter_status = fleetportal.validate_trips_page_trip_filter(log)

        if trips_filter_status:
            log.info(" :  ✅ Trips Filter Card is present.")
        else:
            log.error(" :  ❌ Trips Filter Card is NOT present.")
        assert trips_filter_status, "Trips Filter Card should be present."


    def test_trips_page_trips_list_table(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Trips List Table presence =====")
        trips_list_table_status = fleetportal.validate_trips_page_trips_list_table(log)

        if trips_list_table_status:
            log.info(" :  ✅ Trips List Table is present.")
        else:
            log.error(" :  ❌ Trips List Table is NOT present.")
        assert trips_list_table_status, "Trips List Table should be present."


    def test_trips_page_bulk_edit(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Bulk Edit presence =====")
        bulk_edit_status = fleetportal.validate_trips_page_bulk_edit(log)

        if bulk_edit_status:
            log.info(" :  ✅ Bulk Edit option is present.")
        else:
            log.error(" :  ❌ Bulk Edit option is NOT present.")
        assert bulk_edit_status, "Bulk Edit option should be present."


    def test_trips_page_export_trips(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Export Trips presence =====")
        export_trips_status = fleetportal.validate_trips_page_export_trips(log)

        if export_trips_status:
            log.info(" :  ✅ Export Trips option is present.")
        else:
            log.error(" :  ❌ Export Trips option is NOT present.")
        assert export_trips_status, "Export Trips option should be present."

    def test_trips_page_navigations(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Navigation buttons =====")
        navigation_status = fleetportal.validate_trips_page_navigations(log)

        if navigation_status:
            log.info(" :  ✅ Successfully validated navigation buttons.")
        else:
            log.error(" :  ❌ Failed to validated navigation buttons.")
        assert navigation_status, "Navigation buttons should be present."


    def test_trips_page_active_drivers_tab(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Active Drivers Tab presence =====")
        active_drivers_tab_status = fleetportal.validate_trips_page_active_drivers_tab(log)

        if active_drivers_tab_status:
            log.info(" :  ✅ Active Drivers Tab is present.")
        else:
            log.error(" :  ❌ Active Drivers Tab is NOT present.")
        assert active_drivers_tab_status, "Active Drivers Tab should be present."


    def test_trips_page_manage_tab(self):
        log = self.getLogger()
        fleetportal = TripsPage(self.driver)

        log.info("===== Validating Manage Tab presence =====")
        manage_tab_status = fleetportal.validate_trips_page_manage_tab(log)

        if manage_tab_status:
            log.info(" :  ✅ Manage Tab is present.")
        else:
            log.error(" :  ❌ Manage Tab is NOT present.")
        assert manage_tab_status, "Manage Tab should be present."
