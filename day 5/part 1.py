names = open("input", "r").readlines()
length = len(names[0])

nice = 0
vowels = ["a", "e", "i", "o", "u"]
forbidden = ["ab", "cd", "pq", "xy"]


def treeVowels(name):
    count = 0
    for vowel in vowels:
        count += name.count(vowel)
        if count >= 3:
            return True
    return False


def containsDouble(name):
    for i in range(len(name) - 2):
        if len(set(name[i: i + 2])) == 1:
            return True
    return False


def noForbidden(name):
    for i in range(len(name) - 2):
        if forbidden.count(name[i: i + 2]) > 0:
            return False
    return True


for name in names:
    if treeVowels(name) and containsDouble(name) and noForbidden(name):
        nice += 1

print(nice)
