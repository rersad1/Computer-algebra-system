from classes import *  # Импорт всех базовых классов, таких как Polynomial, Rational, Integer и другие
from operations.rational_operations import RationalOperations  # Импорт операций с рациональными числами
from operations.integer_operations import IntegerOperations  # Импорт операций с целыми числами
from operations.natural_operations import NaturalOperations  # Импорт операций с натуральными числами


class PolynomialOperations:
    @staticmethod
    def ADD_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """Сложение двух многочленов."""
        result = Polynomial()  # Создаем новый пустой многочлен для результата

        # Добавляем члены из первого многочлена
        for degree, coeff in poly1.terms.items():
            result.add_term(Natural(str(degree)), coeff)  # Добавляем каждый член в результирующий многочлен

        # Добавляем члены из второго многочлена
        for degree, coeff in poly2.terms.items():
            if degree in result.terms:  # Если степень уже есть в результате
                new_coeff = RationalOperations.ADD_QQ_Q(result.terms[degree], coeff)  # Складываем коэффициенты
                result.add_term(Natural(str(degree)), new_coeff)  # Обновляем коэффициент
            else:  # Если степени нет в результате
                result.add_term(Natural(str(degree)), coeff)  # Просто добавляем член

        return result  # Возвращаем результирующий многочлен

    @staticmethod
    def SUB_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """Вычитание двух многочленов."""
        result = Polynomial()  # Создаем новый пустой многочлен для результата

        # Копируем члены из первого многочлена
        for degree, coeff in poly1.terms.items():
            result.add_term(Natural(str(degree)), coeff)  # Добавляем каждый член

        # Вычитаем члены второго многочлена
        for degree, coeff in poly2.terms.items():
            neg_coeff = Rational(  # Инвертируем коэффициент
                IntegerOperations.MUL_ZM_Z(coeff.numerator),
                coeff.denominator
            )
            if degree in result.terms:  # Если степень уже есть в результате
                new_coeff = RationalOperations.ADD_QQ_Q(result.terms[degree],
                                                        neg_coeff)  # Складываем с отрицательным коэффициентом
                result.add_term(Natural(str(degree)), new_coeff)  # Обновляем коэффициент
            else:  # Если степени нет в результате
                result.add_term(Natural(str(degree)), neg_coeff)  # Добавляем отрицательный коэффициент

        return result  # Возвращаем результирующий многочлен

    @staticmethod
    def MUL_PQ_P(poly: Polynomial, q: Rational) -> Polynomial:
        """Умножение многочлена на рациональное число."""
        result = Polynomial()  # Создаем новый пустой многочлен

        for degree, coeff in poly.terms.items():  # Проходим по всем членам многочлена
            new_coeff = RationalOperations.MUL_QQ_Q(coeff, q)  # Умножаем коэффициент на рациональное число
            result.add_term(Natural(str(degree)), new_coeff)  # Добавляем результат в многочлен

        return result  # Возвращаем результирующий многочлен

    @staticmethod
    def MUL_Pxk_P(poly: Polynomial, k: Natural) -> Polynomial:
        """Умножение многочлена на x^k."""
        result = Polynomial()  # Создаем новый пустой многочлен
        k_int = int(k)  # Преобразуем натуральное число в целое

        for degree, coeff in poly.terms.items():  # Проходим по всем членам многочлена
            new_degree = Natural(str(degree + k_int))  # Увеличиваем степень каждого члена на k
            result.add_term(new_degree, coeff)  # Добавляем член с новой степенью в результат

        return result  # Возвращаем результирующий многочлен

    @staticmethod
    def LED_P_Q(poly: Polynomial) -> Rational:
        """Возвращает старший коэффициент многочлена."""
        return poly.get_leading_coeff()  # Получаем и возвращаем старший коэффициент

    @staticmethod
    def DEG_P_N(poly: Polynomial) -> Natural:
        """Возвращает степень многочлена."""
        return poly.get_degree()  # Получаем и возвращаем степень многочлена

    @staticmethod
    def FAC_P_Q(poly: Polynomial) -> Rational:
        """Находит НОД числителей и НОК знаменателей коэффициентов."""
        if not poly.terms:  # Если многочлен пустой
            return Rational(Integer("1"), Natural("1"))  # Возвращаем тривиальный множитель

        numerators = []  # Список числителей
        denominators = []  # Список знаменателей

        for coeff in poly.terms.values():  # Проходим по всем коэффициентам
            if int(coeff.numerator) != 0:  # Если числитель не равен нулю
                num = IntegerOperations.ABS_Z_N(coeff.numerator)  # Берем модуль числителя
                numerators.append(num)  # Добавляем в список числителей
                denominators.append(coeff.denominator)  # Добавляем знаменатель в список

        if not numerators:  # Если числители отсутствуют
            return Rational(Integer("1"), Natural("1"))  # Возвращаем тривиальный множитель

        gcd_result = numerators[0]  # Инициализируем НОД первым числителем
        for num in numerators[1:]:  # Вычисляем НОД числителей
            gcd_result = NaturalOperations.GCF_NN_N(gcd_result, num)

        lcm_result = denominators[0]  # Инициализируем НОК первым знаменателем
        for den in denominators[1:]:  # Вычисляем НОК знаменателей
            lcm_result = NaturalOperations.LCM_NN_N(lcm_result, den)

        return Rational(Integer(str(gcd_result)), lcm_result)  # Возвращаем НОД и НОК как рациональное число

    @staticmethod
    def MUL_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Умножение двух многочленов при словарной реализации.
        """
        result_poly = Polynomial()

        # Проходим по всем членам первого многочлена
        for deg1, coeff1 in poly1.terms.items():
            # Проходим по всем членам второго многочлена
            for deg2, coeff2 in poly2.terms.items():
                # Умножаем коэффициенты
                new_coeff = RationalOperations.MUL_QQ_Q(coeff1, coeff2)

                # Складываем степени
                new_degree = deg1 + deg2

                # Если в результате уже есть член с такой степенью, складываем коэффициенты
                if new_degree in result_poly.terms:
                    existing_coeff = result_poly.terms[new_degree]
                    new_coeff = RationalOperations.ADD_QQ_Q(existing_coeff, new_coeff)

                # Добавляем новый член в результат
                result_poly.add_term(Natural(str(new_degree)), new_coeff)

        return result_poly

    @staticmethod
    def DIV_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Деление двух многочленов poly1 и poly2. Возвращает только частное.
        """
        if str(poly2) == "0":
            raise ValueError("Делитель не может быть нулём.")

        # Создаем пустой полином для частного
        quotient = Polynomial()

        # Создаем копию делимого для работы
        remainder = Polynomial()
        remainder.terms = poly1.terms.copy()

        # Получаем степень и коэффициент делителя
        divisor_degree = poly2.get_degree()
        divisor_lead_coeff = poly2.getCoeff(divisor_degree)

        while remainder.terms:
            # Сравниваем степени используя Natural
            dividend_degree = remainder.get_degree()
            comparison = NaturalOperations.COM_NN_D(dividend_degree, divisor_degree)

            if comparison == 1:  # если степень делимого меньше степени делителя
                break

            # Вычисляем степень и коэффициент для нового члена частного
            degree_diff = NaturalOperations.SUB_NN_N(dividend_degree, divisor_degree)
            coeff = RationalOperations.DIV_QQ_Q(
                remainder.getCoeff(dividend_degree),
                divisor_lead_coeff
            )

            # Добавляем член в частное
            quotient.add_term(degree_diff, coeff)

            # Создаем временный полином для вычитания
            temp = Polynomial()
            temp.add_term(degree_diff, coeff)
            temp = PolynomialOperations.MUL_PP_P(poly2, temp)

            # Вычитаем из остатка
            remainder = PolynomialOperations.SUB_PP_P(remainder, temp)

            # Очищаем нулевые члены
            remainder.terms = {k:v for k,v in remainder.terms.items()
                            if int(v.numerator) != 0}

        return quotient


    @staticmethod
    def MOD_PP_P(dividend: Polynomial, divisor: Polynomial) -> Polynomial:
        """
        Остаток от деления многочлена на многочлен при делении с остатком.

        :param dividend: Многочлен-делимое.
        :param divisor: Многочлен-делитель.
        :return: Остаток от деления.
        """
        # Вычисляем частное
        quotient = PolynomialOperations.DIV_PP_P(dividend, divisor)
        print(quotient)
        # Вычисляем вычитаемое
        deductible = PolynomialOperations.MUL_PP_P(quotient, divisor)
        # Получаем остаток
        remainder = PolynomialOperations.SUB_PP_P(dividend, deductible)
        return remainder

    @staticmethod
    def GCF_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Поиск НОД двух многочленов на основе алгоритма Евклида.
        """
        pln1 = create_polynomial(str(poly1))
        pln2 = create_polynomial(str(poly2))

        if int(pln1.get_degree()) < int(pln2.get_degree()):
            pln1, pln2 = pln2, pln1

        if str(pln2) == "0":
            return pln1

        print("\nНачало поиска НОД:")
        while True:
            remainder = PolynomialOperations.MOD_PP_P(pln1, pln2)
            print(f"Остаток: {remainder}")

            if str(remainder) == "0":
                break

            # Находим множитель остатка и нормализуем
            fac = PolynomialOperations.FAC_P_Q(remainder)
            if int(fac.numerator) != 0:
                remainder = PolynomialOperations.MUL_PQ_P(remainder,
                                                        Rational(Integer(str(fac.denominator)),
                                                                Natural(str(fac.numerator))))

            pln1 = pln2
            pln2 = remainder

            if int(remainder.get_degree()) == 0:
                break

        # Находим общий множитель результата
        fac = PolynomialOperations.FAC_P_Q(pln2)

        # Приводим результат к нормализованному виду через умножение на полученный множитель
        if int(fac.numerator) != 0:
            pln2 = PolynomialOperations.MUL_PQ_P(pln2,
                                                Rational(Integer(str(fac.denominator)),
                                                        Natural(str(fac.numerator))))

        # Делаем старший коэффициент положительным
        lead_coeff = pln2.get_leading_coeff()
        if int(lead_coeff.numerator) < 0:
            pln2 = PolynomialOperations.MUL_PQ_P(pln2,
                                                Rational(Integer("-1"), Natural("1")))

        print(f"\nРезультат НОД: {pln2}")
        return pln2

    @staticmethod
    def DER_P_P(poly: Polynomial) -> Polynomial:
        """
        Вычисляет производную многочлена.

        :param poly: Исходный многочлен
        :return: Многочлен-производная
        """
        result = Polynomial()

        for degree, coeff in poly.terms.items():
            if degree > 0:  # Производная константы равна 0
                # Умножаем коэффициент на степень
                new_coeff = RationalOperations.MUL_QQ_Q(
                    coeff,
                    Rational(Integer(str(degree)), Natural("1"))
                )
                # Уменьшаем степень на 1
                result.add_term(Natural(str(degree - 1)), new_coeff)

        return result

    @staticmethod
    def NMR_P_P(poly: Polynomial) -> Polynomial:
        """
        Преобразование многочлена: кратные корни в простые.

        :param poly: Многочлен
        :return: Многочлен с простыми корнями
        """
        # Если многочлен нулевой или константа
        if len(poly.terms) <= 1:
            return poly

        # Вычисляем производную многочлена
        derivative = PolynomialOperations.DER_P_P(poly)

        # Находим НОД многочлена и его производной
        gcd_poly = PolynomialOperations.GCF_PP_P(poly, derivative)

        # Если НОД равен константе, значит кратных корней нет
        if int(gcd_poly.get_degree()) == 0:
            return poly

        # Делим исходный многочлен на НОД
        result = PolynomialOperations.DIV_PP_P(poly, gcd_poly)
        return result
