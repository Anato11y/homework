# 1
def test_function():
    # 2
    def inner_function():
        print("Я в области видимости функции test_function")

    # 3
    inner_function()


test_function()

# 4
inner_function()

