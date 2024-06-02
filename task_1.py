from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

model = LpProblem(name="Max-drink", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat="Continuous")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Continuous")

model += lemonade + fruit_juice, "Сума"

# restrictions
model += (2 * lemonade + 1 * fruit_juice <= 100), "Вода обмеження"
model += (1 * lemonade <= 50), "Цукор обмеження"
model += (1 * lemonade <= 30), "Лимонний сок обмеження"
model += (2 * fruit_juice <= 40), "Фруктове пюре обмеження"

model.solve()

LpStatus[model.status]

print(f"Лимонад: {lemonade.varValue} units")
print(f"Фруктовий сік: {fruit_juice.varValue} units")

input()