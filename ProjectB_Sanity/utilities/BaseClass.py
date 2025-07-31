import os
import inspect
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # Ensure Logs directory exists
        log_dir = os.path.join(os.getcwd(), "ProjectB_Sanity", "Logs")
        os.makedirs(log_dir, exist_ok=True)

        file_path = os.path.join(log_dir, "logfile.log")
        fileHandler = logging.FileHandler(file_path)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        # Avoid adding multiple handlers
        if not logger.hasHandlers():
            logger.addHandler(fileHandler)
            logger.setLevel(logging.DEBUG)

        return logger

    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
