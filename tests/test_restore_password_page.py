from pages.restore_password_page import RestorePasswordPage
from data import Urls
import allure


class TestRestorePasswordPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_restore_password_page(self, driver):
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.click_enter_account()
        restore_password_page.click_restore_password()
        assert restore_password_page.get_current_url() == Urls.FORGOT_PASSWORD_PAGE

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_click_restore(self, driver):
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.click_enter_account()
        restore_password_page.click_restore_password()
        restore_password_page.fill_email_and_click_restore_button()
        restore_password_page.wait_url_changed_restore()
        assert restore_password_page.get_current_url() == Urls.RESET_PASSWORD_PAGE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_show_hide_password(self, driver):
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.click_enter_account()
        restore_password_page.click_restore_password()
        restore_password_page.fill_email_and_click_restore_button()
        restore_password_page.wait_url_changed_restore()
        not_active = restore_password_page.get_input_status()
        restore_password_page.click_show_hide_password()
        active = restore_password_page.get_input_status()
        assert not not_active and active
