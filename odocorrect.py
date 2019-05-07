def numbers(a):
    l = []
    for i in range(10 **(a -1),10 ** a):
        p = list(str(i))
        count = 0   
        for j in range(len(p) - 1):
            if p[j] < p[j + 1]:
                count += 1
            if count == len(p) - 1:
                l.append(i)
    return l
def next_num(a,n):
    l = numbers(a)
    
    k = l.index(n)
    if k == len(l) - 1:
        return l[0]
    return l[k + 1]

def pre_num(a,n):
    l  = numbers(a) 
    k = l.index(n)
    if k == 0:
        return l[len(l) - 1]
    return l[k - 1]

size = int(input())
num = int(input())
print(pre_num(size,num),next_num(size,num))
