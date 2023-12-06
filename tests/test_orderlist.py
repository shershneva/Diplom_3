import allure
from locators.orderlist_page_locators import OrderListPageLocators
from locators.account_page_locators import AccountPageLocators
from pages.orderlist_page import OrderListPage
from pages.main_page import MainPage
from pages.account_page import AccountPage


class TestOrderListPage:
    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_get_order_popup(self, driver):
        mainpage = MainPage(driver)
        mainpage.click_orderlist_button()
        page = OrderListPage(driver)
        page.click_order()

        assert page.find_element(OrderListPageLocators.ORDER_CONTENT).is_displayed() == True

    @allure.title('Проверка отображения созданного заказа в Ленте заказов')
    def test_find_order_in_list(self, driver, signin):
        mainpage = MainPage(driver)
        mainpage.create_order()

        accpage = AccountPage(driver)
        accpage.click_account_button()
        accpage.click_order_list_link()
        accpage.wait_until_element_visibility(10, AccountPageLocators.ORDER_STATUS)
        my_order = accpage.get_order_number()
        mainpage.click_orderlist_button()
        page = OrderListPage(driver)
        page.wait_until_element_visibility(15, OrderListPageLocators.ORDER_LIST_TITLE)
        order = page.get_order_in_orderlist(my_order)

        assert my_order in order

    @allure.title('Проверка увеличения счетчика за все время после создания заказа')
    def test_total_orders_counter(self, driver, signin):
        mainpage = MainPage(driver)
        orderpage = OrderListPage(driver)
        mainpage.click_orderlist_button()
        before_total = orderpage.get_alltime_orders_total()
        mainpage.create_order()
        mainpage.click_orderlist_button()
        after_total = orderpage.get_alltime_orders_total()

        assert before_total < after_total

    @allure.title('Проверка увеличения счетчика заказов за сегодня после создания заказа')
    def test_today_orders_counter(self, driver, signin):
        mainpage = MainPage(driver)
        orderpage = OrderListPage(driver)
        mainpage.click_orderlist_button()
        before_total = orderpage.get_today_orders_total()
        mainpage.create_order()
        mainpage.click_orderlist_button()
        after_total = orderpage.get_today_orders_total()

        assert before_total < after_total

    @allure.title('Проверка есть ли созданный заказ среди заказов в работе')
    def test_new_order_appears_in_work_list(self, driver, signin):
        mainpage = MainPage(driver)
        new_order = mainpage.create_order()
        mainpage.click_orderlist_button()
        page = OrderListPage(driver)
        page.wait_until_element_invisibility(20, OrderListPageLocators.ALL_READY_TITLE)
        order_in_work = page.get_order_number_in_work()

        assert new_order in order_in_work
