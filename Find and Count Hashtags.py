import re
from collections import Counter,OrderedDict
n=int(input())
s=''
for i in range(n):
    s+=str(input())
    s+=" "
li=list(s.split(" "))

ans=[]
for i in li:
    
    x = re.search(r"\#\w+", i)
    if x:
        ans.append(i)

class OrderedCounter(Counter, OrderedDict):
    pass
[print(c[0]) for c in OrderedCounter(sorted(ans)).most_common(5)]
    
