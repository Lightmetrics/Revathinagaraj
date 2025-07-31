import pytest
from ProjectA_Regression.pageObjects.F_10_AssetsPage import AssetsPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_AssetsPage_Test(BaseClass):

    def test_assets_page(self):
        log = self.getLogger()
        assets_page = AssetsPage(self.driver)

        log.info("===== Validating Assets Page presence =====")
        assets_page_status = assets_page.validate_assets_page(log)

        if assets_page_status:
            log.info(" :  ✅ Assets Page is present.")
        else:
            log.error(" :  ❌ Assets Page is NOT present.")
        assert assets_page_status, "Assets Page should be present."

    def test_assets_page_overview_tab(self):
        log = self.getLogger()
        assets_page = AssetsPage(self.driver)

        log.info("===== Validating Assets Page Overview Tab presence =====")
        overview_tab_status = assets_page.validate_assets_page_overview_tab(log)

        if overview_tab_status:
            log.info(" :  ✅ Overview Tab is present.")
        else:
            log.error(" :  ❌ Overview Tab is NOT present.")
        assert overview_tab_status, "Overview Tab should be present."


    def  test_assets_page_edit_assets_details_option(self):
         log = self.getLogger()
         assets_page = AssetsPage(self.driver)

         log.info("===== Validating Edit Assets Details Option =====")
         edit_assets_status = assets_page.validate_assets_page_asset_edit_data_asset_details_opt(log)

         if edit_assets_status:
             log.info(" :  ✅ Edit Assets Details Option is present.")
         else:
             log.error(" :  ❌ Edit Assets Details Option is NOT present.")
         assert edit_assets_status, "Edit Assets Details Option should be present."


    def test_assets_page_manage_devices_opt(self):
        log = self.getLogger()
        assets_page = AssetsPage(self.driver)

        log.info("===== Validating Manage Devices Option presence =====")
        manage_devices_status = assets_page.validate_assets_page_asset_manage_device_opt(log)

        if manage_devices_status:
            log.info(" :  ✅ Manage Devices Option is present.")
        else:
            log.error(" :  ❌ Manage Devices Option is NOT present.")
        assert manage_devices_status, "Manage Devices Option should be present."

    def test_assets_page_manage_assets_tab(self):
        log = self.getLogger()
        assets_page = AssetsPage(self.driver)

        log.info("===== Validating Manage Assets Tab presence =====")
        manage_assets_tab_status = assets_page.validate_assets_page_manage_assets_tab(log)

        if manage_assets_tab_status:
            log.info(" :  ✅ Manage Assets Tab is present.")
        else:
            log.error(" :  ❌ Manage Assets Tab is NOT present.")
        assert manage_assets_tab_status, "Manage Assets Tab should be present."


    def test_assets_page_devices_tab(self):
        log = self.getLogger()
        assets_page = AssetsPage(self.driver)

        log.info("===== Validating Devices Tab presence =====")
        devices_tab_status = assets_page.validate_assets_page_devices_tab(log)

        if devices_tab_status:
            log.info(" :  ✅ Devices Tab is present.")
        else:
            log.error(" :  ❌ Devices Tab is NOT present.")
        assert devices_tab_status, "Devices Tab should be present."


    def test_assets_page_diagnostics_tab(self):
        log = self.getLogger()
        assets_page = AssetsPage(self.driver)

        log.info("===== Validating Diagnostics Tab presence =====")
        diagnostics_tab_status = assets_page.validate_assets_page_diagnostics_tab(log)

        if diagnostics_tab_status:
            log.info(" :  ✅ Diagnostics Tab is present.")
        else:
            log.error(" :  ❌ Diagnostics Tab is NOT present.")
        assert diagnostics_tab_status, "Diagnostics Tab should be present."





