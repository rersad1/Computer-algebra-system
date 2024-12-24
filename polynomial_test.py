import unittest
import time
from classes import *
from operations.rational_operations import RationalOperations
from operations.polynomial_operation import PolynomialOperations


class TestPolynomialOperations(unittest.TestCase):

    def setUp(self):
        # Инициализация тестовых многочленов:
        self.poly1 = create_polynomial("3x^2+2x+1")
        self.poly2 = create_polynomial("4x^2+3x+2")
        self.poly3 = create_polynomial("5x^3+3x^2+x")

    def test_add_polynomials(self):
        result = PolynomialOperations.ADD_PP_P(self.poly1, self.poly3)
        expected = create_polynomial("5x^3+6x^2+3x+1")
        self.assertEqual(result, expected)

    def test_sub_polynomials(self):
        result = PolynomialOperations.SUB_PP_P(self.poly1, self.poly2)
        expected = create_polynomial("-x^2-x-1")
        self.assertEqual(result, expected)

    def test_multiply_polynomial_by_rational(self):
        q = Rational(Integer("2"), Natural("3"))  # 2/3
        result = PolynomialOperations.MUL_PQ_P(self.poly1, q)
        expected = create_polynomial("2x^2+(4/3)x+(2/3)")
        self.assertEqual(result, expected)

    def test_multiply_polynomial_by_xk(self):
        k = Natural("2")  # x^2
        result = PolynomialOperations.MUL_Pxk_P(self.poly1, k)
        expected = create_polynomial("3x^4+2x^3+x^2")
        self.assertEqual(result, expected)

    def test_derivative_polynomial(self):
        result = PolynomialOperations.DER_P_P(self.poly1)
        expected = create_polynomial("6x+2")
        self.assertEqual(result, expected)


    def test_large_polynomials_addition(self):
        # Генерация больших многочленов для сложения
        poly_large1 = create_polynomial(" + ".join([f"{i}x^{i}" for i in range(1000, 0, -1)]))
        poly_large2 = create_polynomial(" + ".join([f"{i}x^{i}" for i in range(500, 0, -1)]))

        start_time = time.time()
        result = PolynomialOperations.ADD_PP_P(poly_large1, poly_large2)
        end_time = time.time()

        print("Результат сложения больших многочленов:", str(result)[:100], "...")
        print("Время расчёта сложения:", end_time - start_time, "секунд")

    def test_large_polynomials_derivative(self):
        # Генерация больших многочленов для вычисления производной
        poly_large = create_polynomial(" + ".join([f"{i}x^{i}" for i in range(250, 0, -1)]))

        start_time = time.time()
        result = PolynomialOperations.DER_P_P(poly_large)
        end_time = time.time()

        print("Результат вычисления производной большого многочлена:", str(result)[:100], "...")
        print("Время расчёта производной:", end_time - start_time, "секунд")


if __name__ == '__main__':
    unittest.main()
