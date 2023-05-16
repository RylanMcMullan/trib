a = ["Colts", "Steelers"]
b = ["Colts", "Steelers"]
print(a == b)

c = b
print(c == b)

print(a is b)

c = b
print(c is b)

a = ["Colts", "Steelers"]
b = ["Colts", "Steelers"]
print(id(a))
print(id(b))

a = ["Colts", "Steelers"]
b = a
print(id(a))
print(id(b))

a = ("Colts", "Steelers")
b = ("Colts", "Steelers")
print(a is b)

a = "Colts"
b = "Colts"
print(a is b)

a = 500
a = 500
print(a is b)

class DryErase:
    def __init__(self, color, size, tip):
        self.color = color
        self.size = size
        self.tip = tip
    def draw(self):
        print("You drew a line on the board")


marker1 = DryErase("blue", "medium", "normal")
print(marker1.color)

marker1.draw()