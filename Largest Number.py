# 3. Write a function largestNum(num1, num2, num3), where the parameters are all integer values.
# The function will return the largest value of the three parameters.


def largestNum(num_1, num_2, num_3):
    return max(num_1, num_2, num_3)


print(largestNum(1, 2, 3))
print(largestNum(4, 1, 4))
print(largestNum(2, 2, 8))
