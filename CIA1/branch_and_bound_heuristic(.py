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

def branch_and_bound_heuristic(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, start, [start])]
    best_path = None
    min_cost = float('inf')

    while queue:
        est_cost, current_cost, node, path = queue.pop(0)

        if node == goal:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        for neighbor, cost in graph[node].items():
            if neighbor not in path:
                total_cost = current_cost + cost
                heuristic_cost = total_cost + heuristic[neighbor]
                queue.append((heuristic_cost, total_cost, neighbor, path + [neighbor]))
                queue = sorted(queue, key=lambda x: x[0])

    print(f"Branch and Bound + Heuristic Best Path: {best_path} with cost {min_cost}")
    return best_path

branch_and_bound_heuristic(graph, 'S', 'G', heuristic)

