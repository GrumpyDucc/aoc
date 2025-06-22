names = open("input", "r").readlines()

nice = 0


def containsRepeating(name):
    for i in range(len(name) - 2):
        triple = name[i: i + 3]
        if triple[0] == triple[2]:
            return True
    return False


def containsPairs(name):
    allPairs = []
    for i in range(len(name) - 1):
        pair = name[i: i + 2]

        for entry in allPairs:
            if entry["pair"] == pair:
                if entry["found"] != i - 1:
                    return True
        allPairs.append({"found": i, "pair": pair})
    return False


for name in names:
    name = name.strip()
    repeating = containsRepeating(name)
    pairs = containsPairs(name)
    if repeating and pairs:
        nice += 1
    print(name, pairs, repeating)

print(nice)
