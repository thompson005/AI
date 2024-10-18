import itertools

graph = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}

def british_museum_search(graph, start, goal):
    all_paths = []

    def dfs(node, visited, path):
        if node == goal:
            all_paths.append(path + [node])
            return
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                dfs(neighbor, visited + [neighbor], path + [node])
    
    dfs(start, [], [])

    best_path = None
    min_cost = float('inf')

    for path in all_paths:
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        if cost < min_cost:
            min_cost = cost
            best_path = path

    print(f"British Museum Search Best Path: {best_path} with cost {min_cost}")
    return best_path

british_museum_search(graph, 'S', 'G')
