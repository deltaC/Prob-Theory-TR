import numpy as np
import scipy.stats


print('X | P')
rv = scipy.stats.hypergeom(16, 11, 5)
for i in range(6):
    print(i, '|', rv.pmf(i))

print('-----------------------')
print('MX =', rv.mean())
print('DX =', rv.var())
