def max_number(*args):
    num = args[0]
    for i in args:
        if i < num:
            num = i
    print(num)
max_number(23, 51, 8, 18, 20)

# 8