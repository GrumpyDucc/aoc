file = open('input', 'r').read()

realSanta = True
posSanta = (0, 0)
posRobo = (0,0)

visitedCoords = [(0,0)]
housesVisitedAtLeastOnce = 1

for move in file:
    if realSanta: pos = posSanta
    else: pos = posRobo

    match move:
        case '^': pos = (pos[0], pos[1]+1)
        case 'v': pos = (pos[0], pos[1]-1)
        case '<': pos = (pos[0]-1, pos[1])
        case '>': pos = (pos[0]+1, pos[1])
    
    if realSanta: posSanta = pos
    else: posRobo = pos

    if pos not in visitedCoords:
        visitedCoords.append(pos)
        housesVisitedAtLeastOnce += 1

    realSanta = not realSanta

print(housesVisitedAtLeastOnce)