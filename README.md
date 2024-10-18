# Graph Search Algorithms and Minimax with Alpha-Beta Pruning

## Overview

This repository showcases various search algorithms designed to navigate a graph, focusing on finding the best path from a starting node (`S`) to a goal node (`G`). Additionally, it covers the **Minimax** algorithm and its optimized version, **Alpha-Beta Pruning**.

### Graph Structure

The graph used for the algorithms is defined as follows:

```python
graph = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}
```

### Heuristic Values

Heuristic values for each node are provided as follows:

```python
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}
```

## Search Algorithms

The following algorithms are implemented to find the best path from `S` to `G`:

1. **British Museum Search**: Explores all paths without optimization.
2. **Depth-First Search (DFS)**: Explores as deep as possible before backtracking.
3. **Breadth-First Search (BFS)**: Explores all nodes at the present depth before moving on.
4. **Hill Climbing**: Chooses the path with the lowest heuristic value.
5. **Beam Search**: Maintains a limited number of best nodes at each level.
6. **Oracle Search**: Uses perfect knowledge to find the shortest path.
7. **Branch and Bound (B&B)**: Explores paths but prunes less promising ones.
8. **Branch and Bound Greedy**: Uses heuristics for guiding the search.
9. **Branch and Bound Greedy + Exit**: Exits immediately upon reaching the goal.
10. **Branch and Bound Greedy + Heuristic**: Combines cost and heuristic aggressively.
11. **Branch and Bound with Heuristic**: Explores nodes based on both cost and heuristic.
12. **A* Algorithm**: Combines path cost and heuristics to find the optimal path.

### Expected Outputs

For all algorithms, the expected output is as follows:

```
Best Path: ['S', 'A', 'D', 'G'] with cost 6
```

## Minimax Algorithm and Alpha-Beta Pruning

### Minimax Algorithm

The **Minimax Algorithm** is used in decision-making scenarios, particularly in two-player games. It operates by evaluating nodes in a tree where one player seeks to maximize their score while the other seeks to minimize it.

### Alpha-Beta Pruning

**Alpha-Beta Pruning** optimizes the Minimax algorithm by eliminating branches that won't affect the final decision. This results in faster evaluations without compromising the accuracy of the results.

#### Key Concepts:

- **Maximizing Player**: Tries to maximize the node value.
- **Minimizing Player**: Tries to minimize the node value.
- **Alpha**: Best value the maximizing player can guarantee.
- **Beta**: Best value the minimizing player can guarantee.

### Example Tree Structure

Both algorithms use a simple game tree structure:

```
          N1
        /          N2      N3
     /  \    /     N4   N5  N6   N7
  / \   / \  / \  /  1   4 7   2 3   0 6   5
```

### Outputs

The outputs for both algorithms are:

```
Optimal value using Minimax: 5
Optimal value using Alpha-Beta Pruning: 5
```

Both algorithms yield the same optimal value, but Alpha-Beta Pruning performs this evaluation more efficiently.
