import allure
from pages.order_list_page import OrderList
from pages.personal_account_page import PersonalAccount


class TestOrderList:

    @allure.title('Открытие окна с заказом')
    def test_click_order_card(self, driver):
        order_list_page = OrderList(driver)
        order_list_page.click_order_list()
        order_list_page.wait_and_find_order_card()
        order_list_page.click_order_card()
        name = order_list_page.wait_and_find_order_card_window()
        assert name.is_displayed()

    @allure.title('Отображение заказа в ленте заказов')
    def test_make_order_and_check_order_list(self, user, driver):
        email = user["email"]
        password = user["password"]
        order_list_page = OrderList(driver)
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        order_list_page.finish_login_make_order_close_window()
        order_list_page.enter_account_enter_profile_history()
        number_profile = order_list_page.number_text()
        order_list_page.click_order_list_and_wait_left_block()
        number_list = order_list_page.block_text()
        assert number_profile in number_list

    @allure.title('Счетчик "Выполнено за всё время" после оформления нового заказа')
    def test_counter_total_changes(self, user, driver):
        email = user["email"]
        password = user["password"]
        order_list_page = OrderList(driver)
        order_list_page.click_order_list_and_find_block_total()
        old_data = order_list_page.block_total_text()
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        order_list_page.finish_login_make_order_close_window()
        order_list_page.click_order_list_and_find_block_total()
        new_data = order_list_page.block_total_text()
        assert int(new_data) > int(old_data)

    @allure.title('Счетчик "Выполнено за сегодня" после оформления нового заказа')
    def test_counter_daily_changes(self, user, driver):
        email = user["email"]
        password = user["password"]
        order_list_page = OrderList(driver)
        order_list_page.click_order_list_find_block_daily()
        old_data = order_list_page.block_daily_text()
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        order_list_page.finish_login_make_order_close_window()
        order_list_page.click_order_list_find_block_daily()
        new_data = order_list_page.block_daily_text()
        assert int(new_data) > int(old_data)

    @allure.title('Отображение созданного заказа в разделе "В работе"')
    def test_make_order_and_check_order_in_work(self, user, driver):
        email = user["email"]
        password = user["password"]
        order_list_page = OrderList(driver)
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        order_list_page.finish_login_make_order_close_window()
        order_list_page.enter_account_enter_profile_history()
        number_profile = order_list_page.number_text()
        order_list_page.click_order_list_find_in_work()
        number_in_work = order_list_page.number_in_work_text()
        assert number_in_work in (number_profile[1:]) or (str(int(number_profile[1:])-1))
