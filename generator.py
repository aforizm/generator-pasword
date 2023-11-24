import random
import string
import secrets


class Generator:
    def __init__(self, length: int, lower: bool, number: bool, symbol: bool, upper: bool = True):
        self.__length = length  # длина пароля
        self.__is_upper = upper  # будут ли буквы с верхним регистром
        self.__is_lower = lower  # будут ли буквы с нижн регистром
        self.__is_numbers = number  # будут ли цифры
        self.__is_symbols = symbol  # будут ли символы(punctuation)

    def generate(self):
        chars = self.__get_character_set()

        while True:
            password = self.__generate_password(chars)

            if self.__meets_requirements(password):
                break

        return password

    def __get_character_set(self):
        chars = []

        if not any([self.__is_upper, self.__is_lower, self.__is_numbers, self.__is_symbols]):
            self.__is_lower = True

        if self.__is_upper:
            chars.extend(string.ascii_uppercase)
        if self.__is_lower:
            chars.extend(string.ascii_lowercase)
        if self.__is_numbers:
            chars.extend(string.digits)
        if self.__is_symbols:
            chars.extend(string.punctuation)

        return chars

    def __generate_password(self, chars):
        return ''.join(secrets.choice(chars) for _ in range(self.__length))

    def __meets_requirements(self, password):
        if self.__is_upper and not any(c.isupper() for c in password):
            return False
        if self.__is_numbers and not any(c.isdigit() for c in password):
            return False
        if self.__is_lower and not any(c.islower() for c in password):
            return False
        if self.__is_symbols and not any(p in password for p in string.punctuation):
            return False

        return True
