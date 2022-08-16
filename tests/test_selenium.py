def test_positive_selenium(browser):
    browser.get(url="http://172.21.1.128:8081/")
    browser.save_screenshot("screenshot/test_positive_selenium.png")
    assert browser.title == "Your Store"


def test_negotive_selenium(browser):
    browser.get(url="http://172.21.1.128:8081/")
    browser.save_screenshot("screenshot/test_negotive_selenium.png")
    assert browser.title == "YourStore"
