num = input()                  # Reading input from STDIN
lis=(num.split())
k= 0
for i in range(int(lis[0]),int(lis[1])+1):
    if  i % int(lis[2]) == 0:
        k= k+1
print(k)








#another approach is by splitting the input into three seperate variables 
l,r,k= (input().split())                 # Reading input from STDIN
count = 0
for i in range(int(l),int(r)+1):
        if i % int(k) == 0:
                count = count +1
        else:
                pass
print(count)
