def test_views_has_content_desc(driver):
    element = driver.find_element_by_accessibility_id("Views")
    assert element.get_attribute("contentDescription") == "Views"
