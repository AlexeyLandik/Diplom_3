from selenium.webdriver.common.by import By


class RestorePageLocators:
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_HIDE_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']")
