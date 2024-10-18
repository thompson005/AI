graph = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}

heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}


def hill_climbing(graph, start, goal, heuristic):
    path = [start]
    current = start
    cost = 0

    while current != goal:
        neighbors = graph[current]
        next_node = min(neighbors, key=lambda x: heuristic[x])
        path.append(next_node)
        cost += neighbors[next_node]
        current = next_node
        if current == goal:
            break

    print(f"Hill Climbing Best Path: {path} with cost {cost}")
    return path

hill_climbing(graph, 'S', 'G', heuristic)
