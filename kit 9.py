def print_series(start, end, step, separator=", "):
    for i in range(start, end + 1, step):
        print(i, end=separator)


print_series(1, 15, 2)
print()


print_series(2, 17, 3)
print()


print_series(3, -30, -10)
print()


print_series(4, 55, 8)
