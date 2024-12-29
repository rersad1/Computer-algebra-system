from classes import *

class NaturalOperations:
    @staticmethod
    def COM_NN_D(num1: Natural, num2: Natural) -> int:
        """
        Сравнение натуральных чисел: 2 - если первое больше второго, 
        0 - если равны, 1 - если первое меньше второго
        """
        if len(num1.digits) != len(num2.digits):
            return 2 if len(num1.digits) > len(num2.digits) else 1
        # Используем zip для эффективного сравнения
        for d1, d2 in zip(num1.digits, num2.digits):
            if d1 != d2:
                return 2 if d1 > d2 else 1
        return 0

    @staticmethod
    def NZER_N_B(num: Natural) -> str:
        """
        Проверка на ноль: если число не равно нулю, то "да",
        если число равно нулю, то "нет"
        """
        return "нет" if len(num.digits) == 1 and num.digits[0] == 0 else "да"

    @staticmethod
    def ADD_1N_N(num: Natural) -> Natural:
        """
        Добавление 1 к натуральному числу
        """
        result = Natural("0")
        result.digits = num.digits.copy()
        
        # Ищем самую правую цифру, не равную 9
        i = len(result.digits) - 1
        while i >= 0 and result.digits[i] == 9:
            result.digits[i] = 0
            i -= 1
            
        # Если все цифры были 9, добавляем 1 в начало
        if i < 0:
            result.digits.insert(0, 1)
        else:
            result.digits[i] += 1
            
        return result

    @staticmethod
    def ADD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Сложение двух натуральных чисел
        """
        result = Natural("0")
        max_len = max(len(num1.digits), len(num2.digits))
        # Выделяем память с учетом возможного переноса в старший разряд
        result.digits = [0] * (max_len + 1)
        
        # Получаем прямой доступ к массивам цифр для оптимизации
        d1 = num1.digits
        d2 = num2.digits
        carry = 0
        i = 1
        
        # Складываем числа поразрядно справа налево
        while i <= max_len:
            # Берем цифры с конца или 0, если разряд закончился
            v1 = d1[-i] if i <= len(d1) else 0
            v2 = d2[-i] if i <= len(d2) else 0
            total = v1 + v2 + carry
            result.digits[-i] = total % 10  # Записываем остаток
            carry = total // 10  # Вычисляем перенос
            i += 1
            
        # Обрабатываем последний перенос или убираем ведущий ноль
        if carry:
            result.digits[0] = carry
        else:
            result.digits.pop(0)
        return result

    @staticmethod
    def SUB_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычитание из первого большего натурального числа второго меньшего
        или равного
        """
        # Проверяем, что первое число больше второго
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            raise ValueError("First number should be greater")

        result = []
        borrow = 0
        # Копируем цифры первого числа
        digits1 = num1.digits.copy()
        # Дополняем нулями второе число слева до длины первого
        digits2 = [0] * (len(digits1) - len(num2.digits)) + num2.digits

        # Вычитаем поразрядно справа налево
        for i in range(len(digits1) - 1, -1, -1):
            diff = digits1[i] - digits2[i] - borrow
            # Если разность отрицательная, занимаем 10 из следующего разряда
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.insert(0, diff)

        # Убираем ведущие нули
        while len(result) > 1 and result[0] == 0:
            result.pop(0)

        new_natural = Natural("0")
        new_natural.digits = result
        return new_natural

    @staticmethod
    def MUL_ND_N(num: Natural, digit: int) -> Natural:
        """
        Умножение натурального числа на цифру
        """
        # Особые случаи умножения на 0 и 1
        if digit == 0:
            return Natural("0")
        if digit == 1:
            result = Natural("0")
            result.digits = num.digits.copy()
            return result
            
        result = Natural("0")
        # Резервируем место для результата с учетом возможного переноса
        result.digits = [0] * (len(num.digits) + 1)
        carry = 0
        
        # Умножаем каждую цифру справа налево
        for i in range(len(num.digits) - 1, -1, -1):
            prod = num.digits[i] * digit + carry
            result.digits[i + 1] = prod % 10  # Записываем остаток
            carry = prod // 10   # Вычисляем перенос
            
        # Обрабатываем последний перенос
        if carry:
            result.digits[0] = carry
        else:
            result.digits.pop(0)
        return result

    @staticmethod
    def MUL_Nk_N(num: Natural, k: Natural) -> Natural:
        """
        Умножение натурального числа на 10^k
        """
        # Преобразуем k в int, если это объект Natural
        k_value = int(str(k)) if isinstance(k, Natural) else k
        
        # При умножении на 10^0 возвращаем исходное число
        if k_value == 0:
            return num
        
        result = Natural("0")
        # Копируем цифры и добавляем k нулей справа
        result.digits = num.digits.copy()
        result.digits.extend([0] * k_value)
        return result


    @staticmethod
    def MUL_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Умножение двух натуральных чисел
        """
        # Меняем числа местами, если второе длиннее
        if len(num2.digits) > len(num1.digits):
            num1, num2 = num2, num1
            
        # Проверка на умножение на ноль
        if num2.digits == [0]:
            return Natural("0")
            
        result = Natural("0")
        # Выделяем память для результата с учетом максимально возможной длины
        result.digits = [0] * (len(num1.digits) + len(num2.digits))
        
        # Умножаем каждую цифру второго числа на первое число
        for i in range(len(num2.digits)-1, -1, -1):
            if num2.digits[i] == 0:
                continue
            carry = 0
            # Умножаем на каждую цифру первого числа
            for j in range(len(num1.digits)-1, -1, -1):
                pos = i + j + 1
                prod = num2.digits[i] * num1.digits[j] + result.digits[pos] + carry
                result.digits[pos] = prod % 10  # Записываем остаток
                carry = prod // 10  # Запоминаем перенос
            result.digits[i] = carry
            
        # Убираем ведущие нули
        while len(result.digits) > 1 and result.digits[0] == 0:
            result.digits.pop(0)
        return result

    @staticmethod
    def SUB_NDN_N(num1: Natural, num2: Natural, multiplier: Natural) -> Natural:
        """
        Вычитание из натурального числа другого натурального числа, умноженного на натуральное число
        
        Args:
            num1 (Natural): Уменьшаемое
            num2 (Natural): Вычитаемое (до умножения)
            multiplier (Natural): Множитель
            
        Returns:
            Natural: Результат вычитания (num1 - num2 * multiplier)
        """    
        product = NaturalOperations.MUL_NN_N(num2, multiplier)
        return NaturalOperations.SUB_NN_N(num1, product)

    @staticmethod
    def DIV_NN_Dk(num1: Natural, num2: Natural, k: int) -> int:
        """
        Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k
        """
        # Проверка корректности k
        if k < 0:
            raise ValueError("k must be non-negative")
            
        # Умножаем делитель на 10^k
        scaled_num2 = NaturalOperations.MUL_Nk_N(num2, k)
        print(f"Scaled num2: {scaled_num2}")
        quotient = 0
        
        # Вычитаем делитель пока возможно
        while NaturalOperations.COM_NN_D(num1, scaled_num2) >= 0:
            num1 = NaturalOperations.SUB_NN_N(num1, scaled_num2)
            quotient += 1
            
        return quotient

    @staticmethod
    def DIV_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Целочисленное деление двух натуральных чисел
        """
        # Проверка деления на ноль
        if not num2.digits or num2.digits == [0]:
            raise ValueError("Division by zero")

        # Если делимое меньше делителя - результат 0
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            return Natural("0")

        # Создаем копию делимого
        dividend = Natural("0")
        dividend.digits = num1.digits.copy()
        result_digits = []

        # Обрабатываем каждую цифру делимого
        temp_number = Natural("0")
        temp_number.digits = []

        # Выполняем деление "столбиком"
        for d in dividend.digits:
            # Добавляем текущую цифру к временному числу
            temp_number.digits = temp_number.digits + [d]
            
            # Убираем ведущие нули
            while len(temp_number.digits) > 1 and temp_number.digits[0] == 0:
                temp_number.digits.pop(0)

            # Находим цифру частного
            quotient_digit = 0
            while NaturalOperations.COM_NN_D(temp_number, num2) != 1:
                temp_number = NaturalOperations.SUB_NN_N(temp_number, num2)
                quotient_digit += 1

            result_digits.append(quotient_digit)

        # Убираем ведущие нули результата
        while len(result_digits) > 1 and result_digits[0] == 0:
            result_digits.pop(0)

        result = Natural("0")
        result.digits = result_digits
        return result

    @staticmethod
    def MOD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Остаток от деления двух натуральных чисел
        """
        # Проверка деления на ноль
        if not num2.digits or num2.digits == [0]:
            raise ValueError("Division by zero")
            
        # Если первое число меньше второго, остаток равен первому числу
        if NaturalOperations.COM_NN_D(num1, num2) == 1:
            return num1

        # Находим частное от деления
        quotient = NaturalOperations.DIV_NN_N(num1, num2)
        
        # Вычисляем остаток как разность делимого и произведения делителя на частное
        reminder = NaturalOperations.SUB_NDN_N(num1, num2, quotient)
        return reminder

    @staticmethod
    def GCF_NN_N(a: Natural, b: Natural) -> Natural:
        """
        Нахождение НОД двух натуральных чисел
        """
        if NaturalOperations.NZER_N_B(a) == "нет" or NaturalOperations.NZER_N_B(b) == "нет":
            raise ValueError("Numbers must be non-zero")

        # Быстрая проверка равенства
        if a.digits == b.digits:
            return a
        
        # Реализация алгоритма Евклида без копий
        while NaturalOperations.NZER_N_B(b) == "да":
            if NaturalOperations.COM_NN_D(a, b) == 2:  # a > b
                a = NaturalOperations.MOD_NN_N(a, b)
            else:
                b = NaturalOperations.MOD_NN_N(b, a)

            # Если одно из чисел стало нулем
            if NaturalOperations.NZER_N_B(a) == "нет":
                return b
        
        return a

    @staticmethod
    def LCM_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Нахождение НОК двух натуральных чисел
        """
        if NaturalOperations.NZER_N_B(num1) == "нет" or NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Numbers must be non-zero")
            
        # Находим произведение чисел
        product = NaturalOperations.MUL_NN_N(num1, num2)
        
        # Находим НОД
        gcd = NaturalOperations.GCF_NN_N(num1, num2)
        
        # НОК = произведение / НОД
        return NaturalOperations.DIV_NN_N(product, gcd)