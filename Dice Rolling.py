# Write a function sumDice(Dice, numRolls), where Dice simulate a dice of Dice sides and numRolls represent the number
# of times the dice is rolled. The function will return the sum of rolling the dice numRolls times.

import random


def sumDice(Dice, Numrolls):
    sum_dice = 0
    for x in range(0, Numrolls):
        sum_dice = sum_dice + random.randint(1, Dice)
    return sum_dice

print(sumDice(2, 3))
print(sumDice(2, 3))
print(sumDice(2, 3))