from pulp import LpProblem, LpVariable, LpMaximize, value

# Создаем модель для задачи линейного программирования с названием "Beverage_production" и целью максимизации производства.
model = LpProblem(name="Beverage_production", sense=LpMaximize)

# Определяем переменные решения для производства лимонада (A) и фруктового сока (B), обе переменные ограничены снизу нулем и целочисленного типа.
lemonade = LpVariable(name="lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Задаем целевую функцию для максимизации общего производства лимонада и фруктового сока.
model += lemonade + fruit_juice, 'Production'

# Устанавливаем ограничения на материалы: вода, сахар, лимонный сок и фруктовое пюре.
model += 2 * lemonade + fruit_juice <= 100, 'Water'
model += lemonade <= 50, 'Sugar'
model += lemonade <= 30, 'Lemon juice'
model += 2 * fruit_juice <= 40, 'Fruit puree'

# Решаем задачу линейного программирования.
model.solve()

# Выводим оптимальные значения производства лимонада и фруктового сока, а также общее производство.
print('\n')
print("🔄 Максимальна кількість продукту:", round(model.objective.value(), 2))
print("🍋 Лемонаду:", round(lemonade.value(), 2))
print("🍏 Фруктового соку:", round(fruit_juice.value(), 2))
print('\n')
