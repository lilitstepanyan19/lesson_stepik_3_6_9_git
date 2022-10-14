from email.policy import default
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es', help='Choose a language: ')


    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    
@pytest.fixture(scope="function")
def browser(request):
    browser = None
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_language:
        browser = webdriver.Chrome(options=options)
    # else:
    #     raise pytest.UsageError("Enter your language")
    yield browser
    print("\nquit browser..")
    browser.quit()

from selenium.webdriver.chrome.options import Options
