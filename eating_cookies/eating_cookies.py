#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(num, cache={}):
    # base case
    if num <= 1:
        return 1

    elif num == 2:
        return 2

    elif num in cache:
        return cache[num]

    else:
        value = eating_cookies(num - 1) + eating_cookies(num -
                                                         2) + eating_cookies(num - 3)
        cache[num] = value
        print(value)
        return value


print(eating_cookies(3))

# print(eating_cookies(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
