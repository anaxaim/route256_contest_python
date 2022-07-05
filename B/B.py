"""B - парное программирование"""

from collections import defaultdict


def get_next_dev_pair(m: list, m_d: dict) -> (list, dict):
    first_dev, second_dev = m[0], m[1]
    second_dev_idx = 1
    div = abs(first_dev - second_dev)

    if next_m := m[2:]:
        for idx, val in enumerate(next_m):
            new_div = abs(first_dev - val)
            if new_div < div:
                div = new_div
                second_dev = val
                second_dev_idx = idx + 2

    m.pop(second_dev_idx)
    m.pop(0)

    print(m_d.get(first_dev).pop(0) + 1, m_d.get(second_dev).pop(0) + 1)

    return m, m_d


if __name__ == '__main__':
    t = int(input())                    # кол-во наборов
    for _ in range(t):
        input()                         # кол-во разрабов (четное)
        mastery = [int(m) for m in input().split()]  # мастерство каждого из n разрабов
        indexes = defaultdict(list)
        for i, v in enumerate(mastery):
            indexes[v].append(i)

        while mastery:
            mastery, indexes = get_next_dev_pair(mastery, indexes)
