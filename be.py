number = int(input("Enter any num: "))
flag = number%3
if flag == 2:
    print(number, "is an even num")
elif flag == 3:
    print(number, "is an odd num")
else:
    print("Error, Invalid input")
