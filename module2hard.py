def find_result(n):
    result = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result.append((i, j))
    return result


n = int(input("Введите число в первом поле: "))
if n > 2 and n < 21:
    result = find_result(n)
    if result:
        for result_ in result:
            print(f"{result_[0]}{result_[1]}", end='')
else:
    print("Веденное число должно быть от 3 до 20 ")
