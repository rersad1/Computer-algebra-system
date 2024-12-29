from classes import *
from operations.natural_operations import NaturalOperations

class IntegerOperations:
    @staticmethod
    def ABS_Z_N(num: Integer) -> Natural:
        new_natural = Natural("0")
        new_natural.digits = num.digits.copy()
        return new_natural

    @staticmethod
    def POZ_Z_D(num: Integer) -> int:
        if len(num.digits) == 1 and num.digits[0] == 0:
            return 0
        return 1 if num.is_negative else 2

    @staticmethod
    def MUL_ZM_Z(num: Integer) -> Integer:
        if len(num.digits) == 1 and num.digits[0] == 0:
            return num
        result = Integer("0")
        result.digits = num.digits.copy()
        result.is_negative = not num.is_negative
        return result

    @staticmethod
    def TRANS_N_Z(num: Natural) -> Integer:
        result = Integer("0")
        result.digits = num.digits.copy()
        result.is_negative = False
        return result

    @staticmethod
    def TRANS_Z_N(num: Integer) -> Natural:
        if num.is_negative:
            raise ValueError("Отрицательное число нельзя преобразовать в натуральное.")
        result = Natural("0")
        result.digits = num.digits.copy()
        return result

    @staticmethod
    def ADD_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        if len(num1.digits) == 1 and num1.digits[0] == 0:
            return num2
        if len(num2.digits) == 1 and num2.digits[0] == 0:
            return num1

        result = Integer("0")
        
        if num1.is_negative == num2.is_negative:
            sum_abs = NaturalOperations.ADD_NN_N(
                IntegerOperations.ABS_Z_N(num1),
                IntegerOperations.ABS_Z_N(num2)
            )
            result.digits = sum_abs.digits
            result.is_negative = num1.is_negative
        else:
            abs1 = IntegerOperations.ABS_Z_N(num1)
            abs2 = IntegerOperations.ABS_Z_N(num2)
            comparison = NaturalOperations.COM_NN_D(abs1, abs2)
            
            if comparison == 2:
                difference = NaturalOperations.SUB_NN_N(abs1, abs2)
                result.digits = difference.digits
                result.is_negative = num1.is_negative
            else:
                difference = NaturalOperations.SUB_NN_N(abs2, abs1)
                result.digits = difference.digits
                result.is_negative = num2.is_negative

            if len(result.digits) == 1 and result.digits[0] == 0:
                result.is_negative = False

        return result

    @staticmethod
    def SUB_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        result = Integer("0")
        abs1 = IntegerOperations.ABS_Z_N(num1)
        abs2 = IntegerOperations.ABS_Z_N(num2)

        if num1.is_negative != num2.is_negative:
            sum_abs = NaturalOperations.ADD_NN_N(abs1, abs2)
            result.digits = sum_abs.digits
            result.is_negative = num1.is_negative
        else:
            comparison = NaturalOperations.COM_NN_D(abs1, abs2)
            if comparison == 2:
                difference = NaturalOperations.SUB_NN_N(abs1, abs2)
                result.digits = difference.digits
                result.is_negative = num1.is_negative
            else:
                difference = NaturalOperations.SUB_NN_N(abs2, abs1)
                result.digits = difference.digits
                result.is_negative = not num1.is_negative

        if len(result.digits) == 1 and result.digits[0] == 0:
            result.is_negative = False

        return result

    @staticmethod
    def MUL_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        if (len(num1.digits) == 1 and num1.digits[0] == 0) or \
           (len(num2.digits) == 1 and num2.digits[0] == 0):
            return Integer("0")

        result = Integer("0")
        abs_result = NaturalOperations.MUL_NN_N(
            IntegerOperations.ABS_Z_N(num1),
            IntegerOperations.ABS_Z_N(num2)
        )
        result.digits = abs_result.digits
        result.is_negative = num1.is_negative != num2.is_negative
        return result

    @staticmethod
    def DIV_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        if len(num2.digits) == 1 and num2.digits[0] == 0:
            raise ValueError("Делитель не может быть равен нулю.")

        result = Integer("0")
        abs_result = NaturalOperations.DIV_NN_N(
            IntegerOperations.ABS_Z_N(num1),
            IntegerOperations.ABS_Z_N(num2)
        )
        result.digits = abs_result.digits
        result.is_negative = num1.is_negative != num2.is_negative
        return result

    @staticmethod
    def MOD_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        if len(num2.digits) == 1 and num2.digits[0] == 0:
            raise ValueError("Делитель не может быть равен нулю.")

        quotient = IntegerOperations.DIV_ZZ_Z(num1, num2)
        product = IntegerOperations.MUL_ZZ_Z(quotient, num2)
        remainder = IntegerOperations.SUB_ZZ_Z(num1, product)

        if num2.is_negative:
            remainder = IntegerOperations.MUL_ZM_Z(remainder)

        return remainder