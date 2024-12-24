from classes import *
from operations.natural_operations import NaturalOperations
from operations.integer_operations import IntegerOperations

class RationalOperations:
    @staticmethod
    def RED_Q_Q(fraction):
        """
        Сокращение дроби.
        """
        if fraction.numerator == Integer("0"):
            return Rational(fraction.numerator, Natural("1"))
        is_negative_numerator = IntegerOperations.POZ_Z_D(fraction.numerator)
        # Применяем ABS_Z_N для числителя и знаменателя
        abs_numerator = IntegerOperations.ABS_Z_N(fraction.numerator)
        abs_denominator = IntegerOperations.ABS_Z_N(fraction.denominator)

        # Находим наибольший общий делитель (gcd) между абсолютными значениями
        gcd = NaturalOperations.GCF_NN_N(abs_numerator, abs_denominator)

        # Получаем сокращенный числитель и знаменатель
        reduced_numerator = NaturalOperations.DIV_NN_N(abs_numerator, gcd)
        reduced_denominator = NaturalOperations.DIV_NN_N(abs_denominator, gcd)

        # Создаем сокращенную дробь с правильным знаком
        if is_negative_numerator == 1:
            reduced_fraction = Rational(IntegerOperations.MUL_ZM_Z(Integer(str(reduced_numerator))), reduced_denominator)
        else:
            reduced_fraction = Rational(Integer(str(reduced_numerator)), Natural(str(reduced_denominator)))

        return reduced_fraction

    @staticmethod
    def INT_Q_B(fraction: Rational) -> str: # проверено тестами работает
        """
        Проверка, является ли рациональное число целым.

        :param fraction: Рациональное число, представленное объектом Rational.
        :return: "да", если число целое, и "нет", если нет.
        """
        # Получаем числитель и знаменатель
        numerator = fraction.numerator
        denominator = fraction.denominator

        # Проверка, является ли знаменатель 1
        if int(denominator) == 1:
            return "да"

        # Если числитель делится на знаменатель без остатка
        if int(numerator) % int(denominator) == 0:
            return "да"

        return "нет"

    @staticmethod
    def TRANS_Z_Q(integer: Integer) -> Rational: # протестировано
        """
        Преобразует целое число в рациональное (дробь).

        :param integer: Целое число (Integer).
        :return: Рациональное число (Rational), представляющее целое число как дробь.
        """
        # Создаем рациональное число с числителем равным целому числу и знаменателем равным 1
        return Rational(integer, Natural("1"))

    @staticmethod
    def TRANS_Q_Z(rational: Rational) -> Integer: # протестировано
        """
        Преобразует сокращенную дробь в целое число, если знаменатель равен 1.

        :param rational: Рациональное число (Rational).
        :return: Целое число (Integer), если знаменатель равен 1, иначе выбрасывает исключение.
        :raises ValueError: Если знаменатель не равен 1.
        """
        # Проверяем, что знаменатель равен 1
        if int(rational.denominator) != 1:
            raise ValueError("Рациональное число не является целым числом, так как знаменатель не равен 1.")

        # Возвращаем числитель как целое число
        return rational.numerator

    @staticmethod
    def ADD_QQ_Q(fraction1: Rational, fraction2: Rational) -> Rational:
        """
        Сложение двух дробей.
        :param fraction1: Первая дробь (Rational).
        :param fraction2: Вторая дробь (Rational).
        :return: Сумма двух дробей (Rational).
        """
        # Находим наименьшее общее кратное (LCM) знаменателей
        lcm_denominator = NaturalOperations.LCM_NN_N(fraction1.denominator, fraction2.denominator)

        # Находим числители для новых дробей
        new_numerator1 = IntegerOperations.MUL_ZZ_Z(fraction1.numerator, Integer(str(NaturalOperations.DIV_NN_N(lcm_denominator, fraction1.denominator))))
        new_numerator2 = IntegerOperations.MUL_ZZ_Z(fraction2.numerator, Integer(str(NaturalOperations.DIV_NN_N(lcm_denominator, fraction2.denominator))))
        
        # Складываем числители
        result_numerator = IntegerOperations.ADD_ZZ_Z(new_numerator1, new_numerator2)

        # Возвращаем результат как новую дробь с общим знаменателем
        final = RationalOperations.RED_Q_Q(Rational(result_numerator, lcm_denominator))
        return final

    @staticmethod
    def SUB_QQ_Q(fraction1: Rational, fraction2: Rational) -> Rational: #????
        """
        Вычитание двух рациональных чисел.
        fraction1 и fraction2 — экземпляры класса Rational (числитель, знаменатель).

        :return: результат вычитания в виде новой рациональной дроби.
        """
        if fraction1.denominator == fraction2.denominator:
            new_numerator = IntegerOperations.SUB_ZZ_Z(fraction1.numerator, fraction2.numerator)
            answer = RationalOperations.RED_Q_Q(Rational(new_numerator, fraction1.denominator))
            return answer
        
        # Находим НОК (наименьшее общее кратное) знаменателей
        lcm_denominator = NaturalOperations.LCM_NN_N(fraction1.denominator, fraction2.denominator)

        # Находим коэффициент для числителей
        new_numerator1 = IntegerOperations.MUL_ZZ_Z(fraction1.numerator, Integer(str(NaturalOperations.DIV_NN_N(lcm_denominator, fraction1.denominator))))
        new_numerator2 = IntegerOperations.MUL_ZZ_Z(fraction2.numerator, Integer(str(NaturalOperations.DIV_NN_N(lcm_denominator, fraction2.denominator))))

        # Вычитаем числители
        new_numerator = IntegerOperations.SUB_ZZ_Z(new_numerator1, new_numerator2)
        # Сокращаем дробь
        answer = RationalOperations.RED_Q_Q(Rational(new_numerator, lcm_denominator))

        return answer

    @staticmethod
    def MUL_QQ_Q(fraction1: Rational, fraction2: Rational) -> Rational:
        """
        Умножение двух рациональных чисел.
        Корректно обрабатывает знаки при умножении рациональных чисел.
        """
        # Умножаем числители с сохранением знаков
        new_numerator = IntegerOperations.MUL_ZZ_Z(fraction1.numerator, fraction2.numerator)
        
        # Умножаем знаменатели (всегда положительные)
        new_denominator = NaturalOperations.MUL_NN_N(fraction1.denominator, fraction2.denominator)
        result = Rational(new_numerator, new_denominator)
        return RationalOperations.RED_Q_Q(result)

    @staticmethod
    def DIV_QQ_Q(fraction1: Rational, fraction2: Rational) -> Rational:
        """
        Деление двух рациональных чисел.
        fraction1 и fraction2 — экземпляры класса Rational (числитель, знаменатель).

        :return: результат деления в виде новой рациональной дроби.
        :raises ValueError: если знаменатель второй дроби равен нулю.
        """
        # Проверяем, что знаменатель второй дроби не равен нулю
        if fraction2.numerator == Natural('0'):
            raise ValueError("Нельзя делить на ноль.")

        # Инвертируем вторую дробь
        inverted_fraction2_numerator = fraction2.denominator
        inverted_fraction2_denominator = fraction2.numerator
        
        # Определяем знаки числителей
        is_negative_numerator1 = IntegerOperations.POZ_Z_D(fraction1.numerator)
        is_negative_numerator2 = IntegerOperations.POZ_Z_D(fraction2.numerator)
        
        # Умножаем числители и знаменатели
        new_numerator = IntegerOperations.MUL_ZZ_Z(fraction1.numerator, Integer(str(inverted_fraction2_numerator)))
        new_denominator = IntegerOperations.MUL_ZZ_Z(Integer(str(fraction1.denominator)), inverted_fraction2_denominator)
        
        # Определяем знак результата:
        # Если оба числа отрицательные или оба положительные - результат положительный
        # Если знаки разные - результат отрицательный
        if (is_negative_numerator1 == 1 and is_negative_numerator2 == 1) or (is_negative_numerator1 == 2 and is_negative_numerator2 == 2):
            # Оба отрицательные или оба положительные - результат положительный
            new_numerator = IntegerOperations.ABS_Z_N(new_numerator)
            new_denominator = IntegerOperations.ABS_Z_N(new_denominator)
        elif is_negative_numerator1 == 0:
            # Если одно из чисел ноль
            new_numerator = Integer("0")
        else:
            # Знаки разные - результат отрицательный
            new_numerator = IntegerOperations.ABS_Z_N(new_numerator)
            new_numerator = IntegerOperations.MUL_ZM_Z(Integer(str(new_numerator)))
            new_denominator = IntegerOperations.ABS_Z_N(new_denominator)
        # Возвращаем результат как новую дробь
        answer = RationalOperations.RED_Q_Q(Rational(Integer(str(new_numerator)), Natural(str(new_denominator))))
        return answer
    