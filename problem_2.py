#!/usr/bin/python3
"""
Function to return max power needed for the list of fields and  water towers
"""
tower = Towers[1, 4, 9]
field = Fields[1, 2, 3, 4]
distance = []


def Waterpump_strength:
    """
    finds the distance between fields and water pumps
    returns the greatest distance hence max power
    """
    for i in tower:
        for j in field:
            if i > j:
                d = i - j
        distance.append(d)
    return max(distance)
