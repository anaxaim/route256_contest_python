"""E. Отчет"""


def is_valid(articles: list):
    already_watched = set()
    current_val = articles.pop(0)
    for i in articles:
        if current_val != i:
            already_watched.add(current_val)
        if i in already_watched:
            print('NO')
            break
        current_val = i
    else:
        print('YES')


if __name__ == '__main__':
    t = input()         # наборы
    for _ in range(int(t)):
        input()  # кол-во отчетов
        a = [int(i) for i in input().split()]
        is_valid(a)
