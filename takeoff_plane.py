for _ in range(int(input())):
    n,p,q,r = map(int, input().split(' '))

 
    maxP = set([i for i in range(0,n+1,p)])
    maxQ = set([i for i in range(0,n+1,q)])
    maxR = set([i for i in range(0,n+1,r)])
 

 
    sumP = maxP-maxQ-maxR
    sumQ = maxQ-maxP-maxR
    sumR = maxR-maxP-maxQ
 
    
 
    print(len(sumP)+len(sumQ)+len(sumR))
