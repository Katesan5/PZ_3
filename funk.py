import math

def linear_function(x):
    return 2 * x + 3  # 2x+3

def quadratic_function(x):
    return x**2 - 4

def trigonometric_function(x):
    return math.sin(x) + math.cos(x)   # sin(x)+cos(x)

def exponential_function(x):
    return math.exp(x)

def logarithmic_function(x):
    return math.log(abs(x) + 1)

def rational_function(x):

    if abs(x + 0.1) < 1e-10:
        return float('inf')
    return 1 / (x + 0.1)

available_functions = {
    '1': ('Линейная (2x + 3)', linear_function),
    '2': ('Квадратичная (x² - 4)', quadratic_function),
    '3': ('Тригонометрическая (sin(x) + cos(x))', trigonometric_function),
    '4': ('Экспоненциальная (e^x)', exponential_function),
    '5': ('Логарифмическая (log(|x| + 1))', logarithmic_function),
    '6': ('Рациональная (1/(x + 0.1))', rational_function)
}