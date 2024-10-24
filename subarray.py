n=int(input())
lis=list(map(int,input().split()))
tar=int(input())
val=0
for i in range(n):
    ele=lis[i]
    for j in range(i+1,n):
        ele+=lis[j]
        if ele==tar:
            print(i+1,j+1)
            break
        if ele==tar:
            break
 
