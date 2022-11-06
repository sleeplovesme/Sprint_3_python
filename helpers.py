from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def click_login_to_your_account_button(driver):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()


def wait_for_login_text(driver):
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))


def wait_for_login_text_return_text(driver):
    return WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]"))).text


def set_default_email(driver):
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("test-data@yandex.ru")


def set_default_password(driver):
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("password")


def set_random_password(driver, random_password):
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(random_password)


def set_password_1(driver):
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(1)


def click_to_login_button(driver):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()


def wait_for_register_order_text_return_text(driver):
    return WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))).text


def click_to_personal_account_button(driver):
    driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()


def click_to_register_button(driver):
    driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()


def click_to_register_link(driver):
    driver.find_element(By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]").click()


def wait_for_registration_text(driver):
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Регистрация')]")))


def click_to_login_link(driver):
    driver.find_element(By.XPATH, "//a[contains(text(), 'Войти')]").click()


def click_to_password_recovery_link(driver):
    driver.find_element(By.XPATH, "//a[contains(text(), 'Восстановить пароль')]").click()


def wait_for_password_recovery_text(driver):
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")))


def wait_for_logout_text(driver):
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(), 'Выход')]")))


def wait_for_logout_text_return_text(driver):
    return WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(), 'Выход')]"))).text


def wait_for_logout_text_and_click(driver):
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(), 'Выход')]"))).click()


def click_to_section_buns(driver):
    driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]").click()


def click_to_section_sauces(driver):
    driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]").click()


def click_to_section_fillings(driver):
    driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]").click()


def wait_for_buns_text_return_text(driver):
    return WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Булки')]"))).text


def wait_for_sauces_text_return_text(driver):
    return WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Соусы')]"))).text


def wait_for_fillings_text_return_text(driver):
    return WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[contains(text(), 'Начинки')]"))).text


def click_to_constructor_button(driver):
    driver.find_element(By.XPATH, "//p[contains(text(), 'Конструктор')]").click()


def click_to_logo(driver):
    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()


def list_of_inputs(driver):
    # Локатор инпутов на форме регистрации (Имя и Почта)
    return driver.find_elements(By.XPATH, "//input[@type='text']")


def wait_for_incorrect_password_text_return_text(driver):
    return WebDriverWait(driver, 5).until(ec.visibility_of_element_located(
        (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"))).text


def set_default_email_and_password_and_click_to_login_button(driver):
    set_default_email(driver)
    set_default_password(driver)
    click_to_login_button(driver)


def click_to_personal_account_button_and_wait_for_login_text(driver):
    click_to_personal_account_button(driver)
    wait_for_login_text(driver)


def click_to_login_link_and_wait_for_login_text(driver):
    click_to_login_link(driver)
    wait_for_login_text(driver)
