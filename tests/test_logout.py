import helpers


class TestLogout:
    def test_logout(self, driver):
        # Проверь выход по кнопке «Выйти» в личном кабинете
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.set_default_email_and_password_and_click_to_login_button(driver)
        helpers.wait_for_register_order_text_return_text(driver)
        helpers.click_to_personal_account_button(driver)
        helpers.wait_for_logout_text_and_click(driver)
        assert helpers.wait_for_login_text_return_text(driver) == 'Вход'
