input = open("input", "r").readlines()

total = 0

for dimension in input:
    lengths = list(map(int, dimension.split("x")))

    sides = [lengths[0] * lengths[1], lengths[1]
             * lengths[2], lengths[0] * lengths[2]]

    smallest = sides[0]
    total += 2 * sides[0]
    for side in sides[1:]:
        if side < smallest:
            smallest = side
        total += 2 * side
    total += smallest

print(total)

