import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Global explicit wait

    # Locators
    username = (By.XPATH, "//input[@placeholder='Enter username']")
    password = (By.XPATH, "//input[@placeholder='Enter password']")
    loginBtn = (By.XPATH, "//span[text()='Sign in']/parent::button")
    dropDown_btn = (By.XPATH, "//app-header//mat-toolbar[contains(@class,'header')]//button/following-sibling::div/button/span/mat-icon/following-sibling::mat-icon")
    customerName = (By.XPATH, "//input[@data-placeholder='Enter customer name']")
    autoComplete = (By.XPATH, "//div[contains(@id,'mat-autocomplete')]")
    customer_tsp_name = (By.XPATH, "(//div[contains(@id,'mat-autocomplete')]/mat-option/span)[1]")
    applyBtn = (By.XPATH, "//span[text()='Apply']/parent::button")
    mainMenu = (By.XPATH, "//button[@aria-haspopup='menu']")
    masterPortal = (By.XPATH, "//span[text()='Master Portal Login']/..")
    master_title = (By.XPATH, "//mat-toolbar[contains(@class,'header')]/div[2]/span")

    def loginToAdminPage(self, log):
        try:
            log.info(" : ******* 🌐/🔐 Attempting login to Admin Page")

            self.wait.until(EC.element_to_be_clickable(self.username)).send_keys("sreenivasulu.akki@lightmetrics.co")
            self.wait.until(EC.element_to_be_clickable(self.password)).send_keys("Srinivas@123")
            self.wait.until(EC.element_to_be_clickable(self.loginBtn)).click()
            time.sleep(7)

            self.wait.until(EC.title_contains("Admin Portal"))
            print("🔗 " + self.driver.current_url)
            log.info(" : ******* 🌐 ✅ Logged in successfully. Page Title: " + self.driver.title)
        except Exception as e:
            log.error(" : ******* 🌐/🚀 ❌ Login to Admin Page failed: " + str(e))
            raise

    def customer_tsp(self, log):
        try:
            # log.info("👤 Selecting customer TSP")

            drop_down1 = self.wait.until(EC.element_to_be_clickable(self.dropDown_btn))
            drop_down1.is_displayed()
            self.driver.refresh()
            time.sleep(5)
            self.wait.until(EC.element_to_be_clickable(self.dropDown_btn)).click()

            customer_input = self.wait.until(EC.element_to_be_clickable(self.customerName))
            time.sleep(1)
            customer_input.clear()
            customer_input.send_keys("lmqatesting1")
            time.sleep(1)

            tsp_name_elem = self.wait.until(EC.visibility_of_element_located(self.customer_tsp_name))
            print(f"✅ Found TSP: {tsp_name_elem.text}")
            log.info(f"✅ Found TSP: {tsp_name_elem.text}")

            self.wait.until(EC.element_to_be_clickable(self.autoComplete)).click()
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable(self.applyBtn)).click()
            time.sleep(2)

            log.info(" : ******* 🌐/🚀 Navigating to Master Portal")
            time.sleep(3)

            main_menu_elem = self.wait.until(EC.presence_of_element_located(self.mainMenu))
            self.driver.execute_script("arguments[0].scrollIntoView();", main_menu_elem)

            self.wait.until(EC.element_to_be_clickable(self.mainMenu)).click()
            time.sleep(3)
            self.wait.until(EC.element_to_be_clickable(self.masterPortal)).click()

            self.wait.until(lambda d: len(d.window_handles) > 1)
            current_handle = self.driver.current_window_handle
            new_window = [h for h in self.driver.window_handles if h != current_handle][0]
            self.driver.switch_to.window(new_window)

            self.wait.until(EC.title_contains("Master Portal"))
            log.info(" : ******* 🌐 ✅ Switched to Master Portal. Title: " + self.driver.title)
            log.info(" : ******* 🔗 Current URL: " + self.driver.current_url)
        except Exception as e:
            log.error(" : ******* 🌐/🚀 ❌ Failed to switch to Master Portal: " + str(e))
            raise
