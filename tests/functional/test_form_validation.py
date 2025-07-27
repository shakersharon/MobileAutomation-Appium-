def test_empty_input(driver):
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Controls").click()
    driver.find_element_by_accessibility_id("2. Dark Theme").click()
    driver.find_element_by_id("io.appium.android.apis:id/add").click()
    log = driver.find_element_by_id("io.appium.android.apis:id/log").text
    assert log == ""
