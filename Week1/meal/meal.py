def main():
    a = convert(input("What time is it?"))
    if 7 <= a <= 8:
        print("breakfast time")
    elif 12 <= a <= 13:
        print("lunch time")
    elif 18 <= a <= 19:
        print("dinner time")


def convert(time):
    flag = 0
    ts = time.split()
    if ts[-1] == "p.m.":
        flag = 1
    x, y = ts[0].split(":")
    return int(x) + int(y) / 60 + 12 * flag


if __name__ == "__main__":
    main()
