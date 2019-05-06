a,l = int(input()),[]
if a < 12 or a % 10 <= a // 10 : print('invalid input')
l = [i for i in range(12 , 100) if i %10 > i // 10]
for i in range(len(l) - 1):
  if a == l[i] : print(l[i - 1],l[i + 1])
if a == l[len(l) - 1]:print(l[len(l) - 2],l[0])

