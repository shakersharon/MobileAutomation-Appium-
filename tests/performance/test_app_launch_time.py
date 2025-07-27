def test_app_launch_time(driver):
    assert driver.launch_time < 10
