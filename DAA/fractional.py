
n = int(input("Enter No of Weights:"))

class wt:
    w = 0
    p = 0
    pw = 1
    
    def __init__(self,w,p):
        self.w = w
        self.p = p
        self.pw = p/w 
        
    def __gt__(self,other):
        return self.pw > other.pw
    
    def __lt__(self,other):
        return self.pw < other.pw
    
    def __repr__(self):
        return f"'W:{self.w}, P:{self.p}, Ratio:{self.pw}'\n"
    
    def __str__(self):
        return f"'W:{self.w}, P:{self.p}, Ratio:{self.pw}'\n"
        
    
weights = []

for i in range(n):
    w = int(input(f"Enter W {i+1}:"))
    p = int(input(f"Enter P {i+1}:"))
    
    weights.append(wt(w,p))
    
cap = int(input("Enter Capacity:"))
print(cap)

wts = sorted(weights,reverse=True)

print(wts)

total_profit = 0
rem_cap = cap
for w in wts:
    if(w.w <= rem_cap):
        total_profit += w.p 
        rem_cap -= w.w
    else:
        total_profit += w.pw* rem_cap
        rem_cap =0
        break
    
print(f"{total_profit = }")
    
    
"""
sample input:
5
2
5
5
15
2
4
6
12
4
12
7

OP:
21
"""