#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program is a better guessing number game


def main():
    loop = 0
    result = 0

    print("This program adds all the integer numbers from 0 to the number you insert.")

    integer_input = input("Insert an integer:")

    try:
        integer = int(integer_input)

        if integer > 0:
            while loop < integer:
                loop = loop + 1
                result = result + loop
            print("\n1 + ... + {0} = {1}".format(integer, result))
        else:
            print("\nThis input is invalid, please, insert a positive integer.")
    except Exception:
        print("\nThis input is invalid, please, insert an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
