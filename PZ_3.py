import numpy as np
from PZ_3_2 import available_functions
from PZ_3_3 import plot_function, print_xy_table
from PZ_3_1 import summ

def calculate_function_values(func, a, b, step):
    """Вычисление значений функции на интервале [a, b] с шагом step"""
    x_vector = np.arange(a, b + step, step)
    y_vector = []

    for x in x_vector:
        try:
            y = func(x)
            y_vector.append(y)
        except Exception as e:
            print(f"Ошибка при x = {x:.2f}: {e}")
            y_vector.append(float('nan'))

    return x_vector, np.array(y_vector)


def main():
    print("=" * 60)
    print("ПРОГРАММА ДЛЯ ИССЛЕДОВАНИЯ ФУНКЦИЙ")
    print("=" * 60)

    # Вывод доступных функций
    print("\nДОСТУПНЫЕ ФУНКЦИИ:")
    for key, (description, _) in available_functions.items():
        print(f"{key}. {description}")

    # Выбор функции
    while True:
        choice = input("\nВыберите функцию (1-6): ").strip()
        if choice in available_functions:
            function_name, selected_function = available_functions[choice]
            print(f"Выбрана функция: {function_name}")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

    # Ввод параметров
    while True:
        try:
            a = float(input("Введите начало интервала (a): "))
            b = float(input("Введите конец интервала (b): "))
            step = float(input("Введите шаг: "))

            if a >= b:
                print("Ошибка: начало интервала должно быть меньше конца!")
                continue
            if step <= 0:
                print("Ошибка: шаг должен быть положительным!")
                continue
            if (b - a) / step > 1000:
                print("Предупреждение: слишком много точек! Увеличьте шаг.")
                continue

            break
        except ValueError:
            print("Ошибка: введите числовые значения!")

    # Вычисление значений функции
    print(f"\nВычисление функции на интервале [{a}, {b}] с шагом {step}...")
    x_vector, y_vector = calculate_function_values (selected_function, a, b, step)

    # Вывод результатов
    print(f"\nРезультаты для функции: {function_name}")
    print(f"Количество точек: {len(x_vector)}")

    # Вывод таблицы значений
    print_xy_table(x_vector, y_vector)

    # Построение графика
    print("\nПостроение графика...")
    plot_function(x_vector, y_vector, function_name.split('(')[0])

    # Статистика
    valid_y = y_vector[~np.isnan(y_vector)]
    if len(valid_y) > 0:
        print(f"\nСТАТИСТИКА:")
        print(f"Минимальное значение Y: {np.min(valid_y):.4f}")
        print(f"Максимальное значение Y: {np.max(valid_y):.4f}")
        print(f"Среднее значение Y: {np.mean(valid_y):.4f}")


if __name__ == "__main__":
    main()