# 1
def get_multiplied_digits(number):
    # 2
    str_number = str(number)
    # 3
    first = int(str_number[0])
    # 5
    if len(str_number) > 1:
        # 4
        return first * get_multiplied_digits(int(str_number[1:]))
    # 6
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
