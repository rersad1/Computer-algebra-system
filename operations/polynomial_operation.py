from classes import *
from operations.rational_operations import RationalOperations
from operations.integer_operations import IntegerOperations
from operations.natural_operations import NaturalOperations

class PolynomialOperations:
    @staticmethod
    def ADD_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Сложение двух многочленов.
        """
        result = Polynomial()

        # Копируем первый многочлен в результат
        current1 = poly1.head
        while current1:
            result.add_term(current1.degree, current1.coefficient)
            current1 = current1.next

        # Добавляем члены второго многочлена
        current2 = poly2.head
        while current2:
            found = False
            current_result = result.head
            
            # Ищем член с такой же степенью в результате
            while current_result:
                if int(current_result.degree) == int(current2.degree):
                    # Складываем коэффициенты
                    new_coefficient = RationalOperations.ADD_QQ_Q(current_result.coefficient, current2.coefficient)
                    # Обновляем коэффициент в результате
                    current_result.coefficient = new_coefficient
                    found = True
                    break
                current_result = current_result.next
                
            # Если не нашли член с такой степенью - добавляем новый
            if not found:
                result.add_term(current2.degree, current2.coefficient)
                
            current2 = current2.next

        return result

    @staticmethod
    def SUB_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Вычитание двух многочленов через прямое вычитание коэффициентов.
        """
        result = Polynomial()

        # Копируем первый многочлен в результат
        current1 = poly1.head
        while current1:
            result.add_term(current1.degree, current1.coefficient)
            current1 = current1.next

        # Вычитаем члены второго многочлена
        current2 = poly2.head
        while current2:
            found = False
            current_result = result.head
            
            # Ищем член с такой же степенью в результате
            while current_result:
                if int(current_result.degree) == int(current2.degree):
                    # Вычитаем коэффициенты используя SUB_QQ_Q
                    new_coefficient = RationalOperations.SUB_QQ_Q(current_result.coefficient, current2.coefficient)
                    # Обновляем коэффициент в результате
                    current_result.coefficient = new_coefficient
                    found = True
                    break
                current_result = current_result.next
                
            # Если не нашли член с такой степенью - добавляем новый с противоположным знаком
            if not found:
                neg_coef = Rational(
                    IntegerOperations.MUL_ZM_Z(current2.coefficient.numerator),
                    current2.coefficient.denominator
                )
                result.add_term(current2.degree, neg_coef)
                
            current2 = current2.next

        return result

    @staticmethod
    def MUL_PQ_P(poly: Polynomial, q: Rational) -> Polynomial:
        """
        Умножение многочлена на рациональное число.
        """
        result = Polynomial()
        current = poly.head
        
        while current:
            # Проверяем, что числитель коэффициента не равен 0
            if int(current.coefficient.numerator) == 0:
                current = current.next
                continue
                
            # Умножаем коэффициент каждого одночлена на рациональное число
            # Сохраняем оригинальный коэффициент без создания нового
            multiplied_coeff = RationalOperations.MUL_QQ_Q(current.coefficient, q)
            multiplied_coeff = RationalOperations.RED_Q_Q(multiplied_coeff)
            # Добавляем результат умножения в новый многочлен
            result.add_term(current.degree, multiplied_coeff)
            current = current.next

        return result

    @staticmethod
    def MUL_Pxk_P(poly: Polynomial, k: Natural) -> Polynomial: # проверено
        """
        Умножение многочлена на x^k.

        :param poly: Многочлен, который нужно умножить.
        :param k: Натуральное число или 0, степень, на которую нужно умножить.
        :return: Новый многочлен, результат умножения.
        """
        result = Polynomial()

        current = poly.head

        # Проходим по всем одночленам в многочлене
        while current:
            # Увеличиваем степень на k
            new_degree = Natural(str(int(current.degree) + int(k)))

            # Добавляем одночлен с новой степенью в новый многочлен
            result.add_term(new_degree, current.coefficient)

            # Переходим к следующему одночлену
            current = current.next

        return result

    @staticmethod
    def LED_P_Q(poly: Polynomial) -> Rational:
        """
        Возвращает старший коэффициент многочлена.

        :param poly: Многочлен, для которого необходимо найти старший коэффициент.
        :return: Старший коэффициент многочлена.
        """
        current = poly.head
        max_degree = None
        leading_coefficient = None

        # Перебираем все одночлены многочлена
        while current:
            if max_degree is None or int(current.degree) > int(max_degree):
                max_degree = current.degree
                leading_coefficient = current.coefficient
            current = current.next

        return leading_coefficient

    @staticmethod
    def DEG_P_N(poly: Polynomial) -> Natural: # проверено
        """
        Возвращает степень многочлена.

        :param poly: Многочлен, для которого необходимо найти степень.
        :return: Степень многочлена (Natural).
        """
        current = poly.head
        max_degree = None

        # Перебираем все одночлены многочлена
        while current:
            if max_degree is None or int(current.degree) > int(max_degree):
                max_degree = current.degree
            current = current.next

        return max_degree

    @staticmethod
    def FAC_P_Q(poly: Polynomial) -> Rational:
        """
        Находит НОД числителей и НОК знаменателей коэффициентов многочлена.

        :param poly: Многочлен
        :return: Кортеж (НОД числителей, НОК знаменателей)
        """
        # Проверяем, не является ли многочлен нулевым
        if NaturalOperations.NZER_N_B(PolynomialOperations.DEG_P_N(poly)) == "нет":
            return Natural("1"), Natural("1")
            
        numerators = []
        denominators = []
        current = poly.head
        
        # Собираем числители и знаменатели
        while current:
            if int(current.coefficient.numerator) != 0:
                # Обрабатываем числитель
                num = IntegerOperations.ABS_Z_N(current.coefficient.numerator) 
                numerators.append(num)
                
                # Обрабатываем знаменатель
                denominators.append(current.coefficient.denominator)
                
            current = current.next

        # Находим НОД числителей
        gcd_result = numerators[0]
        for num in numerators[1:]:
            gcd_result = NaturalOperations.GCF_NN_N(gcd_result, num)

        # Находим НОК знаменателей
        lcm_result = denominators[0]
        for den in denominators[1:]:
            lcm_result = NaturalOperations.LCM_NN_N(lcm_result, den)

        answer = Rational(gcd_result, lcm_result)    
        return answer

    @staticmethod
    def MUL_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Умножение двух многочленов.
        """
        result_poly = Polynomial()

        # Проходим по всем одночленам первого многочлена
        current1 = poly1.head
        while current1:
            # Проходим по всем одночленам второго многочлена
            current2 = poly2.head
            while current2:
                # Умножаем коэффициенты
                new_coeff = RationalOperations.MUL_QQ_Q(current1.coefficient, current2.coefficient)

                # Складываем степени
                new_degree = NaturalOperations.ADD_NN_N(current1.degree, current2.degree)

                # Создаем новый одночлен сразу с нужным коэффициентом
                temp_poly = Polynomial()
                temp_poly.add_term(new_degree, new_coeff)

                # Добавляем результат в итоговый многочлен
                result_poly = PolynomialOperations.ADD_PP_P(result_poly, temp_poly)

                current2 = current2.next
            current1 = current1.next

        return result_poly

    @staticmethod
    def DIV_PP_P(dividend: Polynomial, divisor: Polynomial) -> Polynomial:
        """
        Деление многочлена на многочлен без остатка.
        """
        quotient = Polynomial()
        temp_dividend = dividend
        temp_count = 0
        while temp_dividend.head and int(temp_dividend.head.degree) >= int(divisor.head.degree):
            # Получение старших членов делимого и делителя
            dividend_current = temp_dividend.head
            while dividend_current.next:
                dividend_current = dividend_current.next

            divisor_current = divisor.head
            while divisor_current.next:
                divisor_current = divisor_current.next

            if int(dividend_current.degree) >= int(divisor_current.degree):
                # Вычисляем коэффициент и разность степеней
                quotient_coeff = RationalOperations.DIV_QQ_Q(dividend_current.coefficient, divisor_current.coefficient)
                degree_diff = NaturalOperations.SUB_NN_N(dividend_current.degree, divisor_current.degree)
                quotient.add_term(degree_diff, quotient_coeff)

                # Умножаем делитель на текущий член частного
                temp_poly = PolynomialOperations.MUL_Pxk_P(divisor, degree_diff)
                temp_poly = PolynomialOperations.MUL_PQ_P(temp_poly, quotient_coeff)

                temp_dividend = PolynomialOperations.SUB_PP_P(temp_dividend, temp_poly)

            temp_count += 1
            # Если после вычитания `temp_dividend` стал нулем, выходим из цикла
            if not temp_dividend.head or int(temp_dividend.head.degree) < int(divisor.head.degree) or temp_count > 100:
                break

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
        # Вычисляем вычитаемое
        deductible = PolynomialOperations.MUL_PP_P(quotient, divisor)   
        # Получаем остаток    
        remainder = PolynomialOperations.SUB_PP_P(dividend, deductible)
        
        return remainder

    @staticmethod
    def GCF_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Находит наибольший общий делитель (НОД) двух многочленов.

        :param poly1: Первый многочлен.
        :param poly2: Второй многочлен.
        :return: НОД двух многочленов.
        """
        # Применяем алгоритм Евклида для многочленов
        coefficient = PolynomialOperations.DEG_P_N(poly2)
        string_answer = NaturalOperations.NZER_N_B(coefficient)
        counter = 0
        while string_answer == "да":
            # Находим остаток от деления poly1 на poly2
            remainder = PolynomialOperations.MOD_PP_P(poly1, poly2)
            # Обновляем poly1 и poly2 для следующего шага алгоритма
            poly1, poly2 = poly2, remainder
            print(poly1, poly2)
            coefficient = PolynomialOperations.DEG_P_N(poly2)
            string_answer = NaturalOperations.NZER_N_B(coefficient)
            if counter > 100:
                break
        return poly1  # НОД - это последний ненулевой остаток

    @staticmethod
    def DER_P_P(poly: Polynomial) -> Polynomial:
        """
        Находит производную многочлена.

        :param poly: Многочлен.
        :return: Производная многочлена.
        """
        derivative = Polynomial()
        current = poly.head.next  # Начинаем с первого одночлена

        while current:
            degree = current.degree
            coefficient = current.coefficient

            # Если степень больше 0, вычисляем производную одночлена
            if int(degree) > 0:
                # Производная одночлена a * x^n равна a * n * x^(n-1)
                degree_as_rat = RationalOperations.TRANS_Z_Q(IntegerOperations.TRANS_N_Z(degree))
                new_coefficient = RationalOperations.MUL_QQ_Q(coefficient, degree_as_rat)
                new_degree = Natural(str(int(degree) - 1))
                derivative.add_term(new_degree, new_coefficient)

            current = current.next

        return derivative

    @staticmethod
    def NMR_P_P(poly: Polynomial) -> Polynomial:
        """
        Преобразование многочлена: кратные корни в простые.

        :param poly: Многочлен.
        :return: Многочлен с простыми корнями.
        """
        # Вычисляем производную многочлена
        derivative = PolynomialOperations.DER_P_P(poly)

        # Находим НОД (наибольший общий делитель) между многочленом и его производной
        gcd_poly = PolynomialOperations.GCF_PP_P(poly, derivative)

        # Разделим исходный многочлен на НОД, чтобы избавиться от кратных корней
        result_poly = PolynomialOperations.DIV_PP_P(poly, gcd_poly)

        return result_poly

