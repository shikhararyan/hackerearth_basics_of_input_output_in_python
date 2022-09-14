t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int,input().split( )))
    A.sort()
   
    if len(A) == 3:
        print(A[2] - A[0])


    if len(A) == 2:
        print(A[1] - A[0])


    if len(A) % 2 == 0 and len(A) != 2:
        c = []
        for i in range(int(len(A)/2)):
            c.append(A[i])
        fir = c[0] + c[1]
        d = []
        for i in range(int(len(A)/2),int(len(A))):
            d.append(A[i])
        las = d[-1] +d[-2]
        print(las - fir)   
    
    if len(A) % 2 != 0 and len(A) != 3:
        c = []
        for i in range(int(len(A)/2 + 1)):
            c.append(A[i])
        fir = c[0] + c[1]
        d = []
        for i in range(int(len(A)/2 + 1),int(len(A))):
            d.append(A[i])
        las = d[-1] +d[-2]
        print(las - fir)   

    
