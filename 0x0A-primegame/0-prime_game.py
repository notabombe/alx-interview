#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    '''find round winner'''
    list = list(range(1, n + 1))
    players = ['Maria', 'Ben']

    for i in range(n):
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            # if already picked prime num then
            # find if num is multipl of the prime num
            if prime == -1:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
            elif num % prime == 0:
                selectedIdxs.append(idx)
        if prime == -1:
            return players[1] if players[i % 2] == players[0] else players[0]
        for idx, val in enumerate(selectedIdxs):
            del list[val - idx]
    return None


def isPrime(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        return next(
            (
                "Not prime"
                for i in range(3, int(n ** (1 / 2)) + 1, 2)
                if n % i == 0
            ),
            True,
        )
