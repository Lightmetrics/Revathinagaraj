import time
from selenium.webdriver.common.by import By

from ProjectB_Sanity.pageObjects.Locators_Fleet import FleetPortal_Locators
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ReportsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait


    def validate_reports_page(self, log):
        status = False
        try:
            reports_page1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.reports_page)
            )
            reports_page1.click()
            time.sleep(3)
            print("🔗 " + self.driver.current_url)
            status = reports_page1.is_displayed()
            print(reports_page1.text + " ====> ( Page matched ) 📑")

            overview_tab1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.overview_tab)
            )
            status = overview_tab1.is_displayed()
            print(overview_tab1.text + " ====> ( Tab matched ) ✅")

        except NoSuchElementException:
            pytest.skip("************ Reports page not displayed **********")
        return status

# Coaching Reports:-
# Coaching Session Report:-
    def validate_reports_page_Coaching_session_report(self, log):
        status = False
        try:
            coaching_session1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.coaching_session_report)
            )
            status = coaching_session1.is_displayed()
            print(coaching_session1.text + " ====> ( Card matched )")

            view_report2 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.view_report_btn2)
            )
            status = view_report2.is_displayed()
            print(view_report2.text + " ====> ( Button matched )")
            view_report2.click()
            time.sleep(2)

            select_driver_filt1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_driver_filt)
            )

            back_btn1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = back_btn1.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Coaching Session Report' Page, from the 'Coaching Session' card.")
            time.sleep(2)
            back_btn1.click()

            schedule_opt2 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_btn2)
            )
            status = schedule_opt2.is_displayed()
            print(schedule_opt2.text + " ====> ( Button matched )")
            schedule_opt2.click()
            time.sleep(2)

            back_btn1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = back_btn1.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Coaching Session' card.")
            back_btn1.click()
            time.sleep(2)

        except NoSuchElementException:
            pytest.skip("************ Coaching Session Report card not displayed **********")
        return status


    def validate_reports_page_coaching_effectiveness_report(self, log):
        status = False
        try:
            coaching_effectiveness1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.coaching_effectiveness_report)
            )
            status = coaching_effectiveness1.is_displayed()
            print(coaching_effectiveness1.text + " ====> ( Card matched )")

            view_report3 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.view_report_btn3)
            )
            status = view_report3.is_displayed()
            print(view_report3.text + " ====> ( Button matched )")
            view_report3.click()
            time.sleep(2)

            back_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn))

            status = back_btn.is_displayed()
            print(
                "📄/🚀 ✅ Successfully launched 'Coaching Effectiveness Report' Page, from the 'Coaching Effectiveness' card.")
            back_btn.click()
            time.sleep(2)

        except NoSuchElementException:
            pytest.skip("************ Coaching Effectiveness Report (Driver) card not displayed **********")
        return status

# Driver Reports:-
# Driver Privacy Mode Report:-

    def validate_reports_page_driver_privacy_mode_report(self, log):
        status = False
        try:
            driver_privacy1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.driver_privacy_mode_report)
            )
            status = driver_privacy1.is_displayed()
            print(driver_privacy1.text + " ====> ( Card matched )")

            download_report_priv1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.download_report_repo2)
            )
            status = download_report_priv1.is_displayed()
            print(download_report_priv1.text + " ====> ( Button matched )")
            download_report_priv1.click()
            time.sleep(2)

            print(
                " 🪟/🚀 ✅ Successfully launched 'Driver Privacy Mode Report' Pop-Up window, from 'Driver Privacy ' card.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.close_popup)
            ).click()
            time.sleep(2)

            # Schedule Driver Privacy Mode Report:
            schedule_driver_btn = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_btn5)
            )
            status = schedule_driver_btn.is_displayed()
            print(schedule_driver_btn.text + " ====> ( Button matched )")
            schedule_driver_btn.click()
            time.sleep(2)

            privacy_mode1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = privacy_mode1.is_displayed()
            print(
                "📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Driver Privacy Mode Report' card.")
            privacy_mode1.click()
            time.sleep(3)


        except NoSuchElementException:
            pytest.skip("************ Driver Privacy Mode Report card not displayed **********")
        return status

# Fleet Reports:-
# Fleet Safety Report:-

    def validate_reports_page_fleet_safety_view_report(self, log):
        status = False
        try:
            fleet_safety_report1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.fleet_safety_report)
            )
            status = fleet_safety_report1.is_displayed()
            print(fleet_safety_report1.text + " ====> ( Card matched )")

            view_report_btn1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.view_report_btn1)
            )
            status = view_report_btn1.is_displayed()
            print(view_report_btn1.text + " ====> ( Button matched )")
            view_report_btn1.click()
            time.sleep(2)

            download_report_btn1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.download_report_btn)
            )
            status = download_report_btn1.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Fleet Safety Report' Page, from the 'Fleet Safety' card.")
            print(download_report_btn1.text + " ====> ( Button matched )")

            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            ).click()
            time.sleep(2)


        except NoSuchElementException:
            pytest.skip("************ Fleet Safety View Report button not displayed **********")
        return status


# Added Fleet Safety Schedule Report:-

    def validate_reports_page_fleet_safety_create_schedule_report_page(self, log):
        status = False
        try:
            schedule_report1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_btn1)
            )
            status = schedule_report1.is_displayed()
            print(schedule_report1.text + " ====> ( Button matched )")
            schedule_report1.click()
            time.sleep(5)

            schedule_name_opt = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_name)
            )
            status = schedule_name_opt.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Fleet Safety' card.")
            schedule_name_opt.click()
            time.sleep(2)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            ).click()
            time.sleep(2)

        except NoSuchElementException:
            pytest.skip("************ Create Fleet Safety Report page not displayed **********")
        return status


# Video Request List Report:-
    def validate_reports_page_video_request_list_report(self, log):
        status = False
        try:
            video_request_list1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.video_request_report)
            )
            status = video_request_list1.is_displayed()
            print(video_request_list1.text + " ====> ( Card matched )")

            download_report_vid1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.download_video_request_report_repo)
            )
            status = download_report_vid1.is_displayed()
            print(download_report_vid1.text + " ====> ( Button matched )")
            download_report_vid1.click()
            time.sleep(2)

            print(
                " 🪟/🚀 ✅ Successfully launched 'Video Request List Report' Pop-Up window, from 'Video Request List' card.")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.close_popup)
            ).click()
            time.sleep(2)


# Schedule Video Request List Report:
            schedule_video_request_btn1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_video_request_btn)
            )
            status = schedule_video_request_btn1.is_displayed()
            print(schedule_video_request_btn1.text + " ====> ( Button matched )")
            schedule_video_request_btn1.click()
            time.sleep(2)
            video_request_back1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = video_request_back1.is_displayed()
            print(
                "📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Video Request List Report' card.")
            video_request_back1.click()
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Video Request List Report card not displayed **********")
        return status


# Safety Event Reports:-
# Event Count Report:-
    def validate_reports_page_event_count_report(self, log):
        status = False
        try:
            event_count1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.event_count_report)
            )
            status = event_count1.is_displayed()
            print(event_count1.text + " ====> ( Card matched )")

            download_report_evnt1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.download_report_repo3)
            )
            status = download_report_evnt1.is_displayed()
            print(download_report_evnt1.text + " ====> ( Button matched )")
            download_report_evnt1.click()
            time.sleep(2)
            print(" 🪟/🚀 ✅ Successfully launched 'Event Count Report' Pop-Up window, from 'Event Count' card.")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.close_popup)
            ).click()
            time.sleep(2)

            # schedule event count report:
            schedule_eventcount_btn = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_btn6)
            )
            status = schedule_eventcount_btn.is_displayed()
            print(schedule_eventcount_btn.text + " ====> ( Button matched )")
            schedule_eventcount_btn.click()
            time.sleep(2)

            event_count_sch1 = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = event_count_sch1.is_displayed()
            print(
                "📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Event Count Report' card.")
            event_count_sch1.click()
            time.sleep(3)


        except NoSuchElementException:
            pytest.skip("************ Event Count Report card not displayed **********")
        return status


    def validate_reports_page_event_list_report(self, log):
        status = False
        try:
            event_list1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.event_list_report)
            )
            status = event_list1.is_displayed()
            print(event_list1.text + " ====> ( Card matched )")

            download_report_eve1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.download_report_repo1)
            )
            status = download_report_eve1.is_displayed()
            print(download_report_eve1.text + " ====> ( Button matched )")
            download_report_eve1.click()
            time.sleep(2)

            print(" 🪟/🚀 ✅ Successfully launched 'Event List Report' Pop-Up window, from 'Event List' card.")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.close_popup)
            ).click()
            time.sleep(2)


# Schedule Event List Report:
            schedule_event_list_btn1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_btn4)
            )
            status = schedule_event_list_btn1.is_displayed()
            print(schedule_event_list_btn1.text + " ====> ( Button matched )")
            schedule_event_list_btn1.click()
            time.sleep(2)

            event_list_back1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = event_list_back1.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Event List Report' card.")
            event_list_back1.click()
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ Event List Report card not displayed **********")
        return status

    def validate_reports_page_highg_event_list_report(self, log):
        status = False
        try:
            highg_event_list1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.hightg_event_report)
            )
            status = highg_event_list1.is_displayed()
            print(highg_event_list1.text + " ====> ( Card matched )")

            download_report_highg1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.download_highg_report_repo)
            )
            status = download_report_highg1.is_displayed()
            print(download_report_highg1.text + " ====> ( Button matched )")
            download_report_highg1.click()
            time.sleep(2)

            print(" 🪟/🚀 ✅ Successfully launched 'High G Event List Report' Pop-Up window, from 'High G Event List' card.")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.close_popup)
            ).click()
            time.sleep(2)

# Schedule High G Event List Report:
            schedule_highg_event_list_btn1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_highg_btn)
            )
            status = schedule_highg_event_list_btn1.is_displayed()
            print(schedule_highg_event_list_btn1.text + " ====> ( Button matched )")
            schedule_highg_event_list_btn1.click()
            time.sleep(2)
            highg_event_list_back1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = highg_event_list_back1.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'High G Event List Report' card.")
            highg_event_list_back1.click()
            time.sleep(3)

        except NoSuchElementException:
            pytest.skip("************ High G Event List Report card not displayed **********")
        return status


    def validate_reports_page_panic_button_list_report(self, log):
        status = False
        try:
            panic_button_list1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.panic_button_list_report)
            )
            status = panic_button_list1.is_displayed()
            print(panic_button_list1.text + " ====> ( Card matched )")

            download_report_panic1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.download_panic_report_repo)
            )
            status = download_report_panic1.is_displayed()
            print(download_report_panic1.text + " ====> ( Button matched )")
            download_report_panic1.click()
            time.sleep(2)

            print(" 🪟/🚀 ✅ Successfully launched 'Panic Button List Report' Pop-Up window, from 'Panic Button List' card.")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.close_popup)
            ).click()
            time.sleep(2)

# Schedule Panic Button List Report:
            schedule_panic_button_list_btn1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.schedule_panic_btn)
            )
            status = schedule_panic_button_list_btn1.is_displayed()
            print(schedule_panic_button_list_btn1.text + " ====> ( Button matched )")
            schedule_panic_button_list_btn1.click()
            time.sleep(2)
            panic_button_list_back1 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.back_arrow_btn)
            )
            status = panic_button_list_back1.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Panic Button List Report' card.")
            panic_button_list_back1.click()
            time.sleep(3)
        except NoSuchElementException:
            pytest.skip("************ Panic Button List Report card not displayed **********")
        return status



    def validate_reports_page_export_history_tab(self, log):
        status = False
        try:

            export_history_tab1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.export_history)
            )
            status = export_history_tab1.is_displayed()
            print(export_history_tab1.text + " ====> ( Tab matched ) ✅")
            export_history_tab1.click()
            time.sleep(2)

            export_history_table1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.export_history_table)
            )
            status = export_history_table1.is_displayed()
            print(export_history_table1.text + " ====> ( Table matched )")

            select_request1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_request_type)
            )
            status = select_request1.is_displayed()
            print(select_request1.text + " ====> ( Filter matched )")

            select_duration1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.select_duration_opt)
            )
            status = select_duration1.is_displayed()
            print(select_duration1.text + " ====> ( Filter matched )")


        except NoSuchElementException:
            pytest.skip("************ Export History tab not displayed **********")
        return status


    def validate_reports_page_scheduled_page(self, log):
        status = False
        try:

            schedule_tab1 = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(FleetPortal_Locators.scheduled_tab)
            )
            status = schedule_tab1.is_displayed()
            print(schedule_tab1.text + " ====> ( Tab matched ) ✅")
            schedule_tab1.click()
            time.sleep(2)

            create_schedule_btn1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.create_schedule_btn)
            )
            status = create_schedule_btn1.is_displayed()
            print(create_schedule_btn1.text + " ====> ( Button matched )")
            create_schedule_btn1.click()

            back_btn1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.back_arrow_btn)
            )
            status = back_btn1.is_displayed()
            print("📄/🚀 ✅ Successfully launched 'Create Schedule Reports' Page, from the 'Scheduled' tab.")
            back_btn1.click()
            time.sleep(2)


        except NoSuchElementException:
            pytest.skip("************ Scheduled tab not displayed **********")
        return status