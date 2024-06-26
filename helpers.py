import random
import string
import allure


class User:
    @staticmethod
    @allure.step('Получение случайных данных для создания пользователя')
    def create_random_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = f'{generate_random_string(5)}@mail.ru'
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        login_pass = {"email": login, "password": password, "name": first_name}
        return login_pass
