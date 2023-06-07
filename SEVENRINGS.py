# cook your dish here
for t in range(int(input())):
    n,x = map(int,input().split())
    total = str(n*x)
    if(len(total) == 5 and total[0]!=0):
        print("YES")
    else:
        print("NO")