import unittest
import time
from operations.natural_operations import NaturalOperations
from classes import *

class TestNaturalOperations(unittest.TestCase):

    def setUp(self):
        """Инициализация данных для тестов."""
        self.num1 = Natural("12345")
        self.num2 = Natural("6789")
        self.num3 = Natural("12345")
        self.num4 = Natural("0")
        self.num5 = Natural("9876")
        self.num6 = Natural("100000")

        # Большие числа для бенчмарков
        self.large_num1 = Natural("123456789123456789123456789123456789")
        self.large_num2 = Natural("987654321987654321987654321987654321")

    def test_COM_NN_D(self):
        """Тестируем сравнение двух чисел."""
        # num1 > num2
        self.assertEqual(NaturalOperations.COM_NN_D(self.num1, self.num2), 2)
        # num1 < num2
        self.assertEqual(NaturalOperations.COM_NN_D(self.num2, self.num1), 1)
        # num1 == num3
        self.assertEqual(NaturalOperations.COM_NN_D(self.num1, self.num3), 0)

    def test_NZER_N_B(self):
        """Тестируем проверку на ноль."""
        # num4 == 0
        self.assertEqual(NaturalOperations.NZER_N_B(self.num4), "нет")
        # num1 != 0
        self.assertEqual(NaturalOperations.NZER_N_B(self.num1), "да")

    def test_ADD_1N_N(self):
        """Тестируем добавление 1 к числу."""
        # 12345 + 1 = 12346
        result = NaturalOperations.ADD_1N_N(self.num1)
        self.assertEqual(str(result), "12346")

    def test_ADD_NN_N(self):
        # Проверка метода сложения двух натуральных чисел
        num1 = Natural("123")
        num2 = Natural("456")
        expected = Natural("579")

        result = NaturalOperations.ADD_NN_N(num1, num2)
        self.assertEqual(str(result), str(expected))

    def test_SUB_NN_N(self):
        """Тестируем вычитание двух чисел."""
        # 12345 - 6789 = 5556
        result = NaturalOperations.SUB_NN_N(self.num1, self.num2)
        self.assertEqual(str(result), "5556")
        # Проверка на ошибку при вычитании большего из меньшего числа
        with self.assertRaises(ValueError):
            NaturalOperations.SUB_NN_N(self.num2, self.num1)

    def test_MUL_ND_N(self):
        """Тестируем умножение на цифру."""
        # 12345 * 3 = 37035
        result = NaturalOperations.MUL_ND_N(self.num1, 3)
        self.assertEqual(str(result), "37035")
        # Проверка на значение за пределами диапазона цифр
        with self.assertRaises(ValueError):
            NaturalOperations.MUL_ND_N(self.num1, 10)

    def test_MUL_Nk_N(self):
        """Тестируем умножение на 10^k."""
        # 12345 * 10^3 = 12345000
        result = NaturalOperations.MUL_Nk_N(self.num1, 3)
        self.assertEqual(str(result), "12345000")

    def test_MUL_NN_N(self):
        """Тестируем умножение двух чисел."""
        # 12345 * 6789 = 83810205
        result = NaturalOperations.MUL_NN_N(self.num1, self.num2)
        self.assertEqual(str(result), "83810205")

    def test_SUB_NDN_N(self):
        """Тестируем вычитание из числа, полученного умножением на цифру."""
        # 12345 - (6789 * 3) = 12345 - 20367 = -80322 (нельзя получить отрицательное число)
        with self.assertRaises(ValueError):
            NaturalOperations.SUB_NDN_N(self.num1, self.num2, 3)

    def test_DIV_NN_Dk(self):
        num1 = Natural("98765")
        num2 = Natural("12")

        k = 1
        expected = 8

        result = NaturalOperations.DIV_NN_Dk(num1, num2, k)
        self.assertEqual(result, expected)

    def test_DIV_NN_N(self):
        """Тестируем деление с остатком."""
        # 12345 / 6789 -> (1, 5556)
        quotient = NaturalOperations.DIV_NN_N(self.num1, self.num2)
        remainder = NaturalOperations.MOD_NN_N(self.num1, self.num2)
        self.assertEqual(str(quotient), "1")
        self.assertEqual(str(remainder), "5556")

    def test_MOD_NN_N(self):
        """Тестируем остаток от деления."""
        # 12345 % 6789 = 5556
        result = NaturalOperations.MOD_NN_N(self.num1, self.num2)
        self.assertEqual(str(result), "5556")

    def test_GCF_NN_N(self):
        """Тестируем наибольший общий делитель."""
        # НОД(12345, 6789)
        result = NaturalOperations.GCF_NN_N(self.num1, self.num2)
        self.assertEqual(str(result), "3")

    def test_LCM_NN_N(self):
        """Тестируем наименьшее общее кратное."""
        # НОК(12345, 6789)
        result = NaturalOperations.LCM_NN_N(self.num1, self.num2)
        self.assertEqual(str(result), "27936735")

    # Бенчмарки для больших чисел
    def test_benchmark_addition_large_numbers(self):
        """Бенчмарк: сложение двух больших чисел."""
        start_time = time.time()
        result = NaturalOperations.ADD_NN_N(self.large_num1, self.large_num2)
        end_time = time.time()
        print(f"Сложение двух натуральных чисел результат: {result} заняло {end_time - start_time:.6f} секунд.")

    def test_benchmark_multiplication_large_numbers(self):
        """Бенчмарк: умножение двух больших чисел."""
        start_time = time.time()
        result = NaturalOperations.MUL_NN_N(self.large_num1, self.large_num2)
        end_time = time.time()
        print(f"Умножение больших натуральных чисел: {result} заняло {end_time - start_time:.6f} секунд.")

    def test_benchmark_division_large_numbers(self):
        """Бенчмарк: деление двух больших чисел."""
        start_time = time.time()
        quotient, remainder = NaturalOperations.DIV_NN_N(self.large_num1, self.large_num2)
        end_time = time.time()
        print(f"Деление большого натурального числа: Результат: {quotient},  заняло {end_time - start_time:.6f} секунд.")

if __name__ == "__main__":
    unittest.main()
