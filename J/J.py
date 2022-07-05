"""J. Рифмы (30 баллов)"""

if __name__ == '__main__':
    list_of_words = [input() for _ in range(int(input()))]

    for _ in range(int(input())):
        word = input()
        rifm = {}
        already_printed = False
        for w in list_of_words:
            if word != w:
                if len(word) == 1:
                    if word == w[-1]:
                        if len(w) > 1:
                            print(w)
                        else:
                            print(list_of_words[0])
                        already_printed = True
                        break
                else:
                    w_copy = list(w)
                    count = 0
                    for sym in word[::-1]:
                        last_sym = w_copy.pop()
                        count += 1
                        if last_sym == sym:
                            rifm[w] = count
                        else:
                            break
                        if rifm[w] == len(word) or not w_copy:
                            break

        if not already_printed:
            if rifm:
                m = max(rifm.values())
                for k, v in rifm.items():
                    if v == m:
                        print(k)
                        break
            else:
                print(list_of_words[0])
