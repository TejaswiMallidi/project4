l = []
def ispalindrome():
    for a in range(0,len(l)):
        for b in range(len(l) - 1,0):
            while(a > b):
                if(l[a] == l[b]):
                   a += 1
                   b -=1
            return l
def palindrome():
    for i in range(100,1000):
       for j in range(100,1000):
           l.append(i * j)
           if ispalindrome(): 
              return i * j
print(palindrome())

