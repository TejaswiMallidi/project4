a =int(input())
l = []
for i in range(10 ** (a - 1) ,10 ** a ):
    p = list(str(i))
    count = 0
    for j in range(len(p)-1):
        if(p[j] < p[j + 1]):
            count += 1
        if count == len(p) - 1:
            l.append(i) 

print(l)
