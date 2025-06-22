input = open("input", "r").read()

floor = 0

for c, i in enumerate(input):
    if i == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
