x = "Colts"
y = "Patriots"
z = "Bills"

my_list = [x, y, z]
print(my_list)

x = "Bears"

print(my_list)

my_list = ["Colts", "Steelers", "Dolphins"]
print(my_list)

x, y, z = my_list
print(x)
print(y)
print(z)

def math(x, y, z):
    print(x,y,z)

my_list = [1,2,3]

math(*my_list)