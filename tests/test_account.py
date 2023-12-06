import allure
from locators.account_page_locators import AuthPageLocators
from pages.account_page import AccountPage
from static_data import Urls


class TestAccountPage:
    @allure.title('Проверка перехода по кнопке Личный кабинет')
    def test_go_to_account_from_header(self, driver, signin):
        page = AccountPage(driver)
        page.click_account_button()
        current_url = page.get_current_url()

        assert current_url == Urls.url_account

    @allure.title('Проверка перехода в раздел История заказов')
    def test_go_to_order_history(self, driver, signin):
        page = AccountPage(driver)
        page.click_account_button()
        page.click_order_list_link()
        current_url = page.get_current_url()

        assert current_url == Urls.url_history

    @allure.title('Проверка выхода из аккаунта')
    def test_user_logout(self, driver, signin):
        page = AccountPage(driver)
        page.click_account_button()
        page.click_logout_button()
        page.wait_until_element_visibility(10, AuthPageLocators.ENTER_BUTTON)
        button_text = page.get_element_text(AuthPageLocators.ENTER_BUTTON)

        assert button_text == 'Войти'



