import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
import random

# Функція для методу Монте-Карло інтегрування
def monte_carlo_integration(func, lower_bound, upper_bound, num_samples=1000):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(lower_bound, upper_bound)
        total += func(x)
    
    return (upper_bound - lower_bound) * total / num_samples

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

lower_bound = 0  # Нижня межа
upper_bound = 2  # Верхня межа

# Створення діапазону значень для x
x_values = np.linspace(-0.5, 2.5, 400)
y_values = f(x_values)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x_values, y_values, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(lower_bound, upper_bound)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x_values[0], x_values[-1]])
ax.set_ylim([0, max(y_values) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=lower_bound, color='gray', linestyle='--')
ax.axvline(x=upper_bound, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {lower_bound} до {upper_bound}')
plt.grid()
plt.show()

# Обчислення інтеграла використовуючи метод Монте-Карло
monte_carlo_result = monte_carlo_integration(f, lower_bound, upper_bound, num_samples=100000)
# Обчислення інтеграла використовуючи scipy.integrate.quad
quad_result, quad_error = integrate.quad(f, lower_bound, upper_bound)

print('\n')
print(f"Результати інтегрування")
print(f"{'-'*50}")
print(f"{'Метод':^20} | {'Результат':^12} | {'Помилка':^}")
print(f"{'-'*50}")
print(f"{'Монте-Карло':<20} | {monte_carlo_result:^12.10f} |")
print(f"{'Quad':<20} | {quad_result:^12.10f} | {quad_error}")
print('\n')
