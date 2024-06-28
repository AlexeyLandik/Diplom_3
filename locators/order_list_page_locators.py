from selenium.webdriver.common.by import By


class OrderListLocators:
    BUTTON_ORDER_LIST = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_NUMBER_CARD = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]")
    ORDER_COUNT_TOTAL = (
    By.XPATH, "//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_COUNT_DAY = (By.XPATH, "(//div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    ORDER_CARD = (By.XPATH, "(//a[@class='OrderHistory_link__1iNby'])[1]")
    ORDER_CARD_MODAL_WINDOW_CROSS = (
    By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    ORDER_CARD_MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    LEFT_BLOCK = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']")
    NUMBER_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")
    INGREDIENT = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']/div/p["
                            "@class='counter_counter__num__3nue1']")
    ORDER_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    BUTTON_HISTORY_PROFILE = (By.XPATH, "//a[text()='История заказов']")
