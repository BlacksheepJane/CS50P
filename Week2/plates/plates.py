def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    if length < 2 or length > 6:
        return False
    start = False
    for i in range(length):
        if s[i].isalpha():
            if start:
                return False
        elif s[i].isdigit():
            if i < 2:
                return False
            if not start and s[i] == "0":
                return False
            start = True
        else:
            return False
    return True


main()
