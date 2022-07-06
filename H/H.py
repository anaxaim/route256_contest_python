"""H. Валидация карты (25 баллов)"""


def change_letter(hexagon, line_index, char_index, letter, num_of_lines, num_of_chars):
    in_lines = 0 <= line_index < num_of_lines
    in_chars = 0 <= char_index < num_of_chars

    if in_lines and in_chars and hexagon[line_index][char_index] == letter:
        hexagon[line_index][char_index] = '.'
        for pos in ((-1, -1), (-1, 1), (1, -1), (1, 1), (0, 2), (0, -2)):
            l_idx = line_index + pos[0]
            ch_idx = char_index + pos[1]
            change_letter(hexagon, l_idx, ch_idx, letter, num_of_lines, num_of_chars)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = input().split()
        n = int(n)

        hexagon_card = [list(input()) for _ in range(n)]

        used_letters = set()
        is_valid = True

        for line_idx, line in enumerate(hexagon_card):
            for char_idx, char in enumerate(line):
                if char in used_letters:
                    is_valid = False
                    break
                if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    used_letters.add(char)
                    change_letter(hexagon_card, line_idx, char_idx, char, n, int(m))
            if not is_valid:
                break
        print('YES' if is_valid else 'NO')
