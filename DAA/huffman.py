import heapq

class Node:
    char = None
    freq = None
    left = None
    right = None
    
    def __init__(self,char=None,freq=0):
        self.char = char
        self.freq = freq
        
    def __lt__(self,other):
        return self.freq < other.freq
    
    def __gt__(self,other):
        return self.freq > other.freq
    
    def __str__(self):
        return f"{self.char} : {self.freq}"
    def __repr__(self):
        return f"{self.char} : {self.freq}"

def dfs(root:Node,code:str,ans:dict):
    if(root == None): return
    if(root.char != None):
        ans[root.char] = code
        return
    
    dfs(root.left,code+'0',ans)
    dfs(root.right,code+'1',ans)

s = input("Enter String to Encode:")

cnt = dict()

for c in s:
    if c in cnt:
        cnt[c] +=1
    else:
        cnt[c] = 1
        
print("Frequency:")
print(cnt)

arr:Node = []

for key in cnt.keys():
    temp = Node(key,cnt[key])
    heapq.heappush(arr,temp)
    
while len(arr) > 1:
    t1 = heapq.heappop(arr)
    t2 = heapq.heappop(arr)
    new_t = Node(None,t1.freq+t2.freq)
    new_t.left = t1
    new_t.right = t2
    heapq.heappush(arr,new_t)

root = heapq.heappop(arr)

codes = dict()

dfs(root,'',codes)

print("Codes:")
print(codes)