N=int(input())
vaccines=list(map(int,input().split()))
patients=list(map(int,input().split()))
value=1
for a,b in zip(vaccines,patients):
    if(a<b):
        value=0
        break
    
if(value):
    print('Yes')
else:
    print('No')
