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

import heapq

def a_star(graph, start, goal, heuristic):
    queue = [(0 + heuristic[start], 0, start, [start])]
    best_path = None
    min_cost = float('inf')

    while queue:
        estimated_cost, current_cost, node, path = heapq.heappop(queue)

        if node == goal:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        for neighbor, cost in graph[node].items():
            heapq.heappush(queue, (current_cost + cost + heuristic[neighbor], current_cost + cost, neighbor, path + [neighbor]))

    print(f"A* Best Path: {best_path} with cost {min_cost}")
    return best_path

a_star(graph, 'S', 'G', heuristic)
