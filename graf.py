import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_function(x_vector, y_vector, function_name):      # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x_vector, y_vector, 'b-', linewidth=2, label=f'f(x) = {function_name}')
    plt.title(f'График функции: {function_name}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def print_xy_table(x_vector, y_vector, decimals=4):     # Таблица

    max_display_points = 20
    if len(x_vector) > max_display_points:
        step = len(x_vector) // max_display_points
        x_display = x_vector[::step]
        y_display = y_vector[::step]
    else:
        x_display = x_vector
        y_display = y_vector

    df = pd.DataFrame({
        'X': np.round(x_display, decimals),
        'Y': np.round(y_display, decimals)
    })

    print("\n" + "=" * 50)
    print("ТАБЛИЦА ЗНАЧЕНИЙ ФУНКЦИИ")
    print("=" * 50)
    print(df.to_string(index=False))
    print("=" * 50)

    print("\nВектор X:", np.round(x_vector[:10], decimals), "..." if len(x_vector) > 10 else "")
    print("Вектор Y:", np.round(y_vector[:10], decimals), "..." if len(y_vector) > 10 else "")