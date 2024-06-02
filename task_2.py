import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

def f(x):
    return np.e ** np.sin( x ** 2 )

a = 0 
b = 10 

y_max = 3

def is_dot_belong_to_func(func, x, y):
    return y < func(x)

def monte_carlo_calc(func, a, b, experiments_n, amount_dots):
    
    average_area = 0
     
    for _ in range(experiments_n):
        
        dots = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(amount_dots)]
        
        dots_of_func = [point for point in dots if is_dot_belong_to_func(func, point[0], point[1])]
        
        M = len(dots_of_func)
        N = len(dots)
        
        area = (M / N) * (a * b)
        
        average_area += area

    average_area /= experiments_n
    return average_area

for accuracy in range(1, 4):
    
    experiments = 10 ** accuracy
    print(f"# Experiments {experiments}")

    x = monte_carlo_calc(f, b, y_max, experiments, 10000)
    print(f"S: {x} (experimens {experiments})")
    
print("----------------")

result, error = spi.quad(f, a, b)

print("Integral (quad): ", result)

print("----------------")


x = np.linspace(-0.5, b+1, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=1)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='green', alpha=0.2)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.001])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('f(x) = e ^ sin(x^2) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
