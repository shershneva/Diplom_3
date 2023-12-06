import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from static_data import Urls


class TestMainPage:

    @allure.title('Проверка перехода в Ленту заказов через хедер')
    def test_go_to_order_list(self, driver):
        page = MainPage(driver)
        page.click_orderlist_button()
        current_url = page.get_current_url()

        assert current_url == Urls.url_feed

    @allure.title('Проверка перехода в Конструктор в хедере')
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.click_account_button()
        acc_url = page.get_current_url()
        page.click_construction_button()
        current_url = page.get_current_url()

        assert current_url == Urls.url_main and current_url != acc_url

    @allure.title('Проверка появления всплывающего окна при клике на ингредиент')
    def test_get_ingredient_popup(self, driver):
        page = MainPage(driver)
        page.click_ingredient()

        assert page.find_element(MainPageLocators.INGREDIENT_POPUP_TITLE).is_displayed() == True

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    def test_close_ingredient_details_window(self, driver):
        page = MainPage(driver)
        page.click_ingredient()
        page.click_close_button()
        page.wait_until_element_invisibility(5, MainPageLocators.INGREDIENT_POPUP)

        assert page.find_element(MainPageLocators.INGREDIENT_POPUP_TITLE).is_displayed() == False

    @allure.title('Проверка изменения счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        before_counter = main_page.check_counter_of_ingredients()
        main_page.add_bun_to_basket()
        after_counter = main_page.check_counter_of_ingredients()

        assert after_counter == '2' and before_counter < after_counter

    @allure.title('Проверка успешного создания заказа')
    def test_successful_order(self, driver, signin):
        main_page = MainPage(driver)
        main_page.find_element(MainPageLocators.INGREDIENT_BUN)
        main_page.add_bun_to_basket()
        main_page.add_filling_to_basket()
        main_page.add_sauce_to_basket()
        main_page.find_element(MainPageLocators.ORDER_BUTTON)
        main_page.click_order_button()
        main_page.wait_until_element_visibility(10, MainPageLocators.ORDER_NUMBER)

        assert main_page.find_element(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True


