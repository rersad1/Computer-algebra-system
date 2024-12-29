from classes import *
from operations.natural_operations import NaturalOperations
from operations.integer_operations import IntegerOperations

class RationalOperations:
    @staticmethod
    def RED_Q_Q(fraction: Rational) -> Rational:
        """Оптимизированное сокращение дроби"""
        # Быстрая проверка на ноль
        if fraction.numerator.digits == [0]:
            return Rational(Integer("0"), Natural("1"))
            
        # Находим НОД напрямую, без преобразования типов
        abs_numerator = IntegerOperations.ABS_Z_N(fraction.numerator)
        gcd = NaturalOperations.GCF_NN_N(abs_numerator, fraction.denominator)
        # Если НОД == 1, дробь несократима
        if gcd.digits == [1]:
            return fraction
            
        # Делим числитель и знаменатель на НОД
        reduced_denominator = NaturalOperations.DIV_NN_N(fraction.denominator, gcd)
        
        # Сохраняем знак числителя
        is_negative = fraction.numerator.is_negative
        reduced_numerator_natural = NaturalOperations.DIV_NN_N(abs_numerator, gcd)
        
        # Создаем новый числитель с правильным знаком
        reduced_numerator = Integer("0")
        reduced_numerator.digits = reduced_numerator_natural.digits
        reduced_numerator.is_negative = is_negative
        
        return Rational(reduced_numerator, reduced_denominator)

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
        """Оптимизированное сложение рациональных чисел"""
        if fraction1.denominator == fraction2.denominator:
            new_numerator = IntegerOperations.ADD_ZZ_Z(fraction1.numerator, fraction2.numerator)
            result = RationalOperations.RED_Q_Q(Rational(new_numerator, fraction1.denominator))
            return result
        
        # Находим НОК знаменателей
        lcm = NaturalOperations.LCM_NN_N(fraction1.denominator, fraction2.denominator)
        
        # Вычисляем множители для числителей
        mult1 = NaturalOperations.DIV_NN_N(lcm, fraction1.denominator)
        mult2 = NaturalOperations.DIV_NN_N(lcm, fraction2.denominator)
        
        # Умножаем числители на соответствующие множители
        new_num1 = IntegerOperations.MUL_ZZ_Z(fraction1.numerator, Integer(str(mult1)))
        new_num2 = IntegerOperations.MUL_ZZ_Z(fraction2.numerator, Integer(str(mult2)))
        
        # Складываем числители
        result_num = IntegerOperations.ADD_ZZ_Z(new_num1, new_num2)
        result = RationalOperations.RED_Q_Q(Rational(result_num, lcm))
        return result

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
        """Оптимизированное умножение рациональных чисел"""
        # Прямое умножение числителей и знаменателей
        new_numerator = IntegerOperations.MUL_ZZ_Z(fraction1.numerator, fraction2.numerator)
        new_denominator = NaturalOperations.MUL_NN_N(fraction1.denominator, fraction2.denominator)
        result = RationalOperations.RED_Q_Q(Rational(new_numerator, new_denominator))
        return result

    @staticmethod
    def DIV_QQ_Q(fraction1: Rational, fraction2: Rational) -> Rational:
        """Оптимизированное деление рациональных чисел"""
        if fraction2.numerator == Integer("0"):
            raise ValueError("Деление на ноль")
            
        # Вычисляем новый числитель и знаменатель
        new_numerator = IntegerOperations.MUL_ZZ_Z(fraction1.numerator, 
                                                Integer(str(fraction2.denominator)))
        new_denominator = IntegerOperations.MUL_ZZ_Z(Integer(str(fraction1.denominator)), 
                                                    fraction2.numerator)
        
        # Определяем, должен ли быть результат отрицательным
        result_is_negative = new_denominator.is_negative
        
        # Если знаменатель отрицательный, делаем его положительным и меняем знак числителя
        if result_is_negative:
            new_denominator = IntegerOperations.MUL_ZM_Z(new_denominator)  # Делаем знаменатель положительным
            new_numerator = IntegerOperations.MUL_ZM_Z(new_numerator)      # Инвертируем знак числителя
        
        result = RationalOperations.RED_Q_Q(Rational(new_numerator, new_denominator))
        return result