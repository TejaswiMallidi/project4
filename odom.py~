n = int(input())
l = []
l1 = []
if n % 10 == 0 or n > 6789 or n < 0:
    print('invalid input')
else :
    for j in range(1,6790):
         while n != 0:
             rem = n % 10
             l.append(rem)
             n //= 10
         if l[0] > l[1]:
             if l[1] > l[2]:
                 if l[2] > l[3]:
                      l1.append(l)
         else:
             print('invalid input')
    for i in range(len(l1)-1):
         print(l1[i-5],l1[i-4],l1[i-3],l1[i-2],l[i-1],l1[i+1],l1[i+2],l1[i+3],l1[i+4],l1[i+5])
