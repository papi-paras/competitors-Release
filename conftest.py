import time
import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--player_name", action="store", default="memu"
    )

@pytest.fixture(scope="class")
def setup(request):

    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    browsername = request.config.getoption("--browser_name")
    playername = request.config.getoption("--player_name")
    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    if playername == "memu":
        driver.get('https://www.memuplay.com/blog/en/category/release-notes')
    elif playername == "ldplayer":
        driver.get('https://www.ldplayer.net/other/version-history-and-release-notes.html')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


