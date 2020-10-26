import math
import numpy as np


def game_core(number):
    """Implementation of bisection method"""
    count = 0   # Steps counter
    # Range boundaries. Values are taken from task definition
    a = 1
    b = 100
    while True:
        count += 1
        # Range center
        i = math.floor((b - a) / 2)
        # Target value for current step
        r = a + i
        if r == number:
            break
        if r < number:
            a += i
        else:
            b -= i
    return count


# This function is taken from task definition
def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
