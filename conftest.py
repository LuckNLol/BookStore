import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose language: ru/en/...(etc)")


@pytest.fixture(scope="function")  # function, class, module, session
def browser(request):
    user_language = request.config.getoption("language")

    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart Chrome browser for test..")
    browser = webdriver.Chrome()

    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()