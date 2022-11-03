import helpers


class TestConstructorSections:
    def test_transitions_to_section_buns(self, driver):
        # Проверь, что работают переходы к разделам: «Булки»
        helpers.click_to_section_sauces(driver)
        helpers.click_to_section_buns(driver)
        assert helpers.wait_for_buns_text_return_text(driver) == 'Булки'

    def test_transitions_to_section_sauces(self, driver):
        # Проверь, что работают переходы к разделам: «Соусы»
        helpers.click_to_section_sauces(driver)
        assert helpers.wait_for_sauces_text_return_text(driver) == 'Соусы'

    def test_transitions_to_section_fillings(self, driver):
        # Проверь, что работают переходы к разделам: «Начинки»
        helpers.click_to_section_fillings(driver)
        assert helpers.wait_for_fillings_text_return_text(driver) == 'Начинки'
