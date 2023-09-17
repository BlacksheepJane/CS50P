while True:
    try:
        s = input("Fraction:").split("/")
        a, b = int(s[0]), int(s[1])
        if a > b:
            raise ValueError
    except ValueError:
        pass
    else:
        try:
            c = round(100 * a / b)
        except ZeroDivisionError:
            pass
        else:
            if c <= 1:
                print("E")
            elif c >= 99:
                print("F")
            else:
                print(f"{c}%")
            break
