from classes import *

class NaturalOperations:
    @staticmethod
    def COM_NN_D(num1: Natural, num2: Natural) -> int:
        """
        Сравнение двух натуральных чисел.
        Возвращает:
        - 2, если num1 > num2
        - 1, если num1 < num2
        - 0, если num1 == num2
        """
        # Сначала сравниваем длину чисел (по количеству цифр)
        if len(num1.digits) > len(num2.digits):
            return 2  # Если первое число длиннее, оно больше
        elif len(num1.digits) < len(num2.digits):
            return 1  # Если первое число короче, оно меньше
        else:
            # Если длины чисел равны, сравниваем их цифры по порядку
            for i in range(len(num1.digits)):
                if num1.digits[i] > num2.digits[i]:
                    return 2  # Если цифра в первом числе больше, возвращаем 2
                elif num1.digits[i] < num2.digits[i]:
                    return 1  # Если цифра в первом числе меньше, возвращаем 1
            return 0  # Если все цифры одинаковые, числа равны

    @staticmethod
    def NZER_N_B(num: Natural) -> str:
        """
        Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
        """
        # Если число состоит только из одной цифры 0, то оно равно нулю
        if len(num.digits) == 1 and num.digits[0] == 0:
            return "нет"  # Число равно нулю
        return "да"  # Число не равно нулю

    @staticmethod
    def ADD_1N_N(num: Natural) -> Natural:
        """
        Добавление 1 к натуральному числу.
        """
        carry = 1  # Перенос (начальный перенос 1)
        result_digits = num.digits[::-1]  # Переворачиваем список цифр для удобства

        # Процесс добавления 1 с учетом переноса
        for i in range(len(result_digits)):
            result_digits[i] += carry  # Добавляем перенос
            if result_digits[i] == 10:  # Если получилось 10, то ставим 0 и переносим 1 дальше
                result_digits[i] = 0
                carry = 1
            else:
                carry = 0  # Если перенос не нужен, завершаем операцию
                break

        # Если перенос остался (например, для числа 999 + 1), добавляем его в конец
        if carry == 1:
            result_digits.append(1)

        result_digits.reverse()  # Возвращаем порядок цифр в нормальное состояние
        return Natural(''.join(map(str, result_digits)))  # Формируем новое число из цифр и возвращаем

    @staticmethod
    def ADD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Сложение двух натуральных чисел.
        """
        carry = 0  # Начальный перенос равен 0
        result_digits = []  # Массив для хранения результата сложения

        len1, len2 = len(num1.digits), len(num2.digits)  # Длины чисел
        max_len = max(len1, len2)  # Определяем максимальную длину

        # Процесс сложения с учетом переноса
        for i in range(max_len):
            # Если цифры не хватает, считаем их как 0
            digit1 = num1.digits[len1 - i - 1] if i < len1 else 0
            digit2 = num2.digits[len2 - i - 1] if i < len2 else 0

            total = digit1 + digit2 + carry  # Сложение цифр с учетом переноса
            result_digits.append(total % 10)  # Добавляем младший разряд к результату
            carry = total // 10  # Перенос на старший разряд

        if carry:
            result_digits.append(carry)  # Если есть перенос в самый старший разряд, добавляем его

        result_digits.reverse()  # Переворачиваем цифры для правильного порядка
        return Natural(''.join(map(str, result_digits)))  # Формируем результат из цифр и возвращаем

    @staticmethod
    def SUB_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычитание из первого большего натурального числа второго меньшего или равного.
        """
        # Проверка, что первое число больше или равно второму
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            raise ValueError("Первое число должно быть больше или равно второму.")

        # Если числа равны, возвращаем ноль
        if NaturalOperations.COM_NN_D(num1, num2) == 0:
            return Natural("0")

        result_digits = []  # Массив для хранения результата
        borrow = 0  # Переменная для учета заимствования (занимания)

        # Процесс вычитания по разрядам
        for i in range(1, len(num1.digits) + 1):
            digit1 = num1.digits[-i]  # Цифра из первого числа
            digit2 = num2.digits[-i] if i <= len(num2.digits) else 0  # Цифра из второго числа (если есть)

            diff = digit1 - digit2 - borrow  # Разность цифр с учетом заимствования
            if diff < 0:  # Если результат отрицательный, "занимаем" единицу
                diff += 10
                borrow = 1
            else:
                borrow = 0  # Если нет заимствования, сбрасываем его

            result_digits.append(diff)  # Добавляем разность в результат

        # Разворачиваем результат, убираем ведущие нули
        result_digits.reverse()
        result_str = ''.join(map(str, result_digits)).lstrip("0")  # Преобразуем результат в строку

        return Natural(result_str or "0")  # Если результат пустой, возвращаем "0"

    @staticmethod
    def MUL_ND_N(num: Natural, digit: Natural) -> Natural:
        """
        Умножение натурального числа на цифру (от 0 до 9).
        """
        digit = digit.__int__()
        # Проверка, что цифра находится в допустимом диапазоне
        if not (0 <= digit <= 9):
            raise ValueError("Цифра должна быть в пределах от 0 до 9.")

        result_digits = []  # Массив для хранения результата умножения
        carry = 0  # Начальный перенос равен 0

        # Умножаем каждую цифру числа на заданную цифру
        for i in range(len(num.digits) - 1, -1, -1):
            temp_product = num.digits[i] * digit + carry  # Умножаем цифру и учитываем перенос
            result_digits.append(temp_product % 10)  # Добавляем младший разряд
            carry = temp_product // 10  # Перенос на старший разряд

        # Если остался перенос, добавляем его в результат
        if carry:
            result_digits.append(carry)

        result_digits.reverse()  # Разворачиваем цифры в правильный порядок
        return Natural(''.join(map(str, result_digits)))  # Формируем новое число и возвращаем

    @staticmethod
    def MUL_Nk_N(num: Natural, k: Natural) -> Natural:
        """
        Умножение натурального числа на 10^k.
        """
        k = k.__int__()
        # Проверка, что k - неотрицательное число
        if k < 0:
            raise ValueError("k должно быть натуральным числом (неотрицательным).")

        if k == 0:
            return num  # Если k равно 0, возвращаем исходное число

        # Добавление k нулей в конец числа
        result_digits = num.digits + [0] * k
        return Natural(''.join(map(str, result_digits)))  # Возвращаем новое число с добавленными нулями

    @staticmethod
    def MUL_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Умножение двух натуральных чисел.
        """
        result = Natural("0")  # Начальный результат - ноль

        # Перебираем цифры второго числа (num2)
        for i in range(len(num2.digits)):
            digit = num2.digits[len(num2.digits) - i - 1]  # Берем цифру из второго числа
            temp = NaturalOperations.MUL_ND_N(num1, digit)  # Умножаем первое число на эту цифру
            temp = NaturalOperations.MUL_Nk_N(temp, i)  # Сдвигаем на разряд, умножив на 10^i
            result = NaturalOperations.ADD_NN_N(result, temp)  # Прибавляем результат к общему

        return result  # Возвращаем итоговый результат умножения

    @staticmethod
    def SUB_NDN_N(num1: Natural, num2: Natural, digit: Natural) -> Natural:
        """
        Вычитает из первого натурального числа результат умножения второго натурального числа на цифру.
        """
        digit = digit.__int__()
        # Проверка, что цифра находится в допустимом диапазоне (от 0 до 9)
        if digit < 0 or digit > 9:
            raise ValueError("Цифра должна быть в пределах от 0 до 9.")

        # Умножаем второе число на цифру
        temp = NaturalOperations.MUL_ND_N(num2, digit)

        # Проверяем, что результат вычитания не будет отрицательным
        if NaturalOperations.COM_NN_D(num1, temp) < 0:
            raise ValueError("Результат вычитания будет отрицательным.")

        # Выполняем вычитание
        return NaturalOperations.SUB_NN_N(num1, temp)

    @staticmethod
    def DIV_NN_Dk(num1: Natural, num2: Natural, k: int) -> int:
        """
        Вычисление первой цифры деления двух чисел,
        домноженной на 10^k, где k — это номер позиции цифры.
        """

        # Преобразуем числа в строковое представление для удобства работы
        larger_digits = ''.join(map(str, num1.digits))  # Переводим первое число в строку
        smaller_digits = ''.join(map(str, num2.digits))  # Переводим второе число в строку

        # Домножаем num2 на 10^k
        num2_modified = NaturalOperations.MUL_Nk_N(num2, k)  # Умножаем второе число на 10^k
        modified_smaller_digits = ''.join(map(str, num2_modified.digits))  # Преобразуем его в строку

        # Выполняем деление
        quotient = int(larger_digits) // int(modified_smaller_digits)  # Делим первое число на изменённое второе

        # Извлекаем первую цифру от деления
        first_digit = int(str(quotient)[0])  # Извлекаем первую цифру результата деления

        return first_digit  # Возвращаем первую цифру результата

    @staticmethod
    def DIV_NN_N(num1: Natural, num2: Natural) -> (Natural, Natural):
        """
        Деление первого натурального числа на второе с остатком.
        Возвращает частное.
        """
        # Проверка, что делитель не равен нулю
        if NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Делитель не может быть нулём.")

        # Если первое число меньше второго, частное = 0, остаток = первое число
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            return Natural("0"), num1  # Частное = 0, остаток = num1

        quotient = []  # Список для хранения цифр частного
        remainder = Natural("0")  # Текущий остаток

        # Перебираем цифры num1 по разрядам
        for digit in num1.digits:
            # Увеличиваем остаток, добавляя текущую цифру из num1
            remainder = NaturalOperations.ADD_NN_N(
                NaturalOperations.MUL_Nk_N(remainder, 1),  # Умножаем остаток на 10 (сдвигаем разряд)
                Natural(str(digit))  # Добавляем текущую цифру
            )

            current_digit = 0
            # Пока остаток больше или равен делителю, вычитаем делитель из остатка
            while NaturalOperations.COM_NN_D(remainder, num2) != 1:  # Пока остаток >= делителя
                remainder = NaturalOperations.SUB_NN_N(remainder, num2)  # Вычитаем делитель
                current_digit += 1  # Увеличиваем цифру частного

            quotient.append(current_digit)  # Добавляем цифру частного в результат

        # Формируем строку из цифр частного
        quotient_natural = Natural(''.join(map(str, quotient)))  # Преобразуем цифры в строку и в объект Natural

        return quotient_natural  # Возвращаем частное и остаток

    @staticmethod
    def MOD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление остатка от деления первого натурального числа на второе.
        Предполагается, что делитель (num2) не равен нулю.
        """
        # Проверка, что делитель не равен нулю
        if NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Делитель не может быть нулём.")

        # Если num1 меньше num2, то остаток равен num1
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            return num1

        # Используем цикл для вычитания num2 из num1, пока num1 >= num2
        remainder = num1
        while NaturalOperations.COM_NN_D(remainder, num2) != 1:
            # Находим первую цифру деления и вычитаем умноженное значение
            digit = NaturalOperations.DIV_NN_Dk(remainder, num2, 0)
            temp = NaturalOperations.MUL_ND_N(num2, digit)  # Умножаем num2 на цифру
            remainder = NaturalOperations.SUB_NN_N(remainder, temp)  # Вычитаем из остатка

        return remainder  # Возвращаем остаток от деления

    @staticmethod
    def GCF_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление наибольшего общего делителя (НОД) двух натуральных чисел.
        Используется алгоритм Евклида.
        """
        # Проверяем, не равен ли одно из чисел нулю
        if NaturalOperations.NZER_N_B(num1) == "нет" or NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Число не может быть равно нулю.")

        while True:
            # Если num1 меньше num2, меняем их местами
            if NaturalOperations.COM_NN_D(num1, num2) < 0:
                num1, num2 = num2, num1

            # Получаем остаток от деления
            remainder = NaturalOperations.MOD_NN_N(num1, num2)

            # Если остаток равен нулю, то num2 является НОД
            if NaturalOperations.COM_NN_D(remainder, Natural("0")) == 0:
                return num2

            # Если остаток не равен нулю, продолжаем с новым делителем
            num1, num2 = num2, remainder

    @staticmethod
    def LCM_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление наименьшего общего кратного (НОК).
        """
        gcf = NaturalOperations.GCF_NN_N(num1, num2)  # Находим НОД
        product = NaturalOperations.MUL_NN_N(num1, num2)  # Умножаем оба числа
        lcm = NaturalOperations.DIV_NN_N(product, gcf)  # Делим произведение на НОД, чтобы получить НОК
        return  lcm  # Возвращаем НОК
