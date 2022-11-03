import random

import pytest
from selenium import webdriver

default_email = "test-data@yandex.ru"
default_password = "password"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


# Не знаю подходит ли такая реализация генераторов для дополнительных заданий
@pytest.fixture
def random_login():
    return 'Dmitriy_Obernikhin_4_' + str(random.randint(100, 999)) + '@yandex.ru'


@pytest.fixture
def random_password():
    return random.randint(100000, 999999)
