from pages.personal_account_page import PersonalAccount
from data import Urls
import allure


class TestPersonalAccount:

    @allure.title('Вход в личный кабинет зарегистрированным пользователем')
    def test_enter_personal_account(self, user, driver):
        email = user["email"]
        password = user["password"]
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        personal_account_page.click_enter_personal_account_wait_pages_changes()
        assert personal_account_page.save_button_present() == 'Сохранить'

    @allure.title('Переход в раздел "История заказов"')
    def test_history_profile(self, user, driver):
        email = user["email"]
        password = user["password"]
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        personal_account_page.click_enter_personal_account_wait_pages_changes()
        personal_account_page.click_history_profile()
        assert personal_account_page.get_current_url() == Urls.ORDER_HISTORY_PAGE

    @allure.title('Выход из аккаунта')
    def test_exit_account(self, user, driver):
        email = user["email"]
        password = user["password"]
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_button_personal_account()
        personal_account_page.set_email_input(email)
        personal_account_page.set_password_input(password)
        personal_account_page.click_enter_personal_account_wait_pages_changes()
        personal_account_page.click_exit_button()
        personal_account_page.wait_for_url_changes_profile_account()
        assert personal_account_page.get_current_url() == Urls.LOGIN_PAGE
