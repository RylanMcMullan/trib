print("Example 1")
# Python Iterables
#range(start_val, stop_val, incriment)

for i in range(1, 6, 2):
    print(i**2)

for i in "Hello World":
    print(i)

print("\nExample 2")
#break - leave loop prematurely
#continue - skip code and begin next part of loop

for i in range(1, 6, 2):
    if i**2 == 9:
        continue
    print(i**2)

for i in range(1, 6, 2):
    if i**2 == 25:
        print("Stop")
        break
    print(i**2)

print("\nExample 3")
# do stuff until test is false
i = 1
while i < 20:
    print(i*2)
    i = i + 2