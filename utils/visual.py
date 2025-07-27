import os

def take_screenshot(driver, filename):
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(os.path.join("screenshots", filename))
