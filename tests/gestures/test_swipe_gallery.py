from utils.gestures import swipe_up

def test_swipe_gallery(driver):
    driver.find_element_by_accessibility_id("Views").click()
    driver.find_element_by_accessibility_id("Gallery").click()
    swipe_up(driver)
    assert driver.find_element_by_accessibility_id("1. Photos").is_displayed()
