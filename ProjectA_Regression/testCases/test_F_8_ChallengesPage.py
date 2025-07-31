import pytest
from ProjectA_Regression.pageObjects.F_8_ChallengesPage import ChallengesPage
from ProjectA_Regression.utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class Fleet_ChallengesPage_Test(BaseClass):

    def test_challenges_page(self):
        log = self.getLogger()
        challenges_page = ChallengesPage(self.driver)

        log.info("===== Validating Challenges Page presence =====")
        challenges_page_status = challenges_page.validate_challenges_page(log)

        if challenges_page_status:
            log.info(" :  ✅ Challenges Page is present.")
        else:
            log.error(" :  ❌ Challenges Page is NOT present.")
        assert challenges_page_status, "Challenges Page should be present."


    def test_challenges_page_challenged_events_table(self):
        log = self.getLogger()
        challenges_page = ChallengesPage(self.driver)

        log.info("===== Validating Challenged Events Table presence =====")
        is_challenged_events_table_status = challenges_page.validate_challenges_page_challenged_events_table(log)

        if is_challenged_events_table_status:
            log.info(" :  ✅ Challenged Events Table is present.")
        else:
            log.error(" :  ❌ Challenged Events Table is NOT present.")
        assert is_challenged_events_table_status, "Challenged Events Table should be present."