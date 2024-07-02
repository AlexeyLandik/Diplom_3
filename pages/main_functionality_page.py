from pages.base_page import BasePage
import allure
from seletools.actions import drag_and_drop
from locators.main_functionality_page_locators import MainFunctionalityLocators


class MainFunctionality(BasePage):

    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.click(MainFunctionalityLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по ингредиенту"')
    def click_ingredient(self):
        self.click(MainFunctionalityLocators.INGREDIENT)

    @allure.step('Заголовок всплывающего окна')
    def wait_and_find_header(self):
        name = self.wait_and_find_element(MainFunctionalityLocators.POPUP_WINDOW_HEADER)
        return name

    @allure.step('Клик по крестику, чтобы закрыть всплывающее окно')
    def click_close_window(self):
        self.click(MainFunctionalityLocators.CLOSE_BUTTON)

    @allure.step('Невидимый крестик для закрытия окна')
    def cross_not_is_displayed(self):
        name = self.wait_and_find_element_invisible(MainFunctionalityLocators.CLOSE_BUTTON)
        return not name.is_displayed()

    @allure.step('Перетаскиваем ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_and_find_element(MainFunctionalityLocators.INGREDIENT)
        basket = self.wait_and_find_element(MainFunctionalityLocators.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)

    @allure.step('Поиск текста по локатору ингредиента')
    def counter_ingredient_text(self):
        return self.find_text(MainFunctionalityLocators.INGREDIENT)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_make_order(self):
        self.click(MainFunctionalityLocators.BUTTON_MAKE_ORDER)

    @allure.step('Поиск текста о подтверждении заказа')
    def wait_and_find_confirmation(self):
        name = self.wait_and_find_element(MainFunctionalityLocators.CONFIRMATION_TEXT)
        return name

    @allure.step('Перетаскиваем ингредиент в корзину покупателя')
    def put_ingredient_into_basket(self):
        ingredient = self.wait_and_find_element(MainFunctionalityLocators.INGREDIENT)
        basket = self.wait_and_find_element(MainFunctionalityLocators.ORDER_BASKET)
        drag_and_drop(self.driver, ingredient, basket)
