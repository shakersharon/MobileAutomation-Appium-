import pytest
from utils.data_reader import read_credentials

@pytest.mark.parametrize("username,password", read_credentials("config/login_data.json"))
def test_login_input(driver, username, password):
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Controls").click()
    driver.find_element_by_accessibility_id("2. Dark Theme").click()
    driver.find_element_by_id("io.appium.android.apis:id/edit").send_keys(username)
    driver.find_element_by_id("io.appium.android.apis:id/add").click()
    log = driver.find_element_by_id("io.appium.android.apis:id/log").text
    assert username in log
