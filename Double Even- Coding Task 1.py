# 1. Write a function doubleEven(n), where n is a non - negative integer.The function will return double the value of n
#  if n is even, otherwise it will return -1. doubleEven(10) returns 20 doubleEven(5) returns - 1


def doubleEven(n):
    if n >= 1:
        if n % 2 == 0:
            return n * 2
        else:
            return -1
    else:
        print("Please enter a valid input.")
        exit()


print(doubleEven(10))
print(doubleEven(5))