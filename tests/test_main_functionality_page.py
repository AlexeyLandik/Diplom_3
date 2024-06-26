import allure
from pages.main_functionality_page import MainFunctionality
from data import Urls
from pages.order_list_page import OrderList
from pages.personal_account_page import PersonalAccount


class TestMainFunctions:

    @allure.title('Переход по кнопке "Конструктор"')
    def test_click_button_constructor(self, driver):
        main_functions_page = MainFunctionality(driver)
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        main_functions_page.click_button_constructor()
        assert main_functions_page.get_current_url() == Urls.BASE_PAGE_URL

    @allure.title('Переход по кнопке "Лента заказов"')
    def test_click_button_order_list(self, driver):
        main_functions_page = MainFunctionality(driver)
        order_list_page = OrderList(driver)
        order_list_page.click_order_list()
        assert main_functions_page.get_current_url() == Urls.ORDER_LIST_PAGE

    @allure.title('Появление всплывающего окна при клике на ингредиент')
    def test_popup_window(self, driver):
        main_functions_page = MainFunctionality(driver)
        main_functions_page.click_ingredient()
        name = main_functions_page.wait_and_find_header()
        assert name.is_displayed()

    @allure.title('Закрытие модального окна')
    def test_close_popup_window(self, driver):
        main_functions_page = MainFunctionality(driver)
        main_functions_page.click_ingredient()
        main_functions_page.click_close_window()
        assert main_functions_page.cross_not_is_displayed()

    @allure.title('Изменение счетчика заказа')
    def test_put_ingredient_into_basket(self, driver):
        main_functions_page = MainFunctionality(driver)
        main_functions_page.put_ingredient_into_basket()
        result = main_functions_page.counter_ingredient_text()
        assert result == '2'

    @allure.title('Оформление заказа залогиненным пользователем')
    def test_make_order_confirmed(self, user, driver):
        email = user["email"]
        password = user["password"]
        main_functions_page = MainFunctionality(driver)
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        main_functions_page.finish_login_and_make_order()
        name = main_functions_page.wait_and_find_confirmation()
        assert name.is_displayed()
