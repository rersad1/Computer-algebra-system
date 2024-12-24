from classes import *
from operations.natural_operations import NaturalOperations

class IntegerOperations:
    @staticmethod
    def ABS_Z_N(num: Integer) -> Natural:
        """
        Возвращает абсолютное значение целого числа как натуральное.
        """
        digits_str = ''.join(map(str, num.get_digits()))  # Получаем строковое представление всех цифр числа.
        return Natural(digits_str)  # Создаем объект типа Natural, используя строку цифр.

    @staticmethod
    def POZ_Z_D(num: Integer) -> int:
        """
        Определяет знак числа:
        2 - положительное, 1 - отрицательное, 0 - равно нулю.
        """
        # Проверяем, является ли число нулём (одна цифра и эта цифра равна 0)
        if len(num.get_digits()) == 1 and num.get_digits()[0] == 0:
            return 0  # Число равно нулю.

        # Если знак числа True (отрицательное), возвращаем 1, если False (положительное), то 2.
        return 1 if num.get_sign() else 2

    @staticmethod
    def MUL_ZM_Z(num: Integer) -> Integer:
        """
        Умножение целого числа на (-1).
        """
        # Получаем текущий знак и цифры числа
        current_sign = num.get_sign()  # True если отрицательное, False если положительное
        digits = num.get_digits()

        # Проверяем, является ли число нулём
        is_zero = len(digits) == 1 and digits[0] == 0

        if is_zero:
            # Если число ноль, не инвертируем знак
            new_number = '0'
        else:
            # Инвертируем знак числа
            new_sign = not current_sign
            digits_str = ''.join(map(str, digits))
            new_number = ('-' if new_sign else '') + digits_str

        return Integer(new_number)

    @staticmethod
    def TRANS_N_Z(num: Natural) -> Integer:
        """
        Преобразует натуральное число в целое.
        """
        digits_str = ''.join(map(str, num.get_digits()))  # Получаем строковое представление всех цифр числа.
        return Integer(digits_str)  # Возвращаем целое число с положительным значением.

    @staticmethod
    def TRANS_Z_N(num: Integer) -> Natural:
        """
        Преобразует целое число в натуральное.
        """
        if num.get_sign():  # Если знак числа отрицательный.
            raise ValueError("Отрицательное число нельзя преобразовать в натуральное.")  # Исключение для отрицательных чисел.

        digits_str = ''.join(map(str, num.get_digits()))  # Получаем строковое представление всех цифр числа.
        return Natural(digits_str)  # Создаем объект типа Natural, используя строку цифр.

    @staticmethod
    def ADD_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Сложение двух целых чисел.
        """
        # Определяем знаки чисел: положительное (2), отрицательное (1), ноль (0).
        poz1 = IntegerOperations.POZ_Z_D(num1)  # Знак первого числа.
        poz2 = IntegerOperations.POZ_Z_D(num2)  # Знак второго числа.

        # Если одно из чисел равно 0, возвращаем другое число.
        if poz1 == 0:
            return num2
        if poz2 == 0:
            return num1

        # Получаем модули чисел (абсолютные значения).
        abs_num1 = IntegerOperations.ABS_Z_N(num1)
        abs_num2 = IntegerOperations.ABS_Z_N(num2)


        if poz1 == poz2:  # Оба числа одного знака.
            # Складываем их абсолютные значения (модули).
            sum_abs = NaturalOperations.ADD_NN_N(abs_num1, abs_num2)
            result_sign = num1.get_sign()  # Знак результата будет такой же, как у чисел.
        else:  # Числа с разными знаками.
            # Определяем большее и меньшее число по модулю.
            comparison = NaturalOperations.COM_NN_D(abs_num1, abs_num2)
            if comparison == 2:  # abs_num1 > abs_num2
                difference = NaturalOperations.SUB_NN_N(abs_num1, abs_num2)  # Вычитаем меньшую величину из большей.
                result_sign = num1.get_sign()  # Знак результата будет совпадать с первым числом.
            else:  # abs_num1 <= abs_num2
                difference = NaturalOperations.SUB_NN_N(abs_num2, abs_num1)  # Вычитаем большее из меньшего.
                result_sign = num2.get_sign()  # Знак результата будет совпадать со знаком второго числа.

            # Если результат равен 0, результат всегда положительный.
            if len(difference.get_digits()) == 1 and difference.get_digits()[0] == 0:
                result_sign = False

            sum_abs = difference  # Результат сложения чисел.

        # Создаем строку для результата.
        result_digits = ''.join(map(str, sum_abs.get_digits()))
        result_number = ('-' if result_sign else '') + result_digits  # Если знак отрицательный, ставим минус в начало.
        return Integer(result_number)  # Возвращаем результат сложения двух целых чисел.

    @staticmethod
    def SUB_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Вычитание двух целых чисел.
        """
        # Определяем знак каждого числа
        poz_num1 = IntegerOperations.POZ_Z_D(num1)
        poz_num2 = IntegerOperations.POZ_Z_D(num2)

        # Преобразуем целые числа в натуральные (их абсолютные значения)
        abs_num1 = IntegerOperations.ABS_Z_N(num1)
        abs_num2 = IntegerOperations.ABS_Z_N(num2)

        if poz_num1 != poz_num2:  # Если числа с разными знаками
            # Складываем модули чисел
            result_abs = NaturalOperations.ADD_NN_N(abs_num1, abs_num2)

            # Знак результата зависит от знака первого числа
            if poz_num1 == 1:
                result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))
            else:
                result = Integer(str(result_abs))
        else:  # Если числа с одинаковыми знаками
            # Сравниваем их абсолютные значения
            comparison = NaturalOperations.COM_NN_D(abs_num1, abs_num2)
            
            if comparison == 2:  # |num1| > |num2|
                result_abs = NaturalOperations.SUB_NN_N(abs_num1, abs_num2)
                if poz_num1 == 1:  # Если оба отрицательные
                    result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))
                else:
                    result = Integer(str(result_abs))
            else:  # |num1| ≤ |num2|
                result_abs = NaturalOperations.SUB_NN_N(abs_num2, abs_num1)
                # Ключевое изменение: всегда делаем результат отрицательным при вычитании большего из меньшего
                if poz_num1 == 1:  # Если оба отрицательные
                    result = Integer(str(result_abs))
                else:  # Если оба положительные
                    result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))

        return result

    @staticmethod
    def MUL_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Умножение двух целых чисел.
        """
        # Определяем знак каждого числа.
        poz_num1 = IntegerOperations.POZ_Z_D(num1)  # Знак первого числа.
        poz_num2 = IntegerOperations.POZ_Z_D(num2)  # Знак второго числа.


        # Умножаем абсолютные значения чисел.
        abs_num1 = IntegerOperations.ABS_Z_N(num1)
        abs_num2 = IntegerOperations.ABS_Z_N(num2)
        result_abs = NaturalOperations.MUL_NN_N(abs_num1, abs_num2)

        # Определяем знак результата.
        if (poz_num1 == 1 and poz_num2 == 2) or (poz_num1 == 2 and poz_num2 == 1):
            result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))  # Если знаки разные, результат отрицателен.
        else:
            result = Integer(str(result_abs))  # Если знаки одинаковые, результат положительный.

        return result  # Возвращаем результат умножения.

    @staticmethod
    def DIV_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Деление одного целого числа на другое.
        """
        # Проверяем, что делитель не равен нулю.
        if IntegerOperations.POZ_Z_D(num2) == 0:
            raise ValueError("Делитель не может быть равен нулю.")

        # Получаем абсолютные значения чисел.
        abs_num1 = IntegerOperations.ABS_Z_N(num1)
        abs_num2 = IntegerOperations.ABS_Z_N(num2)

        # Выполняем деление как натуральных чисел.
        quotient_abs = NaturalOperations.DIV_NN_N(abs_num1, abs_num2)  # Получаем только частное.

        # Определяем знак результата.
        poz_num1 = IntegerOperations.POZ_Z_D(num1)
        poz_num2 = IntegerOperations.POZ_Z_D(num2)

        # Определяем, имеют ли числа противоположные знаки
        if (poz_num1 == 1 and poz_num2 == 2) or (poz_num1 == 2 and poz_num2 == 1):
            # Если делимое и делитель имеют противоположные знаки, результат отрицательный
            quotient = IntegerOperations.MUL_ZM_Z(Integer(str(quotient_abs)))
        else:
            # Если делимое и делитель имеют одинаковые знаки, результат положительный
            quotient = Integer(str(quotient_abs))

        return quotient  # Возвращаем результат деления.


    @staticmethod
    def MOD_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Вычисление остатка от деления целого на целое.
        """
        # Проверяем делитель на ноль.
        if IntegerOperations.POZ_Z_D(num2) == 0:
            raise ValueError("Делитель не может быть равен нулю.")

        # Получаем частное от деления.
        quotient = IntegerOperations.DIV_ZZ_Z(num1, num2)

        # Умножаем частное на делитель, чтобы получить кратное.
        product = IntegerOperations.MUL_ZZ_Z(quotient, num2)

        # Находим остаток, вычитая кратное из делимого.
        remainder = IntegerOperations.SUB_ZZ_Z(num1, product)

        # Если делитель отрицателен, меняем знак остатка.
        if IntegerOperations.POZ_Z_D(num2) == 1:
            remainder = IntegerOperations.MUL_ZM_Z(remainder)

        return remainder  # Возвращаем остаток от деления.

