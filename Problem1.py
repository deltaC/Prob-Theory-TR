import numpy as np
import scipy.stats

print("X | ", end='')
for i in range(6):
    if i != 5:
        print(i, "| ", end='')
    else:
        print(i, end='')

print()
print('P | ', end='')
rv = hy
for i in range(6):
    print(scipy.stats.hypergeom.pmf()

# scipy.stats.hypergeom.pmf
