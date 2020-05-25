from selenium import webdriver
import pytest
import time


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("--language", action="store", help="input useranme")


@pytest.fixture
def params(request, browser):
    language = request.config.getoption('--language')
    url = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(30)


