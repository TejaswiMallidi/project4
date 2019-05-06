def fun(num):
    fact = 1
    for i in range(2,num+1):
         fact = fact * i
    return fact

def sum(fact):
    num = fun(fact)
    sum = 0
    while num > 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
    return sum
print(sum(100))
