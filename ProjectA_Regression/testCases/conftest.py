from pathlib import Path
from datetime import datetime
import platform
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from slugify import slugify
from platform import python_version
# Global driver variable to be shared across classes
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests"
    )


# 🔧 SESSION-SCOPED FIXTURE: Create driver only ONCE
@pytest.fixture(scope="session")
def browser_driver(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--headless')  # Optional
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    elif browser_name == "IE":
        raise Exception("IE is deprecated and unsupported.")

    driver.maximize_window()
    driver.get("https://admin.lightmetrics.co/statistics")
    print(driver.title)

    yield driver

    # ✅ Close browser ONCE after all tests
    # driver.quit()


# 🔁 CLASS-SCOPED FIXTURE to attach driver to each test class
@pytest.fixture(scope="class", autouse=True)
def setup(request, browser_driver):
    request.cls.driver = browser_driver


# 📸 Screenshot capture utility
def _capture_screenshot(name):
    global driver
    if driver:
        driver.save_screenshot(name)


# 🧪 Hook: Attach screenshots to report on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        screenshot_dir = Path("Screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        file_name = f"{slugify(item.nodeid)}.png"
        destination_file = screenshot_dir / file_name
        _capture_screenshot(str(destination_file))
        extra.append(pytest_html.extras.png(str(destination_file)))

    report.extra = extra


# ✅ Custom title for the HTML report
def pytest_html_report_title(report):
    report.title = "LightMetrics Technologies Pvt. Ltd"


def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata.update({
            "Tester": "Sreenivasulu Akki",
            "Manager": "Divya Gajanana",
            "Team": "QA - Automation",
            "Testing Suite": "Regression Testing",
            "Portal": "Rebranding Portals",
            "Python Version": python_version()
        })



# ✅ Optional hook: Add custom content at the top and bottom of the report
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    from py.xml import html

    prefix.extend([
        html.h3(html.b("Tester: "), "Sreenivasulu Akki"),
        html.h3(html.b("Manager: "), "Divya Gajanana"),
        html.h3(html.b("Team: "), "QA - Automation"),
        html.h3(html.b("Testing Suite: "), "Regression Testing"),

        html.h3(html.b("TSP Name: "), "Lmpresales"),
        html.h3(html.b("Fleet: "), "Sreenivas Fleet"),

        html.hr()  # horizontal line
    ])

    summary.extend([html.h3(" ")])
    postfix.extend([html.h3(" ")])



