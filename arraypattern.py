m = int(input("Enter the order of matrix: "))
a = [[0 for i in range(m)] for j in range(m)]
temp = 1
for i in range(0,m):
    for j in range(0,m):
        a[i][j]= temp
        temp = temp+1
    
for i in range(0,m):
    for j in range(0,m):
        print(a[i][j],sep=',',end='\t')
    print("\n")


for i in range(0,m):
    temp = i
    for j in range(0,i+1):
        if(j>=0):
            print(a[temp][j],end=',')
            temp=temp - 1      
        else: break
for i in range(1,m):
    temp = m-1
    for j in range(i,m):
        if(temp>=1):
            print(a[temp][j],end=',')
            temp = temp - 1
        else : i = i+1
        
