def hollow_square(n):
    for row in range(n):
        for column in range(n):
            if row == 0 or row == n - 1 or column == 0 or column == n - 1:
                print('#',end = "")
            else:
                print(" ", end = "")
        print()