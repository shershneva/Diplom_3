import allure
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import HeadersLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Переходим на страницу ЛК')
    def click_account_button(self):
        self.click_element(HeadersLocators.ACCOUNT_LINK)
        self.wait_until_element_visibility(15, AccountPageLocators.PROFILE_LINK)

    @allure.step('Выходим из аккаунта по кнопке Выход в ЛК')
    def click_logout_button(self):
        self.click_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Переходим в Историю заказов')
    def click_order_list_link(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step('Получаем номер заказа в Истории заказов')
    def get_order_number(self):
        return self.get_element_text(AccountPageLocators.ORDER_NUMBER)
