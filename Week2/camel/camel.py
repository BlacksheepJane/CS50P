s = input("camelCase: ")
snake = ""
for a in s:
    if a.isupper():
        snake += "_" + a.lower()
    else:
        snake += a
print(f"snake_name: {snake}")
