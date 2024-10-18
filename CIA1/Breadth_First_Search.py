
from collections import deque

graph = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}



def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])  # (current_node, path, cost)
    best_path = None
    min_cost = float('inf')

    while queue:
        node, path, current_cost = queue.popleft()

        if node == goal:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        for neighbor, cost in graph[node].items():
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], current_cost + cost))

    print(f"BFS Best Path: {best_path} with cost {min_cost}")
    return best_path

bfs(graph, 'S', 'G')
