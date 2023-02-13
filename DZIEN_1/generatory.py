#przykład 1
def liczby():
    for i in range(11):
        yield i*2

print(list(liczby()))

for p in liczby():
    print(p)

#przykład 2
def wznowienia(n,k):
    print("wstrzymanie działania...")
    yield 1001
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n+k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n-k
    print("wznowienie działania...")

    print("wstrzymanie działania...")
    yield n*k
    print("wznowienie działania...")


#print(list(wznowienia(7,5)))

for i in wznowienia(7,5):
    if i == 1001:
        continue
    print(f"zwrócono wartość: {i}")

#przykład 3

def complexgen():
    x=0
    while True:
        print("x-print1")
        y = yield x
        print("x-print2")
        if y is None:
            x = x+1
        else:
            x=y


g = complexgen()

print(next(g))
print(next(g))
print(next(g))
print(g.send(123))
print(next(g))
print(next(g))
print(next(g))

