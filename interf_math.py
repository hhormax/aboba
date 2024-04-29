import numpy as np
import matplotlib.pyplot as plt
# Длина волны света (в метрах)
lambda_0 = 632e-9  
# Красный свет от гелий-неонового лазера

# Длина рабочего плеча (в метрах)
L = 100

# Количество точек для расчета
num_points = 10000

# Оптическая разность путей
delta_L = np.linspace(0, L, num_points)
# Интенсивность на детекторе
I =  (1 + np.cos(2 * np.pi * delta_L / lambda_0))
# Построение графика
plt.plot(delta_L, I)

# Настройка графика
plt.xlabel('Оптическая разность путей (м)')
plt.ylabel('Интенсивность')
plt.title('Интерференционные полосы интерферометра Майкельсона')
plt.grid(True)
plt.show()
