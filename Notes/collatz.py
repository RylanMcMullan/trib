inte = int(input("Give me a positive integer: "))
print(inte)

curr_num = inte
steps = 0

while curr_num != 1:
    if curr_num % 2 == 0:
        curr_num = curr_num//2
    else:
        curr_num = curr_num * 3 + 1
        steps += 1
        print(curr_num)

