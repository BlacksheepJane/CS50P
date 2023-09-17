month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}
while True:
    try:
        date = input("Date: ").strip()
        if date[0].isdigit():
            date = date.split("/")
            if len(date) != 3 or int(date[0]) > 12 or int(date[1]) > 31:
                raise ValueError
        elif date[0].isalpha():
            date = date.split()
            if (
                len(date) != 3
                or date[0] not in month
                or date[1][-1] != ","
                or len(date[2]) != 4
                or int(date[1][:-1]) > 31
            ):
                raise ValueError
            date[1] = date[1][:-1]
            date[0] = str(month[date[0]])
        else:
            raise ValueError
    except ValueError:
        continue

    if int(date[0]) < 10:
        date[0] = "0" + date[0]
    if int(date[1]) < 10:
        date[1] = "0" + date[1]
    print(date[2] + "-" + date[0] + "-" + date[1])
    break
