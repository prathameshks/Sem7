import time 

step_itr = 0
step_rec = 0

def fibo_iterative(n):
    global step_itr
    a, b = 0, 1
    for _ in range(n-1):
        step_itr += 1
        a, b = b, a + b
    return a

def fibo_recursive(n):
    global step_rec
    step_rec += 1
    
    if(n <= 1): return 0
    if(n == 2): return 1
    
    return fibo_recursive(n-1) + fibo_recursive(n-2)


t1 = time.time()
print(fibo_iterative(20))
t2 = time.time()

print("Iterative")
print("Time: ", t2-t1)
print("Steps: ", step_itr)

t1 = time.time()
print(fibo_recursive(20))
t2 = time.time()

print("Recursive")
print("Time: ", t2-t1)
print("Steps: ", step_rec)