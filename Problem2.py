import numpy as np
import scipy.stats

probability = 0.97
a = 20

# Вычисляем Ф
phi = (probability + 1) / 2
z_std = scipy.stats.norm.ppf(phi)

# Вычисляем сигму и дисперсию
sigma = a / z_std
DX = sigma ** 2

print("Ответ: DX =", DX)