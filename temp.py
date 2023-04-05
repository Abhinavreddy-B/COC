class F1:
    def __init__(self):
        self.a = 1

    def printclass(self):
        print(self.a)

class F2(F1):
    def __init__(self):
        self.a = 3

f2 = F2()

f2.printclass()