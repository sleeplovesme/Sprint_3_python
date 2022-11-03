import helpers


class TestRegistration:
    def test_check_successful_registration(self, driver, random_login, random_password):
        # Проверь успешную регистрацию
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.click_to_register_link(driver)
        helpers.wait_for_registration_text(driver)
        inputs_type_text = helpers.list_of_inputs(driver)
        inputs_type_text[0].send_keys('test')
        inputs_type_text[1].send_keys(random_login)
        helpers.set_random_password(driver, random_password)
        helpers.click_to_register_button(driver)
        assert helpers.wait_for_login_text_return_text(driver) == 'Вход'

    def test_check_error_for_incorrect_password(self, driver):
        # Проверь ошибку для некорректного пароля
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.click_to_register_link(driver)
        helpers.wait_for_registration_text(driver)
        helpers.set_password_1(driver)
        helpers.click_to_register_button(driver)
        assert helpers.wait_for_incorrect_password_text_return_text(driver) == 'Некорректный пароль'
