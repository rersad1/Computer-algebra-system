import unittest
import time
from classes import *
from operations.integer_operations import IntegerOperations

class TestIntegerOperations(unittest.TestCase):

    # Тестируем метод ABS_Z_N (Абсолютная величина числа)
    def test_ABS_Z_N(self):
        num = Integer("123")
        result = IntegerOperations.ABS_Z_N(num)
        self.assertEqual(result.get_digits(), [1, 2, 3])

        num_neg = Integer("-123")
        result_neg = IntegerOperations.ABS_Z_N(num_neg)
        self.assertEqual(result_neg.get_digits(), [1, 2, 3])

    # Тестируем метод SGN_Z_D (Определение знака числа)
    def test_SGN_Z_D(self):
        num_pos = Integer("123")
        self.assertEqual(IntegerOperations.POZ_Z_D(num_pos), 2)

        num_zero = Integer("0")
        self.assertEqual(IntegerOperations.POZ_Z_D(num_zero), 0)

        num_neg = Integer("-123")
        self.assertEqual(IntegerOperations.POZ_Z_D(num_neg), 1)

    # Тестируем метод MUL_ZM_Z (Умножение на -1)
    def test_MUL_ZM_Z(self):
        num_pos = Integer("123")
        result_pos = IntegerOperations.MUL_ZM_Z(num_pos)
        self.assertEqual(result_pos.get_digits(), [1, 2, 3])
        self.assertTrue(result_pos.get_sign())  # Проверяем, что знак отрицательный

        num_neg = Integer("-123")
        result_neg = IntegerOperations.MUL_ZM_Z(num_neg)
        self.assertEqual(result_neg.get_digits(), [1, 2, 3])
        self.assertFalse(result_neg.get_sign())  # Проверяем, что знак положительный

    # Тестируем метод TRANS_N_Z (Преобразование натурального в целое)
    def test_TRANS_N_Z(self):
        num = Natural("123")
        result = IntegerOperations.TRANS_N_Z(num)
        self.assertEqual(result.get_digits(), [1, 2, 3])
        self.assertFalse(result.get_sign())  # Целое число всегда положительное

    # Тестируем метод TRANS_Z_N (Преобразование целого в натуральное)
    def test_TRANS_Z_N(self):
        num_pos = Integer("123")
        result = IntegerOperations.TRANS_Z_N(num_pos)
        self.assertEqual(result.get_digits(), [1, 2, 3])

        num_neg = Integer("-123")
        with self.assertRaises(ValueError):
            IntegerOperations.TRANS_Z_N(num_neg)

    # Тестируем метод ADD_ZZ_Z (Сложение целых чисел)
    def test_ADD_ZZ_Z(self):
        num1 = Integer("123")
        num2 = Integer("456")
        result = IntegerOperations.ADD_ZZ_Z(num1, num2)
        self.assertEqual(result.get_digits(), [5, 7, 9])
        self.assertFalse(result.get_sign())  # Результат положительный

        num1_neg = Integer("-123")
        result_neg = IntegerOperations.ADD_ZZ_Z(num1_neg, num2)
        self.assertEqual(result_neg.get_digits(), [3, 3, 3])
        self.assertFalse(result_neg.get_sign())  # Результат положительный

    # Тестируем метод SUB_ZZ_Z (Вычитание целых чисел)
    def test_SUB_ZZ_Z(self):
        num1 = Integer("456")
        num2 = Integer("123")
        result = IntegerOperations.SUB_ZZ_Z(num1, num2)
        self.assertEqual(result.get_digits(), [3, 3, 3])
        self.assertFalse(result.get_sign())  # Результат положительный

        num1_neg = Integer("-456")
        result_neg = IntegerOperations.SUB_ZZ_Z(num1_neg, num2)
        self.assertEqual(result_neg.get_digits(), [5, 7, 9])
        self.assertTrue(result_neg.get_sign())  # Результат отрицательный

    def test_MUL_ZZ_Z(self):
        num1 = Integer("123")
        num2 = Integer("456")
        result = IntegerOperations.MUL_ZZ_Z(num1, num2)
        self.assertEqual(result.get_digits(), [5, 6, 0, 8, 8])  # Ожидаем правильный результат
        self.assertFalse(result.get_sign())  # Результат положительный

        num1_neg = Integer("-123")
        result_neg = IntegerOperations.MUL_ZZ_Z(num1_neg, num2)
        self.assertEqual(result_neg.get_digits(), [5, 6, 0, 8, 8])  # Ожидаем правильный результат
        self.assertTrue(result_neg.get_sign())  # Результат отрицательный

    # Тестируем метод DIV_ZZ_Z (Деление целых чисел)
    def test_DIV_ZZ_Z(self):
        # Пример деления положительных чисел
        num1 = Integer("10")
        num2 = Integer("2")
        result = IntegerOperations.DIV_ZZ_Z(num1, num2)
        self.assertEqual(str(result), "5")

    def test_MOD_ZZ_Z(self):
        # Положительные числа
        num1 = Integer("456")
        num2 = Integer("123")
        result = IntegerOperations.MOD_ZZ_Z(num1, num2)
        self.assertEqual(result.get_digits(), [8, 7])  # Ожидаемый результат: 456 % 123 = 87
        self.assertFalse(result.get_sign())  # Результат положительный

    def test_large_integer_operations(self):
        # Бенчмарк для сложения больших целых чисел
        num1 = Integer("123456789012345478325643563247562359723756235623563427592456723456985695632678901234567890")
        num2 = Integer("987654321098727562569856327562375692569254974325743275697562743569256943365432109876543210")

        start_time = time.time()
        result_add = IntegerOperations.ADD_ZZ_Z(num1, num2)
        end_time = time.time()

        print("Результат сложения больших чисел:", result_add)
        print("Время выполнения сложения:", end_time - start_time, "секунд")

        # Бенчмарк для умножения больших целых чисел
        start_time = time.time()
        result_mul = IntegerOperations.MUL_ZZ_Z(num1, num2)
        end_time = time.time()

        print("Результат умножения больших чисел:", result_mul)
        print("Время выполнения умножения:", end_time - start_time, "секунд")

if __name__ == "__main__":
    unittest.main()
