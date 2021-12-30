import numpy as np

def random_predict(number:int=1) -> int:

    number = np.random.randint(1, 101)
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)

        if predict_number == number:
            break

    return count


def score_game(random_predict) -> int:
    """Mean number of tries in 1000 runs our algorithm guesses the
    number in.

    Args:
        random_predict([type]): Guessing function

    Returns:
        int: Mean guessing tries.
    """

    counts = list()
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        counts.append(random_predict(number))

    score = int(np.mean(counts))
    print(f"Your algorithm mean guess count is {score}")
    return score


if __name__ == "__main__":
    score_game(random_predict)
