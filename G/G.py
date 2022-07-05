"""G - Возможные друзья"""

from collections import Counter

if __name__ == '__main__':
    n, m = input().split()              # пользователи, пары друзей
    friends = {}
    for _ in range(int(m)):
        f1, f2 = input().split()  # очередная пара друзей
        f1, f2 = int(f1), int(f2)
        if friends.get(f1):
            friends[f1].add(f2)
        else:
            friends[f1] = {f2}

        if friends.get(f2):
            friends[f2].add(f1)
        else:
            friends[f2] = {f1}
    for i in range(1, int(n) + 1):
        if not friends.get(i):
            friends[i] = set()
    friends_sorted = dict(sorted(friends.items()))

    for idx, val in friends_sorted.items():
        if val:
            rec_friends = []
            for fr in val:
                maybe_fr = friends_sorted[fr]
                m_f = [f for f in maybe_fr if f not in val]
                rec_friends.extend(m_f)
            count_friends = Counter(rec_friends)
            if count_friends.get(idx):
                count_friends.pop(idx)
            if count_friends:
                max_value = max(count_friends.values())

                max_rec_friends = set()
                for i, v in count_friends.items():
                    if v == max_value:
                        max_rec_friends.add(i)
                print(*sorted(max_rec_friends))
            else:
                print(0)
        else:
            print(0)
# если список друзей пуст - 0, иначе id_ друзей в возрастающем порядке
"""
8 6
4 3
3 1
1 2
2 4
2 5
6 8

вых
4
3
2
1
1 4
0
0
0
=======
8 10
1 2
1 3
1 4
4 3
3 2
2 4
1 8
5 6
7 6
5 7

вых
0
8
8
8
0
0
0
2 3 4
"""
