from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_params(params, browser):
    res = browser.find_element_by_css_selector('.btn-add-to-basketaaa ')
    assert res, "страница товара на сайте не содержит кнопку добавления в корзину"



