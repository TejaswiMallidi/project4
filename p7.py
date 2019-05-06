k = pow(2,1000)
print(k)
sum = 0
rem = 0
while k != 0:
    rem = k % 10
    sum = sum + rem
    k //= 10
print(sum)
