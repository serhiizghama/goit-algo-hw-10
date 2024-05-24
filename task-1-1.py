import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import random

# Функція для методу Монте-Карло інтегрування
def monte_carlo_integration(func, a, b, num_samples=1000):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += func(x)
    
    return (b - a) * total / num_samples

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()

# Обчислення інтеграла використовуючи метод Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples=100000)
# Обчислення інтеграла використовуючи scipy.integrate.quad
quad_result, quad_error = spi.quad(f, a, b)

print('\n')
print(f"Результати інтегрування")
print(f"{'-'*50}")
print(f"{'Метод':^20} | {'Результат':^12} | {'Помилка':^}")
print(f"{'-'*50}")
print(f"{'Монте-Карло':<20} | {monte_carlo_result:^12.10f} |")
print(f"{'Quad':<20} | {quad_result:^12.10f} | {quad_error}")
print('\n')
