import timeit
from typing import List, Tuple
import matplotlib.pyplot as plt


def fact_recursive(n: int) -> int:
    """
    Вычисляет факториал числа рекурсивным способом.

    :param n: неотрицательное целое число
    :return: факториал n
    :raises ValueError: если n < 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    """
    Вычисляет факториал числа итеративным способом (через цикл).

    :param n: неотрицательное целое число
    :return: факториал n
    :raises ValueError: если n < 0
    """
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def benchmark(
    values: List[int],
    repeats: int = 5,
    number: int = 1
) -> Tuple[List[float], List[float]]:
    """
    Проводит бенчмарк двух реализаций факториала.

    :param values: список входных значений n
    :param repeats: количество повторов для усреднения
    :param number: число вызовов функции за один замер
    :return: времена для рекурсивной и итеративной версий
    """
    rec_times = []
    iter_times = []

    for n in values:
        rec_time = timeit.repeat(
            stmt=lambda: fact_recursive(n),
            repeat=repeats,
            number=number
        )
        iter_time = timeit.repeat(
            stmt=lambda: fact_iterative(n),
            repeat=repeats,
            number=number
        )

        rec_times.append(sum(rec_time) / repeats)
        iter_times.append(sum(iter_time) / repeats)

    return rec_times, iter_times


def plot_results(
    values: List[int],
    rec_times: List[float],
    iter_times: List[float]
) -> None:
    """
    Строит график зависимости времени вычисления
    от размера входного числа.

    :param values: значения n
    :param rec_times: времена рекурсивной версии
    :param iter_times: времена итеративной версии
    """
    plt.figure(figsize=(8, 5))
    plt.plot(values, rec_times, marker='o', label="Recursive")
    plt.plot(values, iter_times, marker='o', label="Iterative")

    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Factorial: recursive vs iterative")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # ===== Фиксированный набор чисел =====
    test_values = list(range(1, 21))  # одинаковый для всех прогонов

    # ===== Чистый бенчмарк одного вызова =====
    print("Single call benchmark (n=10):")
    print(
        "Recursive:",
        timeit.timeit(lambda: fact_recursive(10), number=1)
    )
    print(
        "Iterative:",
        timeit.timeit(lambda: fact_iterative(10), number=1)
    )

    # ===== Усреднённый бенчмарк =====
    rec, itr = benchmark(test_values, repeats=10, number=1)

    # ===== Визуализация =====
    plot_results(test_values, rec, itr)
