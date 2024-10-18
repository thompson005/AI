
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



def beam_search(graph, start, goal, heuristic, beam_width=2):
    queue = [(start, [start], 0)]
    best_path = None
    min_cost = float('inf')

    while queue:
        next_level = []
        for node, path, current_cost in queue:
            if node == goal:
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_path = path
                continue

            neighbors = sorted(graph[node].items(), key=lambda x: heuristic[x[0]])
            next_level.extend([(neighbor, path + [neighbor], current_cost + cost) for neighbor, cost in neighbors])

        queue = sorted(next_level, key=lambda x: heuristic[x[0]])[:beam_width]

    print(f"Beam Search Best Path: {best_path} with cost {min_cost}")
    return best_path

beam_search(graph, 'S', 'G', heuristic)
