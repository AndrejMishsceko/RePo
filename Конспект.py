

# Задача про кубики

import numpy as np
np.random.seed(1)
n=60
b=np.random.randint(1,7,n)
print(b)
# [6 4 5 1 2 4 6 1 1 2 5 6 5 2 3 5 6 3 5 4 5 3 5 6 3 5 2 2 1 6 2 2 6 2 2 1 5
#  2 1 1 6 4 3 2 1 4 6 2 2 4 5 1 2 4 5 3 5 1 6 4]

a=b [b==3]
print(a)
# [3 3 3 3 3 3]

m=len(a)
print(m)

# Теперь можем вычислить относительную частоту события А

W=m/n
print(W)



