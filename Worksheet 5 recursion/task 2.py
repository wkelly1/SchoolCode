import time

def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
startTime = time.clock()
fib(10)
endTime = time.clock()

print("Time of completion = ",(endTime - startTime)*1000)