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


def branch_and_bound_greedy_exit(graph, start, goal, heuristic):
    queue = [(0 + heuristic[start], 0, start, [start])]

    while queue:
        _, current_cost, node, path = queue.pop(0)

        if node == goal:
            print(f"Branch and Bound Greedy + Exit Best Path: {path} with cost {current_cost}")
            return path

        for neighbor, cost in graph[node].items():
            if neighbor not in path:
                queue.append((current_cost + cost + heuristic[neighbor], current_cost + cost, neighbor, path + [neighbor]))
                queue = sorted(queue, key=lambda x: x[0])

branch_and_bound_greedy_exit(graph, 'S', 'G', heuristic)
