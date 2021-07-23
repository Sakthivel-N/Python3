N0_inp=int(input())
arr=list(map(int,input().split()))
newarr=[]
for i in range(N0_inp-1):
    checkmax=arr[i]
    eval_out=str(arr[i])
    for j in range(i+1,N0_inp):
        if arr[j]>checkmax:
            checkmax=arr[j]
            eval_out+='^'+str(arr[j])
    
    newarr.append(eval(eval_out))


newarr.append(arr[-1])

print(max(newarr))
