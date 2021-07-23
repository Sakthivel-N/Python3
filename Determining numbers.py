from collections import Counter
N=int(input())
arr=list(map(int,input().split(" ")))
newarr=[]
listarr=[str(i) for i in arr]
for i in listarr:
    
    counter = Counter(listarr)
    out=counter[i]
    if(out==1):
        newarr.append(int(i))
st=""

a=sorted(newarr)

for j in a:
    st+=str(j)+" "
print(st)
