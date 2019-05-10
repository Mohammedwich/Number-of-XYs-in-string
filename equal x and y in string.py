def is_x_y_equal(string):
    x, y = 0, 0
    for c in string:
        if c == 'x':
            x += 1
        elif c == 'y':
            y += 1
    if x == y:
        return True
    else:
        return False


xy_string = input("Input a string of x's and y's to check if it has the same number of x's and y's:\n")
if is_x_y_equal(xy_string):
    print("There is an equal number of x's and y's in this string.")
else:
    print("The number of x's and y's is different")
