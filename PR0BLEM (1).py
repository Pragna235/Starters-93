# cook your dish here
def equal(n,m):
    if(n%2==0 and m%2!=0) or (n%2!=0 and m%2==0):
        return False
    
    while(n>=0 and m>=0):
        if(n==m):
            return True
        elif(n<m):
            n+=3
            m-=1 
        else:
            n-=1 
            m+=1
    return False
    
for t in range(int(input())):
    n,m=map(int,input().split())
    if(equal(n,m) == True):
        print("YES")
    else:
        print("NO")
        
        
 
        
