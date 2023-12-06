import allure
from static_data import Urls
from locators.account_page_locators import PasswordResetPageLocators
from pages.auth_page import AuthPage
from pages.password_reset_page import PasswordResetPage


class TestPasswordReset:
    @allure.title('Проверка перехода по клику на Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, driver):
        page = AuthPage(driver)
        page.go_to_site(Urls.url_login)
        page.click_password_reset_link()
        current_url = page.get_current_url()

        assert current_url == Urls.url_password

    @allure.title('Проверка перехода по кнопке Восстановить после ввода емейла')
    def test_enter_email_and_click_reset(self, driver, create_user):
        page = PasswordResetPage(driver)
        page.go_to_site(Urls.url_password)

        page.input_email_for_reset(create_user[0][0])
        page.click_reset_button()
        page.wait_until_element_visibility(10, PasswordResetPageLocators.SAVE_BUTTON)
        current_url = page.get_current_url()

        assert current_url == Urls.url_reset

    @allure.title('Проверка активации поля Пароль после нажатия на кнопку Показать/скрыть пароль')
    def test_show_password_input_active(self, driver, create_user):
        page = PasswordResetPage(driver)
        page.go_to_site(Urls.url_password)

        page.input_email_for_reset(create_user[0][0])
        page.click_reset_button()
        page.wait_until_element_visibility(10, PasswordResetPageLocators.SAVE_BUTTON)
        page.click_show_password_icon()

        assert page.find_element(PasswordResetPageLocators.INPUT_ACTIVE).is_displayed()