def ranju(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(max(i,j, n-i+1, n-j+1), end="")
        print()
n=int(input())
ranju(n)

