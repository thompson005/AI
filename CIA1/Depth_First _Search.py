graph = {
    'S': ['A', 'C'],
    'A': ['S', 'B', 'D'],
    'B': ['A', 'C'],
    'C': ['S', 'B', 'E'],
    'D': ['A', 'G'],
    'E': ['C'],
    'G': ['D']
}


def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
        
    path.append(start)
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result
            
    path.pop()
    return None

print("DFS Path:", dfs(graph, 'S', 'G'))
