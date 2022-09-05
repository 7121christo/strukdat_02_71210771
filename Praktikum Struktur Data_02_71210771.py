#71210771 - Christophorus Adyatma Wahyu SN

import timeit

def fib_iteratif(n):
    a=1
    b=0
    for i in range(0,n):
        a=b
        b=a+b
    return fib_iteratif

for i in range(1,101):
    start = timeit.default_timer()
    fib_iteratif(i)
    end = timeit.default_timer()
    print("fibonacci iteratif ke ", i, ": ", end-start, " detik.")

def fib_rekursif(n):
	if n < 0:
		print("Terjadi kesalahan")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fib_rekursif(n-1) + fib_rekursif(n-2)
    
for i in range(1,101):
    start = timeit.default_timer()
    fib_rekursif(i)
    end = timeit.default_timer()
    print("fibonacci rekursif ke ", i, ": ", end-start, " detik.")


