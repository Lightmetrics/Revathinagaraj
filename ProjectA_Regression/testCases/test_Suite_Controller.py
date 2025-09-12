import pytest
from ProjectA_Regression.utilities.BaseClass import BaseClass
from ProjectA_Regression.testCases.test_AdminPage import AdminPortal
from ProjectA_Regression.testCases.test_MasterPortal import MasterPortal
from ProjectA_Regression.testCases.test_FleetPortal import FleetPortal
from ProjectA_Regression.testCases.test_F_1_HomePage import Fleet_HomePage_Test
from ProjectA_Regression.testCases.test_F_2_SafetyEventsPage import Fleet_SafetyEventsPage_Test
from ProjectA_Regression.testCases.test_F_3_TripsPage import Fleet_TripsPage_Test
from ProjectA_Regression.testCases.test_F_4_LiveViewPage import Fleet_LiveViewPage_Test
from ProjectA_Regression.testCases.test_F_5_CoachingPage import Fleet_CoachingPage_Test
from ProjectA_Regression.testCases.test_F_6_VideoRequestsPage import Fleet_VideoRequestsPage_Test
from ProjectA_Regression.testCases.test_F_7_DriversPage import Fleet_DriversPage_Test
from ProjectA_Regression.testCases.test_F_8_ChallengesPage import Fleet_ChallengesPage_Test
from ProjectA_Regression.testCases.test_F_9_ReportsPage import Fleet_ReportsPage_Test
from ProjectA_Regression.testCases.test_F_10_AssetsPage import Fleet_AssetsPage_Test
from ProjectA_Regression.testCases.test_F_11_UsersPage import Fleet_UsersPage_Test
from ProjectA_Regression.testCases.test_F_12_ConfigurationsPage import Fleet_ConfigurationsPage_Test



@pytest.mark.usefixtures("setup")
class TestSuiteController(BaseClass):

    @pytest.mark.order(1)
    def test_run_admin_portal(self):
        log = self.getLogger()
        print(f"🔆=====@ @ @ Running Full Suite for Customer @ @ @=====🔆")
        log.info(f"🔆=====@ @ @ Running Full Suite for Customer @ @ @=====🔆")
        log.info("===== Suite Controller: Admin Portal =====")

        admin = AdminPortal()
        admin.driver = self.driver
        admin.test_admin_login()
        admin.test_customer_selection_and_master_portal()

    @pytest.mark.order(2)
    def test_run_master_portal(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Master Portal =====")

        master = MasterPortal()
        master.driver = self.driver
        master.test_validate_master_name()
        master.test_home_page_version()
        master.test_account_navigation_and_fleet_dashboard_launch()

    @pytest.mark.order(3)
    def test_run_fleet_portal(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Portal =====")

        fleet = FleetPortal()
        fleet.driver = self.driver
        fleet.test_validate_fleet_name()
        fleet.test_home_page_version()


    @pytest.mark.order(5)
    def test_run_fleet_home_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Home Page =====")

        home = Fleet_HomePage_Test()
        home.driver = self.driver
        home.test_validate_select_date_range()
        home.test_validate_trips_card_present()
        home.test_validate_distance_card()
        home.test_validate_event_per_100_miles_card()
        home.test_home_page_duration()
        # home.test_home_page_recommended_events()   # Data related
        # home.test_home_page_validate_video()   # Data related
        # home.test_home_page_trip_details_btn()    # Data related
        home.test_home_page_top_drivers_card()
        home.test_home_page_coachable_drivers_card()
        home.test_home_page_event_summary_card()
        home.test_home_page_event_trend_card()

    @pytest.mark.order(4)
    def test_run_safety_events_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Safety Events Page =====")

        safety = Fleet_SafetyEventsPage_Test()
        safety.driver = self.driver
        safety.test_safety_events_page_btn()
        safety.test_safety_events_page_events_view()
        safety.test_safety_events_page_filters()
        # safety.test_safety_events_navigation_to_tripdetails()  #Data related

    @pytest.mark.order(6)
    def test_run_fleet_trips_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Trips Page =====")

        trips = Fleet_TripsPage_Test()
        trips.driver = self.driver
        trips.test_trips_page_btn()
        trips.test_trips_page_trips_tab()
        trips.test_trips_page_trip_filter_card()
        trips.test_trips_page_trips_list_table()
        trips.test_trips_page_bulk_edit()
        trips.test_trips_page_export_trips()
        # trips.test_trips_page_navigations()    #Data related
        trips.test_trips_page_active_drivers_tab()
        trips.test_trips_page_manage_tab()

    @pytest.mark.order(7)
    def test_run_fleet_live_view_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Live View Page =====")

        live_view = Fleet_LiveViewPage_Test()
        live_view.driver = self.driver
        live_view.test_live_view_page_btn()
        # live_view.test_live_view_page_asset_table()  # Data related


    @pytest.mark.order(8)
    def test_run_coaching_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Coaching Page =====")

        coaching = Fleet_CoachingPage_Test()
        coaching.driver = self.driver
        coaching.test_coaching_page_btn()
        coaching.test_coaching_page_coachable_drivers_table()
        coaching.test_coaching_page_completed_coaching_sessions_table()

    @pytest.mark.order(9)
    def test_run_video_requests_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Video Requests Page =====")

        video_requests = Fleet_VideoRequestsPage_Test()
        video_requests.driver = self.driver
        video_requests.test_video_requests_page()
        video_requests.test_video_requests_page_table()
        video_requests.test_video_requests_page_video_request()
        video_requests.test_video_requests_page_filter()
        video_requests.test_video_requests_page_panic_btn_filter()
        video_requests.test_video_requests_page_event_on_demand_filter()


    @pytest.mark.order(10)
    def test_run_drivers_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Drivers Page =====")

        drivers = Fleet_DriversPage_Test()
        drivers.driver = self.driver
        drivers.test_drivers_page()
        drivers.test_drivers_page_driver_list_table()
        drivers.test_drivers_page_search_driver_opt()
        drivers.test_drivers_page_batch_update_btn()
        drivers.test_drivers_page_export_button()
        # drivers.test_drivers_page_export_driverlist_csv()   # Async Report
        # drivers.test_drivers_page_export_bulk_qrcode()   # Async Report
        # drivers.test_drivers_page_download_qrcode()  # Data related &  Async Report
        # drivers.test_drivers_page_add_images_option()  # Data related
        # drivers.test_drivers_page_verify_driver_name()   # Create New data
        # drivers.test_drivers_page_check_box_validation()  # Data related  & Async Report
        drivers.test_drivers_page_installers_tab()


    @pytest.mark.order(11)
    def test_run_challenges_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Challenges Page =====")

        challenges = Fleet_ChallengesPage_Test()
        challenges.driver = self.driver
        challenges.test_challenges_page()
        challenges.test_challenges_page_challenged_events_table()


    @pytest.mark.order(12)
    def test_run_reports_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Reports Page =====")

        reports = Fleet_ReportsPage_Test()
        reports.driver = self.driver
        reports.test_reports_page()
        reports.test_reports_page_Coaching_session_report()
        reports.test_reports_page_coaching_effectiveness_report()
        # reports.test_reports_page_driver_privacy_mode_report()  # Async Report
        reports.test_reports_page_fleet_safety_view_report()
        # reports.test_reports_page_fleet_safety_create_schedule_report()    # Async Report
        # reports.test_reports_page_fleet_safety_edit_schedule_report_page()    # Async Report
        # reports.test_reports_page_video_request_list_report()   # Async Report
        # reports.test_reports_page_event_count_report()   # Async Report
        # reports.test_reports_page_event_list_report()   # Async Report
        # reports.test_reports_page_highg_event_list_report()    # Async Report
        # reports.test_reports_page_panic_button_list_report()   # Async Report
        reports.test_reports_page_export_history_tab()
        reports.test_reports_page_scheduled_tab()




    @pytest.mark.order(13)
    def test_run_assets_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Assets Page =====")

        assets = Fleet_AssetsPage_Test()
        assets.driver = self.driver
        assets.test_assets_page()
        assets.test_assets_page_overview_tab()
        # assets.test_assets_page_edit_assets_details_option()   # Data related
        # assets.test_assets_page_manage_devices_opt()   # Data related
        assets.test_assets_page_manage_assets_tab()
        assets.test_assets_page_devices_tab()
        assets.test_assets_page_diagnostics_tab()


    @pytest.mark.order(14)
    def test_run_users_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Users Page =====")

        users = Fleet_UsersPage_Test()
        users.driver = self.driver
        users.test_users_page()
        users.test_users_tab()
        # users.test_manage_users_table_data()    # Data related
        users.test_users_page_roles_tab()
        # users.test_manage_roles_table_data()    # Data related
        users.test_users_page_user_activity_log_tab()


    @pytest.mark.order(15)
    def test_run_configurations_page(self):
        log = self.getLogger()
        log.info("===== Suite Controller: Fleet Configurations Page =====")

        configurations = Fleet_ConfigurationsPage_Test()
        configurations.driver = self.driver
        configurations.test_configurations_page()
        configurations.test_configurations_page_basic_configurations_table()
        configurations.test_configurations_page_advanced_tab()
        configurations.test_configurations_page_coaching_tab()
        configurations.test_configurations_page_tagging_tab()
        # configurations.test_configurations_page_add_tag()    # Data related
        # configurations.test_configurations_page_add_attribute()    # Data related
        # configurations.test_configurations_page_entities_page()

        print(f"🔆✅ ✅ =====@ Full suite passed for customer @===== ✅ ✅🔆")
        log.info(f"🔆✅ ✅ =====@ Full suite passed for customer @===== ✅ ✅🔆")











