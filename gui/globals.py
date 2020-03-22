x =1
print(x)

class a():
    def setX(self):
        global x
        x = 2
        print(f"in class{x}")

print(x)
outclass = a()
outclass.setX()
print(x)

class b():
    def printx(self):
        print(f"in class b {x}")

print (x)
outclass2 = b()
outclass2.printx()
