import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language")

    
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(25.0)
    if user_language == 'es':
        print("\n Run test on Espaniol")
    elif user_language != "es":
        print("\n Run test on English")
        user_language = 'en'
    yield browser
    print("\nquit browser..")
    browser.quit()
