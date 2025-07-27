from utils.visual import take_screenshot

def test_home_screenshot(driver):
    take_screenshot(driver, "apidemos_home.png")
