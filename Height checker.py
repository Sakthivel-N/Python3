a=int(input())
count = 0
heights=[int(i) for i in str(a)]
        
for x,y in zip(heights,sorted(heights)):
    if x!=y:
        count+=1
print (count)

