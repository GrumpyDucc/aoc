file = open("input", "r").readlines()

total = 0

for dimension in file:
    lengths = list(map(int, dimension.split("x")))

    paper = lengths[0] * lengths[1] * lengths[2]

    largest = lengths[0]
    for side in lengths:
        if side > largest:
            largest = side
    lengths.remove(largest)

    paper += (lengths[0] + lengths[1]) * 2
    total += paper

print(total)

