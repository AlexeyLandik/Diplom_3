import pytest
import allure
import requests
from selenium import webdriver
from data import Urls
from helpers import User


@allure.step('Запуск драйвера для Firefox и Chrome')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    driver.get(Urls.BASE_PAGE_URL)
    yield driver
    driver.quit()


@allure.step('Создание уникального пользователя и его регистрация с последующим удалением данных')
@pytest.fixture(scope='function')
def user():
    payload = User.create_random_login_password()
    response = requests.post(Urls.API_USER_REGISTRATION, data=payload)
    yield payload
    token = response.json()["accessToken"]
    requests.delete(Urls.API_USER_DELETE, data=payload, headers={"Authorization": token})
