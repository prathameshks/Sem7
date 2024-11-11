wt =[]
val = []

n = int(input("Enter N:"))

for _ in range(n):
    wt.append(int(input("Enter w:")))
    val.append(int(input("Enter val:")))
    
cap = int(input("Enter capacity:"))

dp = [[-1 for _ in range(cap+1)] for __ in range(n+1)]
# print(dp)

def func(ind,wt_left):
    if(wt_left == 0): return 0
    if(ind < 0): return 0
    if(dp[ind][wt_left] != -1): return dp[ind][wt_left]
    
    # dont select at ind
    ans = func(ind-1,wt_left)
    # choose at ind
    if(wt_left >= wt[ind]):
        a2 = func(ind-1,wt_left - wt[ind]) + val[ind]
        ans = max(ans,a2)
        
    dp[ind][wt_left] = ans
    return ans
    
print(func(n-1,cap))




"""
IP:
3
3
30
4
70
5
60
8

"""
