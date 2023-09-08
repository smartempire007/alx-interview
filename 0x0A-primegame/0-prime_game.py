#!/usr/bin/python3
"""Prime Game.

This code defines a game where two players, Maria and Ben, take turns.
The goal of the game is to determine the winner based on a set of numbers.
Each player selects a prime number, and removes all multiples of that
prime number from the remaining set of numbers. The player who
cannot make a move loses the round. The code determines the overall winner
by counting the number of rounds won by each player.

"""


def isWinner(x, nums):
    """Main Prime game function. Determine the winner.

    Args:
        x (int): A positive integer representing the number of rounds to
        be played.
        nums (list): A list of integers representing the numbers in each round.

    Returns:
        str or None: The name of the winner ("Maria" or "Ben") or None if input
        validation fails.

    """

    # Check for edge cases:
    try:
        assert x and type(x) == int and x > 0
        assert nums and type(nums) == list and len(nums) != 0
        for n in nums:
            # n can be 0, in which case the round is skipped
            assert type(n) == int
    except Exception:
        return None

    def is_prime(n):
        """Helper function to check if a number is prime.

        Args:
            n (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.

        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def game(n):
        """Helper function to determine who wins the round.

        If n is 1, Ben wins automatically since Maria cannot make a move.

        Args:
            n (int): The number in the current round.

        Returns:
            str: The name of the winner ("Maria" or "Ben").

        """
        primes = [i for i in range(1, n + 1) if is_prime(i)]
        non_primes = [i for i in range(1, n + 1) if not is_prime(i)]

        turn = "Maria"
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            non_primes = [np for np in non_primes if np % prime != 0]

            if primes or non_primes:
                turn = "Ben" if turn == "Maria" else "Maria"
            else:
                return turn
        return "Ben" if turn == "Maria" else "Maria"

    marias = 0
    bens = 0

    for n in nums:
        winner = game(n)
        if winner == "Maria":
            marias += 1
        else:
            bens += 1

    if marias > bens:
        return "Maria"
    elif bens > marias:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner:", isWinner(3, [4, 5, 1]))
