import sys


def solve():
    # Зчитуємо всі дані
    input_data = sys.stdin.read().split()

    idx = 0
    while idx < len(input_data):
        # Отримуємо наступні 5 чисел
        nums = [
            int(input_data[idx]),
            int(input_data[idx + 1]),
            int(input_data[idx + 2]),
            int(input_data[idx + 3]),
            int(input_data[idx + 4])
        ]
        idx += 5

        if nums == [0, 0, 0, 0, 0]:
            break

        # Масив для відстеження юзаних чисел
        used = [False] * 5

        # Рекурсивна функція перебору
        def backtrack(current_val, count):
            # Базовий випадок: якщо використали всі 5 чисел
            if count == 5:
                return current_val == 23

            # Перебираємо всі 5 чисел
            for i in range(5):
                if not used[i]:
                    # Позначаємо число як використане
                    used[i] = True

                    if count == 0:
                        # Якщо це перше число, операцій ще немає, просто беремо його
                        if backtrack(nums[i], 1):
                            return True
                    else:
                        # Пробуємо всі три операції з наступним числом
                        if backtrack(current_val + nums[i], count + 1):
                            return True
                        if backtrack(current_val - nums[i], count + 1):
                            return True
                        if backtrack(current_val * nums[i], count + 1):
                            return True

                    # "Повернення" (backtrack) - знімаємо позначку для наступних ітерацій
                    used[i] = False

            return False

        # Запускаємо перебір, починаючи з 0 чисел і початкового значення 0
        if backtrack(0, 0):
            print("Possible")
        else:
            print("Impossible")


if __name__ == "__main__":
    # Щоб уникнути перевищення ліміту глибини рекурсії
    sys.setrecursionlimit(2000)
    solve()