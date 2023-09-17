dic = {}
while True:
    try:
        s = input().upper()
    except EOFError:
        break
    else:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
for key, value in sorted(dic.items()):
    print(f"{value} {key}")
