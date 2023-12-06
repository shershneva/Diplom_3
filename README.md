# Diplom_3
## Автотесты для веб-приложения сайта Stellar Burgers ## 
Используются библиотеки random и string для тестовых данных. 
Для запросов к API в части создания тестового клиента используются библиотеки json и requests.
Для генерации отчетов используется библиотека allure, для запуска тестов pytest.

### Файл generator содержит функции: ###
generate_random_string - генерация строки заданной длины
create_new_user - генерация нового пользователя

### Файл static_data: ###
содержит тестовые ссылки

## TestPasswordReset ##
* test_click_password_reset_button — Нажатие на ссылку восстановления пароля на странице авторизации
* test_enter_email_and_click_reset — Проверка перехода по кнопке Восстановить после ввода емейла
* test_show_password_input_active — Проверка активации поля Пароль после нажатия на кнопку Показать/скрыть пароль


## TestAccountPage ##
* test_go_to_account_from_header — Проверка перехода по кнопке Личный кабинет
* test_go_to_order_history — Проверка перехода в раздел История заказов
* test_user_logout — Проверка выхода из аккаунта


## TestMainPage ##
* test_go_to_order_list — Проверка перехода в Ленту заказов через хедер
* test_go_to_constructor — Проверка перехода в Конструктор в хедере
* test_get_ingredient_popup — Проверка появления всплывающего окна при клике на ингредиент
* test_close_ingredient_details_window — Проверка закрытия всплывающего окна с деталями ингредиента
* test_ingredient_counter — Проверка изменения счетчика ингредиента
* test_successful_order — Проверка успешного создания заказа


## TestOrderListPage ##
* test_get_order_popup — Проверка открытия всплывающего окна с деталями заказа
* test_find_order_in_list — Проверка отображения созданного заказа в Ленте заказов
* test_total_orders_counter — Проверка увеличения счетчика за все время после создания заказа
* test_today_orders_counter — Проверка увеличения счетчика заказов за сегодня после создания заказа
* test_new_order_appears_in_work_list — Проверка есть ли созданный заказ среди заказов в работе

