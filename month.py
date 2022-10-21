#!/usr/bin/env python3
# Created by : Patrice Pat-Odita
# Created on : Oct 17, 2022
# This program asks the user for a number between 1 and 12
# then tells them what month is represented by that number.

# state the month selected as a string
def find_month(month):
    months = {
        1: "{} represents January.".format(month),
        2: "{} represents February.".format(month),
        3: "{} represents March.".format(month),
        4: "{} represents April.".format(month),
        5: "{} represents May.".format(month),
        6: "{} represents June.".format(month),
        7: "{} represents July.".format(month),
        8: "{} represents August.".format(month),
        9: "{} represents September.".format(month),
        10: "{} represents October.".format(month),
        11: "{} represents November.".format(month),
        12: "{} represents December.".format(month),
    }
    # handle the error case
    return months.get(month, "Error. {} does not represent a month.".format(month))


# Calls the function
if __name__ == "__main__":
    user_month = int(input("Enter the number for a month" "(i.e 2 for February):"))
    print(find_month(user_month))
