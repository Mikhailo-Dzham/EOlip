import sys


def solve():
    input_data = sys.stdin.read().split()

    it = iter(input_data)
    for n_str in it:
        try:
            m_str = next(it)
            m = int(m_str)
        except StopIteration:
            break

        memo = {}

        def get_max_product(idx, parts_left):

            if parts_left == 1:
                return int(n_str[idx:])

            state = (idx, parts_left)
            if state in memo:
                return memo[state]

            max_val = -1

            limit = len(n_str) - parts_left + 1

            for i in range(idx + 1, limit + 1):
                current_part = int(n_str[idx:i])

                res = get_max_product(i, parts_left - 1)

                if res != -1:
                    current_product = current_part * res
                    if current_product > max_val:
                        max_val = current_product

            memo[state] = max_val
            return max_val

        print(get_max_product(0, m))


if __name__ == '__main__':
    solve()