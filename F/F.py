"""F - Отрезки времени"""
from datetime import datetime
from itertools import chain


def string_to_time(string: str) -> datetime.time:
    return datetime.strptime(string, '%H:%M:%S').time()


def is_valid(ranges: list) -> bool:
    sorted_ranges = sorted(ranges, key=lambda r: r[0])

    # проверяем, что нет пересечения на границах
    last = sorted_ranges[0][1]
    for s in sorted_ranges[1:]:
        if s[0] == last:
            return False
        last = s[1]

    # проверяем, что нет вхождения
    return list(chain(*sorted_ranges)) == sorted(chain(*sorted_ranges))


if __name__ == '__main__':
    t = input()         # наборы
    for _ in range(int(t)):
        n = int(input())     # кол-во отрезков
        list_of_dates = []
        left_more_than_right = False
        broken = False
        for i in range(n):
            dt_left, dt_right = input().split('-')
            try:
                dt_left_to_time = string_to_time(dt_left)
                dt_right_to_time = string_to_time(dt_right)
                if dt_left_to_time > dt_right_to_time:  # проверяем что левая граница не позже правой
                    left_more_than_right = True
                list_of_dates.append([dt_left_to_time, dt_right_to_time])
            except:
                broken = True
                continue
        if not broken and is_valid(list_of_dates) and not left_more_than_right:
            print('YES')
        else:
            print('NO')
