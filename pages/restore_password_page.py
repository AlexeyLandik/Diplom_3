from pages.base_page import BasePage
import allure
from locators.restore_page_locators import RestorePageLocators
from data import Constants
from data import Urls


class RestorePasswordPage(BasePage):

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_enter_account(self):
        self.click(RestorePageLocators.BUTTON_ENTER_ACCOUNT)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_restore_password(self):
        self.click(RestorePageLocators.BUTTON_RESTORE_PASSWORD)

    @allure.step('Заполнение поля почты')
    def fill_email_field(self, email):
        email_input = self.wait_and_find_element(RestorePageLocators.EMAIL_FIELD)
        email_input.send_keys(email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_restore_password(self):
        self.click(RestorePageLocators.RESTORE_BUTTON)

    @allure.step('Заполнение поля email и клик по кнопке "Восстановить"')
    def fill_email_and_click_restore_button(self):
        self.fill_email_field(Constants.EMAIL)
        self.click_button_restore_password()

    @allure.step('Ожидание смены страницы при восстановлении пароля')
    def wait_url_changed_restore(self):
        self.wait_url_changes(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Получение атрибута 'type' со значением 'text'")
    def get_input_status(self):
        input_status = self.wait_and_find_element(RestorePageLocators.PASSWORD_FIELD)
        return input_status.get_attribute("type") == 'text'

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_show_hide_password(self):
        self.click(RestorePageLocators.SHOW_HIDE_PASSWORD)
