import pytest
from ProjectA_Regression.pageObjects.F_12_ConfigurationsPage import ConfigurationsPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_ConfigurationsPage_Test(BaseClass):


    def test_configurations_page(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Fleet Configurations Page Test =====")
        configurations_page_status = configurations_page.validate_configurations_page(log)

        if configurations_page_status:
            log.info(" :  ✅ Configurations Page is present.")
        else:
            log.error(" :  ❌ Configurations Page is NOT present.")
        assert configurations_page_status, "Configurations Page should be present."


    def test_configurations_page_basic_configurations_table(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Basic Configurations Table Test =====")
        basic_configurations_table_status = configurations_page.validate_configurations_page_basic_configurations_table(log)

        if basic_configurations_table_status:
            log.info(" :  ✅ Basic Configurations Table is present.")
        else:
            log.error(" :  ❌ Basic Configurations Table is NOT present.")
        assert basic_configurations_table_status, "Basic Configurations Table should be present."


    def test_configurations_page_advanced_tab(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Advanced Tab Test =====")
        advanced_tab_status = configurations_page.validate_configurations_page_advanced_tab(log)

        if advanced_tab_status:
            log.info(" :  ✅ Advanced Tab is present.")
        else:
            log.error(" :  ❌ Advanced Tab is NOT present.")
        assert advanced_tab_status, "Advanced Tab should be present."


    def test_configurations_page_coaching_tab(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Coaching Tab Test =====")
        coaching_tab_status = configurations_page.validate_configurations_page_coaching_tab(log)

        if coaching_tab_status:
            log.info(" :  ✅ Coaching Tab is present.")
        else:
            log.error(" :  ❌ Coaching Tab is NOT present.")
        assert coaching_tab_status, "Coaching Tab should be present."


    def test_configurations_page_tagging_tab(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Tagging Tab Test =====")
        tagging_tab_status = configurations_page.validate_configurations_page_tagging_tab(log)

        if tagging_tab_status:
            log.info(" :  ✅ Tagging Tab is present.")
        else:
            log.error(" :  ❌ Tagging Tab is NOT present.")
        assert tagging_tab_status, "Tagging Tab should be present."

    def test_configurations_page_add_tag(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Add Tag Test =====")
        add_tag_status = configurations_page.validate_configurations_page_add_tag(log)

        if add_tag_status:
            log.info(" :  ✅ Add Tag is present.")
        else:
            log.error(" :  ❌ Add Tag is NOT present.")
        assert add_tag_status, "Add Tag should be present."

    def test_configurations_page_add_attribute(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Add Attribute Test =====")
        add_attribute_status = configurations_page.validate_configurations_page_add_attribute(log)

        if add_attribute_status:
            log.info(" :  ✅ Add Attribute is present.")
        else:
            log.error(" :  ❌ Add Attribute is NOT present.")
        assert add_attribute_status, "Add Attribute should be present."


    def test_configurations_page_entities_page(self):
        log = self.getLogger()
        configurations_page = ConfigurationsPage(self.driver)

        log.info("===== Validating Entities Page Test =====")
        entities_page_status = configurations_page.validate_configurations_page_entities_page(log)

        if entities_page_status:
            log.info(" :  ✅ Entities Page is present.")
        else:
            log.error(" :  ❌ Entities Page is NOT present.")
        assert entities_page_status, "Entities Page should be present."

