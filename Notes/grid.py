"""
grid = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
"""
grid = [
    [0] * 3,
    [1] * 3,
    [2] * 3
]

for i in range(len(grid)):
    print(grid[i])


perfect_squares = []
for i in range(1, 10, 1):
    perfect_squares.append(i**2)
print(perfect_squares)


# shorter version
perfect_squares = [i**2 for i in range(1, 10, 1)]
print(perfect_squares)

div_list = []
for i in range(0, 11):
    div_list.append(i % 2 == 0 or i % 3 == 0)
    print(div_list)

# shorter version
div_list = [i % 2 == 0 or i % 3 == 0 for i in range(0, 11)]


div_list = []
for i in range(0, 11):
    if (i % 2 == 0 or i % 3 == 0):
        div_list.append(i)
    print(div_list)

# shorter version
div_list = [i for i in range(0, 11) if i % 2 == 0 or i % 3 == 0]

def func(x, y, z):
    print(x + y + z)

my_list = [1,2,3]

func(*my_list) # * splits items in list
