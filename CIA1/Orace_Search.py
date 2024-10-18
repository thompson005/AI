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

def oracle_search(graph, start, goal):
    path = ['S', 'A', 'D', 'G']  # Known best path from S to G
    cost = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
    print(f"Oracle Search Best Path: {path} with cost {cost}")
    return path

oracle_search(graph, 'S', 'G')
