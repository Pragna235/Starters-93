# cook your dish here
def equal(n,m):
    if(n%2==0 and m%2!=0) or (n%2!=0 and m%2==0):
        return False
    while(n>=0 and m>=0):
        n=n-1
        m=m+1 
        if(n==m):
            return True
        m=m-1
        n=n+3
        if(n==m):
            return True
    return False
    
for t in range(int(input())):
    n,m=map(int,input().split())
    if(equal(n,m) == True):
        print("YES")
    else:
        print("NO")
        
        
 
        
