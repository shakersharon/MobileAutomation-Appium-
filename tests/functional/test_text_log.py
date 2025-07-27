def test_log_text(driver):
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Controls").click()
    driver.find_element_by_accessibility_id("2. Dark Theme").click()
    driver.find_element_by_id("io.appium.android.apis:id/edit").send_keys("Hello Appium")
    driver.find_element_by_id("io.appium.android.apis:id/add").click()
    log = driver.find_element_by_id("io.appium.android.apis:id/log").text
    assert "Hello Appium" in log
