#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Nov 2019
# This program calculates the surface area of a tetrahedron

import math


def sa_calculator(height):
    # calculates the volume

    # process
    sa = math.sqrt(3) * height**2
    return round(sa, 2)


def main():
    # This is asks for the user input

    # Welcomes user
    print("This program calculates the surface area of a tetrahedron. ")

    while True:
        try:
            # input
            height = float(input("What is the lenght: "))
            # runs volume_calculator()
            sa = sa_calculator(height=height)
            # output
            print("\nThe surface area is " + str(sa) + " cm2.")
            break

        except ValueError:
            print("Please put in integer.\n")


if __name__ == "__main__":
    main()
