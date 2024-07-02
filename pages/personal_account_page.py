from data import Urls
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators
import allure


class PersonalAccount(BasePage):

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_profile(self):
        self.click(PersonalAccountPageLocators.BUTTON_HISTORY_PROFILE)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_button(self):
        self.click(PersonalAccountPageLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_button_personal_account(self):
        self.click(PersonalAccountPageLocators.BUTTON_ACCOUNT)

    @allure.step('Заполнение поля email')
    def set_email_input(self, email):
        email_input = self.wait_and_find_element(PersonalAccountPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)

    @allure.step('Заполнение поля password')
    def set_password_input(self, password):
        email_input = self.wait_and_find_element(PersonalAccountPageLocators.INPUT_PASSWORD)
        email_input.send_keys(password)

    @allure.step('Клик по кнопке "Войти"')
    def click_enter_button(self):
        self.click(PersonalAccountPageLocators.BUTTON_ENTER)

    @allure.step('Ожидание смены страницы логина')
    def wait_url_changes_login(self):
        self.wait_url_changes(Urls.LOGIN_PAGE)

    @allure.step('Ожидание смены главной страницы')
    def wait_for_url_changes_main(self):
        self.wait_url_changes(Urls.BASE_PAGE_URL)

    @allure.step('Ожидание смены страницы аккаунт')
    def wait_for_url_changes_account(self):
        self.wait_url_changes(Urls.ACCOUNT_PAGE)

    @allure.step('Ожидание смены страницы аккаунт-профайл')
    def wait_for_url_changes_profile_account(self):
        self.wait_url_changes(Urls.ACCOUNT_PROFILE_PAGE)

    @allure.step('Вход в личный кабинет с ожиданием смены необходимых страниц')
    def click_enter_personal_account_wait_pages_changes(self):
        self.click_enter_button()
        self.wait_url_changes_login()
        self.click_button_personal_account()
        self.wait_for_url_changes_main()
        self.wait_for_url_changes_account()

    @allure.step('Поиск текста кнопки "Сохранить"')
    def save_button_present(self):
        return self.find_text(PersonalAccountPageLocators.BUTTON_SAVE)
