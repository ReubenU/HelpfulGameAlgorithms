# Author:   Reuben Unicruz
# Date:     3/12/2019


# For displaying a car's
# position in a race in
# string format.
def strPosition(intPos):
    spcCase = {1:'st',2:'nd',3:'rd'}

    ones = intPos%10
    tens = intPos%100

    if (ones not in spcCase or tens in range(10,20)):
        return ('%ith')%(intPos)

    return ('%i%s')%(intPos, spcCase[ones])
