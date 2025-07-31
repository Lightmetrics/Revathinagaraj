import pytest
from ProjectB_Sanity.testCases.test_AdminPage import AdminPortal
from ProjectB_Sanity.testCases.test_MasterPortal import MasterPortal
from ProjectB_Sanity.testCases.test_FleetPortal import FleetPortal
from ProjectB_Sanity.utilities.BaseClass import BaseClass
from ProjectB_Sanity.testCases.test_F_1_HomePage import Fleet_HomePage_Test
from ProjectB_Sanity.testCases.test_F_2_SafetyEventsPage import Fleet_SafetyEventsPage_Test
from ProjectB_Sanity.testCases.test_F_3_TripsPage import Fleet_TripsPage_Test
from ProjectB_Sanity.testCases.test_F_4_LiveViewPage import Fleet_LiveViewPage_Test
from ProjectB_Sanity.testCases.test_F_5_CoachingPage import Fleet_CoachingPage_Test
from ProjectB_Sanity.testCases.test_F_6_VideoRequestsPage import Fleet_VideoRequestsPage_Test
from ProjectB_Sanity.testCases.test_F_7_DriversPage import Fleet_DriversPage_Test
from ProjectB_Sanity.testCases.test_F_8_ChallengesPage import Fleet_ChallengesPage_Test
from ProjectB_Sanity.testCases.test_F_9_ReportsPage import Fleet_ReportsPage_Test
from ProjectB_Sanity.testCases.test_F_10_AssetsPage import Fleet_AssetsPage_Test
from ProjectB_Sanity.testCases.test_F_11_UsersPage import Fleet_UsersPage_Test
from ProjectB_Sanity.testCases.test_F_12_ConfigurationsPage import Fleet_ConfigurationsPage_Test

customer_list = ["lmqatesting1", "lmpresales"]

@pytest.mark.usefixtures("setup")
class TestSuiteController(BaseClass):  # ✅ Inherit from BaseClass to use getLogger()

    @pytest.mark.order(1)
    @pytest.mark.parametrize("config", customer_list)
    def test_run_full_suite_for_customer(self, config):
        log = self.getLogger()
        print(f"🔆=====@ @ @ Running Full Suite for Customer: ("+ config +") @ @ @=====🔆")
        log.info(f"🔆=====@ @ @ Running Full Suite for Customer: {config} @ @ @=====🔆")

        try:
        # Step 1: Admin Portal
            print(f"=====@ @ @ 🚪 Running Admin Portal for 🚪: ("+ config +") @ @ @=====(1)")
            log.info(f"=====@ @ @ 🚪 Running Admin Portal for 🚪: {config} @ @ @=====(1)")

            admin = AdminPortal()
            admin.driver = self.driver
            admin.test_admin_login(config)
            admin.test_customer_selection_and_master_portal(config)

        # Step 2: Master Portal
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🧠 Running Master Portal for 🧠: ("+ config +") @ @ @=====(2)")
            log.info(f"=====@ @ @ 🧠 Running Master Portal for 🧠: {config} @ @ @=====(2)")

            master = MasterPortal()
            master.driver = self.driver
            master.test_validate_master_name()
            master.test_home_page_version()
            master.test_account_navigation_and_fleet_dashboard_launch()

        # Step 3: Fleet Portal
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🚛 Running Fleet Portal for 🚛: ("+ config +") @ @ @=====(3)")
            log.info(f"=====@ @ @ 🚛 Running Fleet Portal for 🚛: {config} @ @ @=====(3)")

            fleet = FleetPortal()
            fleet.driver = self.driver
            fleet.test_validate_fleet_name()
            fleet.test_home_page_version()

        # Step 4: Validate Fleet Home Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🏠 Validating Fleet Home Page for 🏠: ("+ config +") @ @ @=====(4)")
            log.info(f"=====@ @ @ 🏠 Validating Fleet Home Page for 🏠: {config} @ @ @=====(4)")

            home = Fleet_HomePage_Test()
            home.driver = self.driver
            home.test_validate_select_date_range()
            home.test_validate_trips_card_present()
            home.test_validate_distance_card()
            home.test_validate_event_per_100_miles_card()
            home.test_home_page_duration()
            home.test_home_page_recommended_events()
            home.test_home_page_top_drivers_card()
            home.test_home_page_coachable_drivers_card()
            home.test_home_page_event_summary_card()
            home.test_home_page_event_trend_card()

        # Step 5: Validate Safety Events Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🛡️ Validating Safety Events Page for 🛡️: ("+ config +") @ @ @=====(5)")
            log.info(f"=====@ @ @ 🛡️ Validating Safety Events Page for 🛡️: {config} @ @ @=====(5)")

            safety = Fleet_SafetyEventsPage_Test()
            safety.driver = self.driver
            safety.test_safety_events_page_btn()
            safety.test_safety_events_page_events_view()
            safety.test_safety_events_page_filters()

        # Step 6: Validate Trips Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🚗 Validating Trips Page for 🚗: ("+ config +") @ @ @=====(6)")
            log.info(f"=====@ @ @ 🚗 Validating Trips Page for 🚗: {config} @ @ @=====(6)")

            trips = Fleet_TripsPage_Test()
            trips.driver = self.driver
            trips.test_trips_page_btn()
            trips.test_trips_page_trips_tab()
            trips.test_trips_page_trip_filter_card()
            trips.test_trips_page_trips_list_table()
            trips.test_trips_page_bulk_edit()
            trips.test_trips_page_export_trips()
            trips.test_trips_page_active_drivers_tab()
            trips.test_trips_page_manage_tab()

        # Step 7: Validate Live View Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 📺 Validating Live View Page for 📺: ("+ config +") @ @ @=====(7)")
            log.info(f"=====@ @ @ 📺 Validating Live View Page for 📺: {config} @ @ @=====(7)")

            live_view = Fleet_LiveViewPage_Test()
            live_view.driver = self.driver
            live_view.test_live_view_page_btn()

        # Step 8: Validate Coaching Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🏆 Validating Coaching Page for 🏆: ("+ config +") @ @ @=====(8)")
            log.info(f"=====@ @ @ 🏆 Validating Coaching Page for 🏆: {config} @ @ @=====(8)")

            coaching = Fleet_CoachingPage_Test()
            coaching.driver = self.driver
            coaching.test_coaching_page_btn()
            coaching.test_coaching_page_coachable_drivers_table()
            coaching.test_coaching_page_completed_coaching_sessions_table()

        # Step 9: Validate Video Requests Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🎥 Validating Video Requests Page for 🎥: ("+ config +") @ @ @=====(9)")
            log.info(f"=====@ @ @ 🎥 Validating Video Requests Page for 🎥: {config} @ @ @=====(9)")

            video_requests = Fleet_VideoRequestsPage_Test()
            video_requests.driver = self.driver
            video_requests.test_video_requests_page()
            video_requests.test_video_requests_page_table()
            video_requests.test_video_requests_page_video_request()
            video_requests.test_video_requests_page_filter()
            video_requests.test_video_requests_page_panic_btn_filter()
            video_requests.test_video_requests_page_event_on_demand_filter()

        # Step 10: Validate Drivers Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 👥 Validating Drivers Page for 👥: ("+ config +") @ @ @=====(10)")
            log.info(f"=====@ @ @ 👥 Validating Drivers Page for 👥: {config} @ @ @=====(10)")

            drivers = Fleet_DriversPage_Test()
            drivers.driver = self.driver
            drivers.test_drivers_page()
            drivers.test_drivers_page_driver_list_table()
            drivers.test_drivers_page_search_driver_opt()
            drivers.test_drivers_page_batch_update_btn()
            drivers.test_drivers_page_export_button()
            drivers.test_drivers_page_add_images_option()  # Data related
            drivers.test_drivers_page_verify_driver_name()   # Create new data
            drivers.test_drivers_page_check_box_validation()
            drivers.test_drivers_page_installers_tab()

        # Step 11: Validate Challenges Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🏅 Validating Challenges Page for 🏅: ("+ config +") @ @ @=====(11)")
            log.info(f"=====@ @ @ 🏅 Validating Challenges Page for 🏅: {config} @ @ @=====(11)")

            challenges = Fleet_ChallengesPage_Test()
            challenges.driver = self.driver
            challenges.test_challenges_page()
            challenges.test_challenges_page_challenged_events_table()

        # Step 12: Validate Reports Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 📊 Validating Reports Page for 📊: ("+ config +") @ @ @=====(12)")
            log.info(f"=====@ @ @ 📊 Validating Reports Page for 📊: {config} @ @ @=====(12)")

            reports = Fleet_ReportsPage_Test()
            reports.driver = self.driver
            reports.test_reports_page()
            reports.test_reports_page_fleet_safety_view_report()
            # reports.test_reports_page_fleet_safety_create_schedule_report()  # Create new data
            # reports.test_reports_page_fleet_safety_edit_schedule_report_page()  # Edit newly created data
            reports.test_reports_page_Coaching_session_report()
            reports.test_reports_page_coaching_effectiveness_report()
            reports.test_reports_page_event_list_report()    # Async Report
            reports.test_reports_page_driver_privacy_mode_report()   # Async Report
            reports.test_reports_page_event_count_report()   # Async Report
            reports.test_reports_page_export_history_tab()
            reports.test_reports_page_scheduled_tab()

        # Step 13: Validate Assets Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 🚚 Validating Assets Page for 🚚: ("+ config +") @ @ @=====(13)")
            log.info(f"=====@ @ @ 🚚 Validating Assets Page for 🚚: {config} @ @ @=====(13)")

            assets = Fleet_AssetsPage_Test()
            assets.driver = self.driver
            assets.test_assets_page()
            assets.test_assets_page_overview_tab()
            assets.test_assets_page_manage_assets_tab()
            assets.test_assets_page_devices_tab()
            assets.test_assets_page_diagnostics_tab()

        # Step 14: Validate Users Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ 👤 Validating Users Page for 👤: ("+ config +") @ @ @=====(14)")
            log.info(f"=====@ @ @ 👤 Validating Users Page for 👤: {config} @ @ @=====(14)")

            users = Fleet_UsersPage_Test()
            users.driver = self.driver
            users.test_users_page()
            users.test_users_tab()
            # users.test_manage_users_table_data()    # Data related
            users.test_users_page_roles_tab()
            # users.test_manage_roles_table_data()    # Data related
            users.test_users_page_user_activity_log_tab()

        # Step 15: Validate Configurations Page
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")
            print(f"=====@ @ @ ⚙️ Validating Configurations Page for ⚙️: ("+ config +") @ @ @=====(15)")
            log.info(f"=====@ @ @ ⚙️ Validating Configurations Page for ⚙️: {config} @ @ @=====(15)")

            configurations = Fleet_ConfigurationsPage_Test()
            configurations.driver = self.driver
            configurations.test_configurations_page()
            configurations.test_configurations_page_basic_configurations_table()
            configurations.test_configurations_page_advanced_tab()
            configurations.test_configurations_page_coaching_tab()
            configurations.test_configurations_page_tagging_tab()
            # configurations.test_configurations_page_add_tag()  # Data related
            # configurations.test_configurations_page_add_attribute()  # Data related
            configurations.test_configurations_page_entities_page()

            print(f"🔆✅ ✅ =====@ Full suite passed for customer: ("+ config +") @===== ✅ ✅🔆")
            log.info(f"🔆✅ ✅ =====@ Full suite passed for customer: {config} @===== ✅ ✅🔆")
            print("\n" + "-" * 200 + "\n")
            log.info("\n" + "-" * 200 + "\n")


        except Exception as e:
            log.error(f"❌ Full suite failed for {config}: {e}")
            assert False, f"Test failed for {config}"
