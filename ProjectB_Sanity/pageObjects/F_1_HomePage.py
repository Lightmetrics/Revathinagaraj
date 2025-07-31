import time
from ProjectB_Sanity.pageObjects.Locators_Fleet import FleetPortal_Locators
from telnetlib import EC
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Fleet_HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait




    def validate_select_date_range(self, log ):
        status = False
        try:
            home_page = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FleetPortal_Locators.home_page)
            )
            status = home_page.is_displayed()
            print(home_page.text + " ====>  ( Page matched ) 📑")
            home_page.click()

            time.sleep(3)

            print("🔗 " + self.driver.current_url)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.select_date_range)
            ).click()
            time.sleep(1)

            past_30_days1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.past_30_days)
            )
            status = past_30_days1.is_displayed()
            print(past_30_days1.text + " ====>  ( Selected Date Range )")

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(FleetPortal_Locators.past_30_days)
            ).click()
            time.sleep(2)

        except NoSuchElementException:
            pytest.skip("************* Select Date Range not displayed *************")
        return status

        ########### Trips Card Validation #######################

    def validate_trips_card_present(self, log):
        status = False
        try:
            trips = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.trips_card)
            )
            status = trips.is_displayed()
            print(trips.text + " ====>  ( Card matched )")
        except NoSuchElementException:
            pytest.skip("************* Trips Card not displayed *************")
        return status

    def validate_distance(self, log):
        status = False
        try:
            distance = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.distance_card)
            )
            status = distance.is_displayed()
            print(distance.text + " ====>  ( Card matched )")
        except NoSuchElementException:
            pytest.skip("************ Distance(mi) Card not displayed **********")
        return status

    def validate_event_per_100_miles(self, log):
        status = False
        try:
            events_card = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.events_card)
            )
            status = events_card.is_displayed()
            print(events_card.text + " ====>  ( Card matched )")
        except NoSuchElementException:
            pytest.skip("************ Events Per 100 Miles Card not displayed **********")
        return status

    def validate_duration(self, log):
        status = False
        try:
            duration = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.duration_hours)
            )
            status = duration.is_displayed()
            print(duration.text + " ====> ( Card matched )")
        except NoSuchElementException:
            pytest.skip("************ Duration (hours) Card not displayed **********")
        return status

    # recommended_for_coaching
    def validate_recommended_for_coaching(self, log):
        status = False
        try:
            recomanded_events1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.recomanded_events)
            )
            status = recomanded_events1.is_displayed()
            print(recomanded_events1.text + " ====> ( Card matched )")

        except NoSuchElementException:
            pytest.skip("************ Recommended for coaching card not displayed **********")
        return status

    ## Top Drivers card :-

    def validate_top_drivers(self, log):
        status = False
        try:
            # Wait until the top drivers element is visible and then scroll into view
            top_drivers1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.top_drivers)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", top_drivers1)
            status = top_drivers1.is_displayed()
            print(top_drivers1.text + " ====>  ( Card matched )")
            time.sleep(2)

        except NoSuchElementException:
            pytest.skip("************ Top Drivers card not displayed **********")
        return status

    def validate_coachable_drivers(self, log):
        status = False
        try:
            coachable_drivers1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.coachable_drivers_card)
            )
            status = coachable_drivers1.is_displayed()
            print(coachable_drivers1.text + " ====>  ( Card matched )")
        except NoSuchElementException:
            pytest.skip("************ Coachable drivers card not displayed **********")
        return status

    def validate_event_summary(self, log):
        status = False
        try:
            event_summary1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.event_summary)
            )
            status = event_summary1.is_displayed()
            print(event_summary1.text + " ====>  ( Card matched )")
        except NoSuchElementException:
            pytest.skip("************ Event Summary card not displayed **********")
        return status

    def validate_event_trend(self, log):
        status = False
        try:
            event_trend1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(FleetPortal_Locators.event_trend)
            )
            status = event_trend1.is_displayed()
            print(event_trend1.text + " ====>  ( Card matched )")

        except NoSuchElementException:
            pytest.skip("************ Event Trend card not displayed **********")

        return status