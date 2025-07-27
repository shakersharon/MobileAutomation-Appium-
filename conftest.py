import pytest
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time


def load_caps(device_name):
    with open("config/capabilities.json") as f:
        caps = json.load(f)
    return caps.get(device_name)


def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        default="android_apidemos",
        help="Device configuration name from capabilities.json"
    )


@pytest.fixture(scope="function")
def driver(request):
    caps_dict = load_caps(request.config.getoption("--device"))
    if caps_dict is None:
        pytest.skip("Unknown device specified")

    options = UiAutomator2Options().load_capabilities(caps_dict)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()
