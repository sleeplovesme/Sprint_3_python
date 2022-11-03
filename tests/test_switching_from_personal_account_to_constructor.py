import helpers


class TestSwitchToConstructor:
    def test_click_to_constructor(self, driver):
        # Проверь переход по клику на «Конструктор»
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.set_default_email_and_password_and_click_to_login_button(driver)
        helpers.wait_for_register_order_text_return_text(driver)
        helpers.click_to_personal_account_button(driver)
        helpers.wait_for_logout_text(driver)
        helpers.click_to_constructor_button(driver)
        assert helpers.wait_for_register_order_text_return_text(driver) == 'Оформить заказ'

    def test_click_to_logo(self, driver):
        # Проверь переход по клику на логотип Stellar Burgers
        helpers.click_to_personal_account_button_and_wait_for_login_text(driver)
        helpers.set_default_email_and_password_and_click_to_login_button(driver)
        helpers.wait_for_register_order_text_return_text(driver)
        helpers.click_to_personal_account_button(driver)
        helpers.wait_for_logout_text(driver)
        helpers.click_to_logo(driver)
        assert helpers.wait_for_register_order_text_return_text(driver) == 'Оформить заказ'
