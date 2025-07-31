from pathlib import Path
from slugify import slugify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from platform import python_version
import pytest
import platform
from py.xml import html



# ============================== #
#        Pytest Options          #
# ============================== #

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox"
    )


# ============================== #
#        Browser Fixture         #
# ============================== #

@pytest.fixture(scope="function", autouse=True)
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = Options()
        # options.add_argument('--headless')  # Uncomment if needed
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()  # Maximize before opening the URL
    driver.get("https://admin.lightmetrics.co/statistics")
    request.cls.driver = driver

    yield driver

    driver.quit()


# ============================== #
#     HTML Reporting Hooks      #
# ============================== #

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot to HTML report on failure."""
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver') or getattr(item.cls, "driver", None)

        if driver:
            screenshot_dir = Path("Screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            file_name = slugify(item.nodeid) + ".png"
            file_path = screenshot_dir / file_name
            driver.save_screenshot(str(file_path))
            extra.append(pytest_html.extras.png(str(file_path)))

    report.extra = extra


# ============================== #
#       HTML Report Meta        #
# ============================== #

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
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    from py.xml import html

    prefix.extend([
        html.h3(html.b("Tester: "), "Sreenivasulu Akki"),
        html.h3(html.b("Manager: "), "Divya Gajanana"),
        html.h3(html.b("Team: "), "QA - Automation"),
        html.h3(html.b("Testing Suite: "), "Sanity Testing"),
        html.h3(html.b("Portal: "), "Rebranding Portals"),

        html.h3(html.b("TSP's List: "), "Charteredgreentech, Argus, Quantatec, Digicore, Safefleet, Rearviewsafety, Michelin"),

        html.hr()  # horizontal line
    ])

    summary.extend([html.h3(" ")])
    postfix.extend([html.h3(" ")])





