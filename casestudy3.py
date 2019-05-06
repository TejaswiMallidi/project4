l1 = input()
l2 = input()
l3 = input()
l4 = input()
l5 = input()

l = [list(l1),list(l2),list(l3),list(l4),list(l5)]
l6 = (input())
b = list(l6)
c = 1

for i in range(0,5):
    for j in range(0,5):
        if l[i][j]== ' ':
            m,n = i,j

for k in range(len(b)):
    if m == 0 and b[k] == 'A':
        c = 0
        print("This puzzle has no final configuration")
        break
    if m == 4 and b[k] == 'B':
        c = 0
        print("This puzzle has no final configuration")
        break
    if n == 0 and b[k] == 'L':
        c = 0
        print("This puzzle has no final configuration")
        break
    if n == 4 and b[k] == 'R':
        c = 0
        print("This puzzle has no final configuration")
        break
      
    if b[k] == 'A':
        l[m][n],l[m-1][n] = l[m-1][n],l[m][n]
        m,n = m-1,n
    if b[k] == 'B':
        l[m][n],l[m+1][n] = l[m+1][n],l[m][n]
        m,n = m+1,n
    if b[k] == 'R':
        l[m][n],l[m][n+1] = l[m][n+1],l[m][n] 
        m,n= m,n+1   
    if b[k] == 'L':
        l[m][n],l[m][n-1] =  l[m][n-1],l[m][n] 
        m,n = m,n-1 

if c != 0:
   for i in range(0,5):
       for j in range(0,5):
           print(l[i][j],end = ' ')
   print()
