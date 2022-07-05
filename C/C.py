"""С - Оповещения"""

if __name__ == '__main__':
    n, q = input().split()          # пользователи / запросы
    gl = 0
    counter = 1
    users = {user: 0 for user in range(1, int(n) + 1)}
    for _ in range(int(q)):
        t, id_ = input().split()    # тип запроса / id пользователя
        t, id_ = int(t), int(id_)   # (1 - отправить оповещение / 2 - вывести оповещение) | id_  (0 - глобальный)
        if t == 1:
            if id_ != 0:
                users[id_] = counter
            else:
                gl = counter
            counter += 1
        else:
            print(max(gl, users[id_]))
