import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from operations.natural_operations import NaturalOperations
from operations.integer_operations import IntegerOperations
from operations.rational_operations import RationalOperations
from operations.polynomial_operation import PolynomialOperations
from classes import *

# Функция обработки выбора модуля
def execute_module(module_name):
    messagebox.showinfo("Выполнение", f"Вы выбрали модуль: {module_name}")


# Основной класс приложения
class AlgebraSystemApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система компьютерной алгебры")
        self.geometry("1200x1000")

        # Категории и модули
        self.categories = {
            "Натуральные числа с нулем": {
                "N-1 Сравнение натуральных чисел": NaturalOperations.COM_NN_D,
                "N-2 Проверка на ноль": NaturalOperations.NZER_N_B,
                "N-3 Добавление 1 к натуральному числу": NaturalOperations.ADD_1N_N,
                "N-4 Сложение натуральных чисел": NaturalOperations.ADD_NN_N,
                "N-5 Вычитание из первого большего натурального числа второго меньшего или равного": NaturalOperations.SUB_NN_N,
                "N-6 Умножение натурального числа на цифру": NaturalOperations.MUL_ND_N,
                "N-7 Умножение натурального числа на 10^k, k-натуральное": NaturalOperations.MUL_Nk_N,
                "N-8 Умножение натуральных чисел": NaturalOperations.MUL_NN_N,
                "N-9 Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом": NaturalOperations.SUB_NDN_N,
                "N-10 Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k": NaturalOperations.DIV_NN_Dk,
                "N-11 Неполное частное от деления первого натурального числа на второе с остатком": NaturalOperations.DIV_NN_N,
                "N-12 Остаток от деления первого натурального числа на второе натуральное": NaturalOperations.MOD_NN_N,
                "N-13 НОД натуральных чисел": NaturalOperations.GCF_NN_N,
                "N-14 НОК натуральных чисел": NaturalOperations.LCM_NN_N,
            },
            "Целые числа": {
                "Z-1 Абсолютная величина числа": IntegerOperations.ABS_Z_N,
                "Z-2 Определение положительности числа": IntegerOperations.POZ_Z_D,
                "Z-3 Умножение целого на (-1)": IntegerOperations.MUL_ZM_Z,
                "Z-4 Преобразование натурального в целое": IntegerOperations.TRANS_N_Z,
                "Z-5 Преобразование целого неотрицательного в натуральное": IntegerOperations.TRANS_Z_N,
                "Z-6 Сложение целых чисел": IntegerOperations.ADD_ZZ_Z,
                "Z-7 Вычитание целых чисел": IntegerOperations.SUB_ZZ_Z,
                "Z-8 Умножение целых чисел": IntegerOperations.MUL_ZZ_Z,
                "Z-9 Частное от деления целого на целое": IntegerOperations.DIV_ZZ_Z,
                "Z-10 Остаток от деления целого на целое": IntegerOperations.MOD_ZZ_Z,
            },
            "Рациональные числа": {
                "Q-1 Сокращение дроби": RationalOperations.RED_Q_Q,
                "Q-2 Проверка сокращенного дробного на целое": RationalOperations.INT_Q_B,
                "Q-3 Преобразование целого в дробное": RationalOperations.TRANS_Z_Q,
                "Q-4 Преобразование сокращенного дробного в целое": RationalOperations.TRANS_Q_Z,
                "Q-5 Сложение дробей": RationalOperations.ADD_QQ_Q,
                "Q-6 Вычитание дробей": RationalOperations.SUB_QQ_Q,
                "Q-7 Умножение дробей": RationalOperations.MUL_QQ_Q,
                "Q-8 Деление дробей (делитель отличен от нуля)": RationalOperations.DIV_QQ_Q,
            },
            "Многочлены с рациональными коэффициентами": {
                "P-1 Сложение многочленов": PolynomialOperations.ADD_PP_P,
                "P-2 Вычитание многочленов": PolynomialOperations.SUB_PP_P,
                "P-3 Умножение многочлена на рациональное число": PolynomialOperations.MUL_PQ_P,
                "P-4 Умножение многочлена на x^k, k-натуральное или 0": PolynomialOperations.MUL_Pxk_P,
                "P-5 Старший коэффициент многочлена": PolynomialOperations.LED_P_Q,
                "P-6 Степень многочлена": PolynomialOperations.DEG_P_N,
                "P-7 Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей": PolynomialOperations.FAC_P_Q,
                "P-8 Умножение многочленов": PolynomialOperations.MUL_PP_P,
                "P-9 Частное от деления многочлена на многочлен при делении с остатком": PolynomialOperations.DIV_PP_P,
                "P-10 Остаток от деления многочлена на многочлен при делении с остатком": PolynomialOperations.MOD_PP_P,
                "P-11 НОД многочленов": PolynomialOperations.GCF_PP_P,
                "P-12 Производная многочлена": PolynomialOperations.DER_P_P,
                "P-13 Преобразование многочлена — кратные корни в простые": PolynomialOperations.NMR_P_P,
            },
        }

        # Создаем интерфейс
        self.create_widgets()

    def create_widgets(self):
        # Категория
        self.category_label = tk.Label(self, text="Выберите категорию:")
        self.category_label.pack(pady=10)

        self.category_combobox = ttk.Combobox(self, values=list(self.categories.keys()))
        self.category_combobox.pack(pady=10)
        self.category_combobox.bind("<<ComboboxSelected>>", self.on_category_selected)

        # Модули
        self.module_label = tk.Label(self, text="Модули:")
        self.module_label.pack(pady=10)

        self.module_listbox = tk.Listbox(self, height=15)
        self.module_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Поле ввода данных
        self.input_label = tk.Label(self, text="Введите аргументы через запятую:")
        self.input_label.pack(pady=10)

        self.input_entry = tk.Entry(self)
        self.input_entry.pack(pady=10, fill=tk.X, expand=True)

        # Кнопка выполнения
        self.execute_button = tk.Button(self, text="Выполнить", command=self.on_execute)
        self.execute_button.pack(pady=10)

        # Индикатор выполнения
        self.progress = ttk.Progressbar(self, mode="indeterminate")
        self.progress.pack(pady=10)

        # Поле вывода результата
        self.result_label = tk.Label(self, text="Результат:")
        self.result_label.pack(pady=10)

        self.result_text = tk.Text(self, height=10, state="disabled")
        self.result_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def on_category_selected(self, event):
        category = self.category_combobox.get()
        self.module_listbox.delete(0, tk.END)
        for module in self.categories[category]:
            self.module_listbox.insert(tk.END, module)

    def on_execute(self):
        # Запуск индикатора выполнения
        self.progress.start()
        self.after(100, self.run_execution)  # Отложенный запуск выполнения

    def run_execution(self):
        # Получение выбранной категории и модуля
        selected_category = self.category_combobox.get()
        selected_module = self.module_listbox.get(tk.ACTIVE)

        if not selected_category or not selected_module:
            messagebox.showwarning("Ошибка", "Выберите категорию и модуль для выполнения.")
            return

        # Получаем выбранную функцию
        module_function = self.categories[selected_category][selected_module]

        # Логика обработки в зависимости от категории
        if selected_category == "Натуральные числа с нулем":
            self.process_natural_number(module_function)
        elif selected_category == "Целые числа":
            self.process_integer_number(module_function)
        elif selected_category == "Рациональные числа":
            self.process_rational_number(module_function)
        elif selected_category == "Многочлены с рациональными коэффициентами":
            self.process_polynomal_number(module_function)
        else:
            messagebox.showwarning("Ошибка", "Неподдерживаемая категория.")

        self.progress.stop()

    def process_natural_number(self, module_function):
        # Окно для ввода данных
        input_data = self.input_entry.get().strip()
        if not input_data:
            messagebox.showwarning("Ошибка", "Данные не введены.")
            return

        try:
            # Преобразуем данные в натуральные числа
            inputs = [Natural(x.strip()) for x in input_data.split(",")]
            result = module_function(*inputs)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            if isinstance(result, (list, tuple)):
                result = ", ".join(map(str, result))
            self.result_text.insert(tk.END, f"Результат: {result}")
            self.result_text.config(state="disabled")
        except ValueError as e:
            messagebox.showwarning("Ошибка", str(e))

    def process_integer_number(self, module_function):
        input_data = self.input_entry.get().strip()
        if not input_data:
            messagebox.showwarning("Ошибка", "Данные не введены.")
            return

        try:
            # Преобразуем данные в целые числа
            inputs = [Integer(x.strip()) for x in input_data.split(",")]
            result = module_function(*inputs)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            if isinstance(result, (list, tuple)):
                result = ", ".join(map(str, result))
            self.result_text.insert(tk.END, f"Результат: {result}")
            self.result_text.config(state="disabled")
        except ValueError as e:
            messagebox.showwarning("Ошибка", str(e))

    def process_rational_number(self, module_function):
        input_data = self.input_entry.get().strip()
        if not input_data:
            messagebox.showwarning("Ошибка", "Данные не введены.")
            return
        try:
            # Особая обработка для TRANS_Z_Q
            if module_function.__name__ == "TRANS_Z_Q":
                if '/' in input_data:
                    raise ValueError("Для преобразования целого в дробное введите целое число без знаменателя")
                # Преобразуем входное значение в целое число
                integer_input = Integer(input_data.strip())
                result = module_function(integer_input)
                # Явно показываем дробь с знаменателем
                display_result = f"{result.numerator}/{result.denominator}"
            else:
                # Стандартная обработка для остальных операций с дробями
                inputs = []
                for fraction in input_data.split(","):
                    fraction = fraction.strip()
                    if '/' not in fraction:
                        raise ValueError(f"Некорректный формат дроби: '{fraction}'. Ожидается 'числитель/знаменатель'.")
                    numerator, denominator = fraction.split("/")
                    inputs.append(Rational(Integer(numerator.strip()), Natural(denominator.strip())))

                result = module_function(*inputs)
                display_result = str(result)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Результат: {display_result}")
            self.result_text.config(state="disabled")
        except ValueError as e:
            messagebox.showwarning("Ошибка", str(e))

    def process_polynomal_number(self, module_function):
        input_data = self.input_entry.get().strip()
        if not input_data:
            messagebox.showwarning("Ошибка", "Данные не введены.")
            return

        try:

            # Разбиваем строку на аргументы
            args = [x.strip() for x in input_data.split(",")]
            
            # Особая обработка для MUL_Pxk_P и MUL_PQ_P
            if module_function.__name__ == "MUL_Pxk_P":
                if len(args) != 2:
                    raise ValueError("Требуется два аргумента: многочлен и натуральная степень k")
                poly = create_polynomial(args[0])
                k = Natural(args[1])
                result = module_function(poly, k)
                
            elif module_function.__name__ == "MUL_PQ_P":
                if len(args) != 2:
                    raise ValueError("Требуется два аргумента: многочлен и рациональное число")
                poly = create_polynomial(args[0])
                # Парсим рациональное число
                if '/' in args[1]:
                    num, den = args[1].split('/')
                    q = Rational(Integer(num.strip()), Natural(den.strip()))
                else:
                    q = Rational(Integer(args[1].strip()))
                result = module_function(poly, q)
                
            else:
                # Стандартная обработка для остальных функций
                inputs = [create_polynomial(poly) for poly in args]
                result = module_function(*inputs)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Результат: {result}")
            self.result_text.config(state="disabled")
            
        except ValueError as e:
            messagebox.showwarning("Ошибка", str(e))
        except Exception as e:
            messagebox.showwarning("Ошибка", f"Некорректный формат ввода: {str(e)}")
            # Преобразуем данные в целые числа
            inputs = [create_polynomial(x.strip()) for x in input_data.split(",")]
            result = module_function(*inputs)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            if isinstance(result, (list, tuple)):
                result = ", ".join(map(str, result))
            self.result_text.insert(tk.END, f"Результат: {result}")
            self.result_text.config(state="disabled")
        except ValueError as e:
            messagebox.showwarning("Ошибка", str(e))


# Запуск приложения
if __name__ == "__main__":
    app = AlgebraSystemApp()
    app.mainloop()

