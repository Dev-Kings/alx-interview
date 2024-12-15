#!/usr/bin/python3
"""
Making Change Module
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given total amount.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to make change for.

    Returns:
        int: Minimum number of coins required to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any combination of coins, return -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if total == 0:
            break
        num_coins = total // coin
        coin_count += num_coins
        total -= coin * num_coins

    return coin_count if total == 0 else -1
