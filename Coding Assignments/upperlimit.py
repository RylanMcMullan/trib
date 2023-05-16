upperLimit = input("Give me a number: ")
i = int(upperLimit)

def divisible(str): # check if the number is divisible by 3 and 2
    if (int(str) % 2 == 0 and int(str) % 3 == 0):
        return "divisible by both"
    elif (int(str) % 2 == 0 and int(str) % 3 != 0):
        return "divisible by 2"
    elif (int(str) % 2 != 0 and int(str) % 3 == 0):
        return "divisible by 3"
    else:
        return "divisible by none"

print(f"Upper Limit is {upperLimit}\nNumber        Divisible by 2 and 3?") # printing table content

while True: # print every number from upper limit down to 1 and what it's divisible by
    print(f"The number {i} is: {divisible(i)}")
    
    i = i - 1

    if i > 0:
        continue
    else:
        break