#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max = 0
    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - price
            if max == 0 or profit > max:
                max = profit
    return max


stocks = [1050, 270, 1540, 3800, 2]
print(find_max_profit(stocks))
