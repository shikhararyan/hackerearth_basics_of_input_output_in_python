num = input()                  # Reading input from STDIN
lis=(num.split())
k= 0
for i in range(int(lis[0]),int(lis[1])+1):
    if  i % int(lis[2]) == 0:
        k= k+1
print(k)
