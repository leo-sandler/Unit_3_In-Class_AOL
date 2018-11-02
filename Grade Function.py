# Write a function grade(percent), where percent is a number given as a percentage. The function will return a string
#  that represents the letter grade for the percentage. Note: The function will return the string
# ‘error’ if the parameter is invalid


def grade(percent):
    if 79 >= percent >= 65:
        return "C"
    elif 89 >= percent >= 80:
        return "B"
    elif 100 >= percent >= 90:
        return "A"
    elif 65 > percent > -1:
        return "F"
    elif percent >= 101:
        return "Error"
    else:
        return "Error"


print(grade(100) + " was your grade.")
print(grade(99) + " was your grade.")
print(grade(89) + " was your grade.")
print(grade(64) + " was your grade.")
print(grade(20) + " was your grade.")
print(grade(101))
print(grade(-1))
print()