from pages.base_page import BasePage
import allure
from seletools.actions import drag_and_drop
from data import Urls
from locators.order_list_page_locators import OrderListLocators
# from locators.main_functionality_page_locators import MainFunctionalityLocators
# from locators.personal_account_page_locators import PersonalAccountPageLocators


class OrderList(BasePage):

    @allure.step('Клик по кнопке "Ленте заказов"')
    def click_order_list(self):
        self.click(OrderListLocators.BUTTON_ORDER_LIST)

    @allure.step('Поиск заголовка карточки заказа')
    def wait_and_find_order_card(self):
        name = self.wait_and_find_element(OrderListLocators.ORDER_CARD)
        return name

    @allure.step('Клик по карточке заказа')
    def click_order_card(self):
        self.click(OrderListLocators.ORDER_CARD)

    @allure.step('Поиск всплывающего окна')
    def wait_and_find_order_card_window(self):
        name = self.wait_and_find_element(OrderListLocators.ORDER_CARD_MODAL_WINDOW)
        return name

    @allure.step('Перетаскиваем ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_and_find_element(OrderListLocators.INGREDIENT)
        basket = self.wait_and_find_element(OrderListLocators.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_button_account(self):
        self.click(OrderListLocators.BUTTON_ACCOUNT)

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        self.click(OrderListLocators.BUTTON_ENTER)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_make_order(self):
        self.click(OrderListLocators.BUTTON_MAKE_ORDER)

    @allure.step('Клик по крестику всплывающего окна')
    def click_cross(self):
        self.click(OrderListLocators.ORDER_CARD_MODAL_WINDOW_CROSS)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_profile(self):
        self.click(OrderListLocators.BUTTON_HISTORY_PROFILE)

    @allure.step('Войти в личный кабинет, далее в "Историю заказов" и дождаться карточки заказа')
    def enter_account_enter_profile_history(self):
        self.click_button_account()
        self.wait_for_url_changes_main()
        self.wait_for_url_changes_profile()
        self.click_history_profile()
        self.wait_and_find_order_card()

    @allure.step('Завершить логин пользователя и оформить заказ, кликнув по крестику окна')
    def finish_login_make_order_close_window(self):
        self.click_enter_button()
        self.put_ingredient_into_basket()
        self.click_make_order()
        self.click_cross()

    @allure.step('Поиск текста по локатору "номер карточки заказа"')
    def number_text(self):
        return self.find_text(OrderListLocators.ORDER_NUMBER_CARD)

    @allure.step('Поиск текста по локатору левого блока с карточками заказов')
    def block_text(self):
        return self.find_text(OrderListLocators.LEFT_BLOCK)

    @allure.step('Ожидание смены главной страницы')
    def wait_for_url_changes_main(self):
        self.wait_url_changes(Urls.BASE_PAGE_URL)

    @allure.step('Ожидание смены страницы профайл')
    def wait_for_url_changes_profile(self):
        self.wait_url_changes(Urls.ACCOUNT_PAGE)

    @allure.step('Поиск элемента левого блока с карточками заказов по локатору')
    def wait_and_find_left_block(self):
        name = self.wait_and_find_element(OrderListLocators.LEFT_BLOCK)
        return name

    @allure.step('Кликнуть по кнопке "Лента заказов" и дождаться появления левого блока')
    def click_order_list_and_wait_left_block(self):
        self.click_order_list()
        self.wait_and_find_left_block()

    @allure.step('Ожидание появления блока со счетчиком "За все время"')
    def wait_and_find_block_total(self):
        name = self.wait_and_find_element(OrderListLocators.ORDER_COUNT_TOTAL)
        return name

    @allure.step('Получение текста из счетчика "За все время"')
    def block_total_text(self):
        return self.find_text(OrderListLocators.ORDER_COUNT_TOTAL)

    @allure.step('Ожидание появления блока со счетчиком "За сегодня')
    def wait_and_find_block_daily(self):
        name = self.wait_and_find_element(OrderListLocators.ORDER_COUNT_DAY)
        return name

    @allure.step('Получение текста из счетчика "За сегодня"')
    def block_daily_text(self):
        return self.find_text(OrderListLocators.ORDER_COUNT_DAY)

    @allure.step('Клик по кнопке "Лента заказов" и дождаться появления блока счетчика "За все время"')
    def click_order_list_and_find_block_total(self):
        self.click_order_list()
        self.wait_and_find_block_total()

    @allure.step('Клик по кнопке "Лента заказов" и ожидание появления блока счетчика "За сегодня"')
    def click_order_list_find_block_daily(self):
        self.click_order_list()
        self.wait_and_find_block_daily()

    @allure.step('Ожидание появления блока раздела "В работе"')
    def wait_and_find_number_in_work(self):
        name = self.wait_and_find_element(OrderListLocators.NUMBER_IN_WORK)
        return name

    @allure.step('Получение текста из блока раздела "В работе"')
    def number_in_work_text(self):
        return self.find_text(OrderListLocators.NUMBER_IN_WORK)

    @allure.step('Клик по кнопке "Лента заказов" и ожидание появления блока раздела "В работе"')
    def click_order_list_find_in_work(self):
        self.click_order_list()
        self.wait_and_find_number_in_work()
