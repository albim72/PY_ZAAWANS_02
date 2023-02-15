import time
import concurrent.futures
from funkcja_prime import znajdz_sume_liczb_pierwszych

numbers = [(1,10000),(3,50000),(5000,100000),(4,900),(8000,15000),(95000,133000)]

def synchroniczna():
    starttime = time.time()
    for pair in numbers:
        prime_suma = znajdz_sume_liczb_pierwszych(*pair)
        print(prime_suma)
    endtime=time.time()
    print(f'całkowity czas wyznaczenia sum - synchronicznie: {endtime-starttime} s')


def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)

def asynchroniczna():
    starttime = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    print(list(wynik))
    endtime = time.time()
    print(f'całkowity czas wyznaczenia sum - asynchronicznie: {endtime - starttime} s')

def main():
    asynchroniczna()
    synchroniczna()


if __name__ == '__main__':
    main()
