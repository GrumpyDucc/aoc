file = open('input', 'r').read()

visitedCoords = [(0, 0)]
pos = (0, 0)
housesVisitedAtLeastOnce = 1

for move in file:
    match move:
        case '^': pos = (pos[0], pos[1]+1)
        case 'v': pos = (pos[0], pos[1]-1)
        case '<': pos = (pos[0]-1, pos[1])
        case '>': pos = (pos[0]+1, pos[1])
    if pos not in visitedCoords:
        visitedCoords.append(pos)
        housesVisitedAtLeastOnce += 1

print(housesVisitedAtLeastOnce)