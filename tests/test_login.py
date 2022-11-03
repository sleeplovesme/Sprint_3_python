import helpers


class TestLogin:
    def test_login_using_login_to_account_button_on_main_page(self, driver):
        # вход по кнопке «Войти в аккаунт» на главной
        helpers.click_login_to_your_account_button(driver)
        helpers.wait_for_login_text(driver)
        helpers.set_default_email_and_password_and_click_to_login_button(driver)
        assert helpers.wait_for_register_order_text_return_text(driver) == 'Оформить заказ'

    def test_login_via_personal_account_button(self, driver):
        # вход через кнопку «Личный кабинет»
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.set_default_email_and_password_and_click_to_login_button(driver)
        assert helpers.wait_for_register_order_text_return_text(driver) == 'Оформить заказ'

    def test_login_via_button_in_registration_form(self, driver):
        # вход через кнопку в форме регистрации
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.click_to_register_link(driver)
        helpers.wait_for_registration_text(driver)
        helpers.click_to_login_link_and_wait_for_login_text(driver)
        helpers.set_default_email_and_password_and_click_to_login_button(driver)
        assert helpers.wait_for_register_order_text_return_text(driver) == 'Оформить заказ'

    def test_login_via_button_in_password_recovery_form(self, driver):
        # вход через кнопку в форме восстановления пароля
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.click_to_password_recovery_link(driver)
        helpers.wait_for_password_recovery_text(driver)
        helpers.click_to_login_link_and_wait_for_login_text(driver)
        helpers.set_default_email_and_password_and_click_to_login_button(driver)
        assert helpers.wait_for_register_order_text_return_text(driver) == 'Оформить заказ'
