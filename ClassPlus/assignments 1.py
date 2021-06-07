# As the travelling time between the mentioned universes can't  be negative so we can use Dijskta's algorithm
def modifiedDijskta(adjMat, universes, patrols):
    # Relaxing all edges
    requiredTime = [float('inf')] * universes
    requiredTime[0] = 0

    for x in range(universes):
        for y in range(universes):
            if adjMat[x][y] != -1:
                # Checking for patrolling condition
                wait = 1 if requiredTime[x] + adjMat[x][y] in patrols[y] else 0

                # Relaxing an edge
                if requiredTime[y] > requiredTime[x] + adjMat[x][y] + wait:
                    requiredTime[y] = requiredTime[x] + adjMat[x][y] + wait

    # Checking is source reachable
    return requiredTime[universes-1] if requiredTime[universes-1] != float('inf') else -1


if __name__ == '__main__':
    universes, portals = [int(x) for x in input().split()]
    adjMat = [[-1 for i in range(universes)] for j in range(universes)]
    for k in range(portals):
        x, y, w = [int(x) for x in input().split()]
        adjMat[x-1][y-1] = w

    # making patrol as list of set as searching time in set in O(1)
    patrols = [set([int(i) for i in input().split()]) for j in range(universes)]

    print(modifiedDijskta(adjMat, universes, patrols))


