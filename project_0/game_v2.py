import numpy as np
from typing import Callable

def guess_binary(number: int) -> int:
    """Guess the passed number by halving the distance between 
    a random initial number and the passed *number*.

    Args:
        number: A value to guess.

    Returns:
        Number of guesses made in order to guess the *number* argument.
    """

    # No need to select a random value for binary search.
    guessing_max = 100
    guessing_min = 0
    count = 0

    while True:
        count += 1

        # This must be handled explicitly since guessing_max will never be reached
        # due to division result truncation.
        if guessing_max - guessing_min == 1:
            guessed = guessing_max
        else:
            guessed = guessing_min + (guessing_max - guessing_min) // 2

        if guessed == number:
            break

        if guessed > number:
            guessing_max = guessed
        else:
            guessing_min = guessed

    return count


def score_game(guess_function: Callable[[int], int]) -> int:
    """Get the guess number mean value over 1000 runs.

    Args:
        guess_function: Guessing function.

    Returns:
        int: Guessing tries mean value over 1000 runs.
    """

    counts = list()
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        counts.append(guess_function(number))

    score = int(np.mean(counts))
    print(f"Your algorithm mean guess count is {score}")
    return score


if __name__ == "__main__":
    score_game(guess_binary)
