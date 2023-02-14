from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def mojafunkcja(a):
    for i in range(15000000):
        a[i] += 1

@jit(target_backend='cuda')
def mojafunkcjaGP(a):
    for i in range(15000000):
        a[i] += 1

if __name__ == '__main__':

    n = 15000000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    mojafunkcja(a)
    print(f"czas wykoania operacji na CPU: {timer()-start} s")

    start = timer()
    mojafunkcjaGP(a)
    print(f"czas wykoania operacji na GPU: {timer() - start} s")
    

