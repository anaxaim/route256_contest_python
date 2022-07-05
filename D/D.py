"""D - Подсказчик паролей"""

vowels = ['e', 'u', 'i', 'o', 'a', 'y']


def get_alphas_and_digits(password: str) -> (str, str):
    alphas = ''
    digits = ''
    for p in password:
        if p.isdigit():
            digits += p
        else:
            alphas += p
    return alphas, digits


def has_one_upper(password: str) -> bool:
    return password.lower() != password


def has_one_lower(password: str) -> bool:
    return password.upper() != password


def has_one_vowel(password: str) -> bool:
    ps = password.lower()

    for v in vowels:
        if v in ps:
            return True
    return False


def has_one_consonant(password: str) -> bool:
    ps = password.lower()

    for i in ps:
        if i not in vowels:
            return True
    return False


def set_secure(p: str) -> str:
    secure_pass = p
    alphas, digits = get_alphas_and_digits(p)

    check_upper = True
    check_lower = True
    check_cons = True

    if not digits:
        secure_pass += '1'

    if not has_one_vowel(alphas):
        if not has_one_upper(alphas):
            secure_pass += 'A'
            check_upper = False
        else:
            secure_pass += 'a'
            check_lower = False

    if not has_one_upper(alphas) and check_upper:
        if not has_one_vowel(alphas):
            secure_pass += 'A'
        else:
            secure_pass += 'B'
            check_cons = False

    if not has_one_consonant(alphas) and check_cons:
        secure_pass += 'b'
        check_lower = False

    if not has_one_lower(alphas) and check_lower:
        if not has_one_vowel(alphas):
            secure_pass += 'a'
        else:
            secure_pass += 'b'

    return secure_pass


if __name__ == '__main__':
    t = input()         # пользователи
    for _ in range(int(t)):
        print(set_secure(input()))

"""
вх данные
5
passw0rd
2
aq
Ay0
3xE

вых данные
passw0rdD
2lO
aqF2
Ay0c
3xE
"""

"""
5
a
Y
z
X
0

"""
