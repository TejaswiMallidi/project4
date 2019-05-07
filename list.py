class myclass():
    def __init__(self, *args):
        self.l = []
        for i in args:
            self.l.append(i)
    def __repr__(self):
        return str(self.l)
    def sqr(self):
        return[i ** 2 for i in self.l]

k = myclass(10,8,20,27,21)
p = myclass.sqr(k)
print(k,p)
