import pytest
from ProjectB_Sanity.pageObjects.F_7_DriversPage import DriversPage
from ProjectB_Sanity.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_DriversPage_Test(BaseClass):


    def test_drivers_page(self):
        log = self.getLogger()
        drivers_page = DriversPage(self.driver)

        log.info("===== Validating Drivers Page presence =====")
        drivers_page_status = drivers_page.validate_Drivers_page(log)

        if drivers_page_status:
            log.info(" :  ✅ Drivers Page is present.")
        else:
            log.error(" :  ❌ Drivers Page is NOT present.")
        assert drivers_page_status, "Drivers Page should be present."

    def test_drivers_page_driver_list_table(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Validating Driver List Table presence =====")
        is_driver_list_table_status = fleetportal.validate_Drivers_page_driver_list_table(log)

        if is_driver_list_table_status:
            log.info(" :  ✅ Driver List Table is present.")
        else:
            log.error(" :  ❌ Driver List Table is NOT present.")
        assert is_driver_list_table_status, "Driver List Table should be present."

    def test_drivers_page_search_driver_opt(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Validating Search Driver Option presence =====")
        is_search_driver_status = fleetportal.validate_Drivers_page_driver_search_option(log)

        if is_search_driver_status:
            log.info(" :  ✅ Search Driver is present.")
        else:
            log.error(" :  ❌ Search Driver is NOT present.")
        assert is_search_driver_status, "Search Driver option should be present."

    def test_drivers_page_batch_update_btn(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Validating Batch Update Button presence =====")
        is_batch_update_btn_status = fleetportal.validate_Drivers_page_batch_update_btn(log)

        if is_batch_update_btn_status:
            log.info(" :  ✅ Batch Update Button is present.")
        else:
            log.error(" :  ❌ Batch Update Button is NOT present.")
        assert is_batch_update_btn_status, "Batch Update Button should be present."

    def test_drivers_page_export_button(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Validating Export Button presence =====")
        is_export_btn_status = fleetportal.validate_Drivers_page_export_btn(log)

        if is_export_btn_status:
            log.info(" :  ✅ Export Button is present.")
        else:
            log.error(" :  ❌ Export Button is NOT present.")
        assert is_export_btn_status, "Export Button should be present."

    def test_drivers_page_add_images_option(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Validating Add Images Option presence =====")
        is_add_images_option_status = fleetportal.validate_Drivers_page_add_images_btn(log)

        if is_add_images_option_status:
            log.info(" :  ✅ Add Images Option is present.")
        else:
            log.error(" :  ❌ Add Images Option is NOT present.")
        assert is_add_images_option_status, "Add Images Option should be present."

    def test_drivers_page_verify_driver_name(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Verifying Driver Name Availability =====")
        is_driver_name_status = fleetportal.validate_Drivers_page_check_driver_name_availability(log)

        if is_driver_name_status:
            log.info(" :  ✅ Driver name already exists.")
        else:
            log.error(" :  ❌ Driver name does NOT exist.")
        assert is_driver_name_status, "Driver name should be available in the list."

    def test_drivers_page_check_box_validation(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Validating Check Box Selection =====")
        is_check_box_status = fleetportal.validate_Drivers_page_check_boxes_validation(log)

        if is_check_box_status:
            log.info(" :  ✅ Check Box Selection is successful.")
        else:
            log.error(" :  ❌ Check Box Selection failed.")
        assert is_check_box_status, "Check Box should be selectable."

    def test_drivers_page_installers_tab(self):
        log = self.getLogger()
        fleetportal = DriversPage(self.driver)

        log.info("===== Validating Installers Tab presence =====")
        is_installers_tab_status = fleetportal.validate_Drivers_page_installers_tab(log)

        if is_installers_tab_status:
            log.info(" :  ✅ Installers Tab is present.")
        else:
            log.error(" :  ❌ Installers Tab is NOT present.")
        assert is_installers_tab_status, "Installers Tab should be present."