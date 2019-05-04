import random

def numberPicker():
    one = random.randint(0, 15)
    if one == 10:
        return 'a'
    if one == 11:
        return 'b'
    if one == 12:
        return 'c'
    if one == 13:
        return 'd'
    if one == 14:
        return 'e'
    if one == 15:
        return 'f'
    return one


def getV(l, seq):
    if l[seq] == "a":
        return 10
    if l[seq] == "b":
        return 11
    if l[seq] == "c":
        return 12
    if l[seq] == "d":
        return 13
    if l[seq] == "e":
        return 14
    if l[seq] == "f":
        return 15
    return l[seq]


def sixPick(one, two, three, four, five, six):
    num = random.randint(0, 5)
    if num == 0:
        one = numberPicker()
    if num == 1:
        two = numberPicker()
    if num == 2:
        three = numberPicker()
    if num == 3:
        four = numberPicker()
    if num == 4:
        five = numberPicker()
    if num == 5:
        six = numberPicker()
    a = '#' + str(one) + str(two) + str(three) + str(four) + str(five) + str(six)
    ''.join(a)
    return a
