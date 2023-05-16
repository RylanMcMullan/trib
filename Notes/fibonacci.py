x = 0 # first number
y = 1 # second number

while True:    
    if x >= 1000 or y >= 1000:
        print(x)
        print("Done")
        break
    else:
        print(x)
        x = x + y
        print(y)
        y = x + y