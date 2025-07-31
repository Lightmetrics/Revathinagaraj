import pytest
from ProjectB_Sanity.pageObjects.F_9_ReportsPage import ReportsPage
from ProjectB_Sanity.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_ReportsPage_Test(BaseClass):

    def test_reports_page(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Reports Page presence =====")
        reports_page_status = reports_page.validate_reports_page(log)

        if reports_page_status:
            log.info(" :  ✅ Reports Page is present.")
        else:
            log.error(" :  ❌ Reports Page is NOT present.")
        assert reports_page_status, "Reports Page should be present."

    def test_reports_page_fleet_safety_view_report(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Fleet Safety View Report presence =====")
        fleet_safety_report_status = reports_page.validate_reports_page_fleet_safety_view_report(log)

        if fleet_safety_report_status:
            log.info(" :  ✅ Fleet Safety View Report is present.")
        else:
            log.error(" :  ❌ Fleet Safety View Report is NOT present.")
        assert fleet_safety_report_status, "Fleet Safety View Report should be present."


    def test_reports_page_fleet_safety_create_schedule_report(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Fleet Safety Create Schedule Report presence =====")
        fleet_safety_schedule_report_status = reports_page.validate_reports_page_fleet_safety_create_schedule_report_page(log)

        if fleet_safety_schedule_report_status:
            log.info(" :  ✅ Create Fleet Safety Schedule Report is present.")
        else:
            log.error(" :  ❌ Create Fleet Safety Schedule Report is NOT present.")
        assert fleet_safety_schedule_report_status, "Create Fleet Safety Schedule Report should be present."


    def test_reports_page_fleet_safety_edit_schedule_report_page(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Fleet Safety Edit Schedule Report Page presence =====")
        fleet_safety_edit_schedule_report_status = reports_page.validate_reports_page_fleet_safety_edit_schedule_report_page(log)

        if fleet_safety_edit_schedule_report_status:
            log.info(" :  ✅ Edit Fleet Safety Schedule Report Page is present.")
        else:
            log.error(" :  ❌ Edit Fleet Safety Schedule Report Page is NOT present.")
        assert fleet_safety_edit_schedule_report_status, "Edit Fleet Safety Schedule Report Page should be present."


    def test_reports_page_Coaching_session_report(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Coaching Session Report presence =====")
        coaching_session_report_status = reports_page.validate_reports_page_Coaching_session_report(log)

        if coaching_session_report_status:
            log.info(" :  ✅ Coaching Session Report is present.")
        else:
            log.error(" :  ❌ Coaching Session Report is NOT present.")
        assert coaching_session_report_status, "Coaching Session Report should be present."

    def test_reports_page_coaching_effectiveness_report(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Coaching Effectiveness Report presence =====")
        coaching_effectiveness_report_status = reports_page.validate_reports_page_coaching_effectiveness_report(log)

        if coaching_effectiveness_report_status:
            log.info(" :  ✅ Coaching Effectiveness Report is present.")
        else:
            log.error(" :  ❌ Coaching Effectiveness Report is NOT present.")
        assert coaching_effectiveness_report_status, "Coaching Effectiveness Report should be present."


    def test_reports_page_event_list_report(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Event List Report presence =====")
        event_list_report_status = reports_page.validate_reports_page_event_list_report(log)

        if event_list_report_status:
            log.info(" :  ✅ Event List Report is present.")
        else:
            log.error(" :  ❌ Event List Report is NOT present.")
        assert event_list_report_status, "Event List Report should be present."

    def test_reports_page_driver_privacy_mode_report(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Driver Privacy Mode Report presence =====")
        driver_privacy_mode_report_status = reports_page.validate_reports_page_driver_privacy_mode_report(log)

        if driver_privacy_mode_report_status:
            log.info(" :  ✅ Driver Privacy Mode Report is present.")
        else:
            log.error(" :  ❌ Driver Privacy Mode Report is NOT present.")
        assert driver_privacy_mode_report_status, "Driver Privacy Mode Report should be present."

    def test_reports_page_event_count_report(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Event Count Report presence =====")
        event_count_report_status = reports_page.validate_reports_page_event_count_report(log)

        if event_count_report_status:
            log.info(" :  ✅ Event Count Report is present.")
        else:
            log.error(" :  ❌ Event Count Report is NOT present.")
        assert event_count_report_status, "Event Count Report should be present."


    def test_reports_page_export_history_tab(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Export History Tab presence =====")
        export_history_tab_status = reports_page.validate_reports_page_export_history_tab(log)

        if export_history_tab_status:
            log.info(" :  ✅ Export History Tab is present.")
        else:
            log.error(" :  ❌ Export History Tab is NOT present.")
        assert export_history_tab_status, "Export History Tab should be present."


    def test_reports_page_scheduled_tab(self):
        log = self.getLogger()
        reports_page = ReportsPage(self.driver)

        log.info("===== Validating Scheduled Tab presence =====")
        scheduled_tab_status = reports_page.validate_reports_page_scheduled_page(log)

        if scheduled_tab_status:
            log.info(" :  ✅ Scheduled Tab is present.")
        else:
            log.error(" :  ❌ Scheduled Tab is NOT present.")
        assert scheduled_tab_status, "Scheduled Tab should be present."

