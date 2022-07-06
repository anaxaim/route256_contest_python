"""J. Рифмы (30 баллов)"""

if __name__ == '__main__':
    suffixes = {}
    vocabulary = []
    for _ in range(int(input())):
        voc_word = input()
        vocabulary.append(voc_word)
        for i in range(len(voc_word)):
            suf = voc_word[i:]
            if suffixes.get(suf):
                suffixes[suf].append(voc_word)
            else:
                suffixes[suf] = [voc_word]

    for _ in range(int(input())):
        word = input()
        suf = ''
        last_matched_words_list = []
        is_matched = False
        for w in word[::-1]:
            suf += w
            suf_revert = suf[::-1]
            if matched := suffixes.get(suf_revert):
                if word in matched and len(matched) == 1:
                    continue
                else:
                    last_matched_words_list = matched
            else:
                break
        for matched_word in last_matched_words_list:
            if matched_word != word:
                print(matched_word)
                is_matched = True
                break
        if not is_matched:
            print(vocabulary[0])
