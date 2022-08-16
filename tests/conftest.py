import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="Browser to run tests"
    )
    parser.addoption(
        "--headless", action="store_true", help="Browser in headless mode"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    options = webdriver.ChromeOptions()
    if headless:
        options.headless = True

    if browser_name == "chrome":
        _browser = webdriver.Chrome(executable_path="d:\mars\qa\otus\lesson_10\webdrivers\chromedriver",
                                    options=options)
    elif browser_name == "firefox":
        _browser = webdriver.Firefox(executable_path="d:\mars\qa\otus\lesson_10\webdrivers\geckodriver")
    elif browser_name == "opera":
        _browser = webdriver.Opera(executable_path="d:\mars\qa\otus\lesson_10\webdrivers\operadriver")
    elif browser_name == "yandex":
        _browser = webdriver.Chrome(executable_path="d:\mars\qa\otus\lesson_10\webdrivers\yandexdriver",
                                    options=options)
    elif browser_name == "edge":
        _browser = webdriver.Edge(executable_path="d:\mars\qa\otus\lesson_10\webdrivers\msedgedriver")
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported ")
    yield _browser
    _browser.close()
