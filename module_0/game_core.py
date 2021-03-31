import math
import numpy as np


def game_core_impl(number):
    """Implementation of bisection method"""
    count = 0   # Steps counter
    # Range boundaries. Values are taken from task definition (constant)
    BOTTOM_BOUND = 1
    UPPER_BOUND = 101
    while True:
        count += 1
        # Range center
        center = math.floor((UPPER_BOUND - BOTTOM_BOUND) / 2)
        # Target value for current step
        current_value = BOTTOM_BOUND + center
        if current_value == number:
            break
        if current_value < number:
            BOTTOM_BOUND += center
        else:
            UPPER_BOUND -= center
    return count


# This function is taken from task definition
def score_game(game_core):
    # Range boundaries. Values are taken from task definition (constant)
    BOTTOM_BOUND = 1
    UPPER_BOUND = 101
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(BOTTOM_BOUND, UPPER_BOUND, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_impl)
