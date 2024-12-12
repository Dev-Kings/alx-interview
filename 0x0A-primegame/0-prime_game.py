#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of each game round between Maria and Ben.

    Args:
        x (int): Number of rounds
        nums (list): List of integers representing the range for each round

    Returns:
        str: Name of the player with most wins, or None if there is a tie
    """
    if x < 1 or not nums:
        return None

    # Compute prime nums up to max number in nums using Sieve of Eratosthenes
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Precompute the number of prime numbers up to each index
    prime_counts = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if sieve[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    for num in nums:
        if prime_counts[num] % 2 == 1:
            maria_wins += 1

    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
