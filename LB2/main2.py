def guess_number(numbers, guess, method: str) -> list[int] | None:
    """Выполняет поиск числа в последовательности.

    Функция поддерживает два режима:
    - 'bin' — бинарный поиск (эффективный, O(log n))
    - 'lin' — линейный поиск (медленный перебор, O(n))

    Аргументы:
        numbers: range или список чисел (могут быть неотсортированы)
        guess: число, которое нужно найти
        method: тип поиска ('bin' или 'lin')

    Возвращает:
        [угаданное_число, количество_сравнений] — если найдено
        None — если не найдено

    Пример:
        guess_number(list(range(1, 101)), 73, 'bin')
        [73, 7]
    """

    # --- Определяем порядок ---
    if isinstance(numbers, range):
        ascending = numbers.step > 0
    else:
        # Проверяем, отсортирован ли список
        ascending = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
        descending = all(numbers[i] >= numbers[i + 1] for i in range(len(numbers) - 1))

        if not (ascending or descending):
            numbers = sorted(numbers)
            ascending = True

    # --- Бинарный поиск ---
    if method == "bin":
        left, right = 0, len(numbers) - 1
        count = 0

        while left <= right:
            count += 1
            mid = (left + right) // 2
            val = numbers[mid]

            if val == guess:
                return [guess, count]

            if ascending:
                if val < guess:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if val < guess:
                    right = mid - 1
                else:
                    left = mid + 1

        return None

    # --- Линейный поиск ---
    else:
        for i, num in enumerate(numbers, start=1):
            if num == guess:
                return [guess, i]
        return None
