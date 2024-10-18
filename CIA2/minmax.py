def minimax_algorithm(current_depth, index, maximizing_player, leaf_values):
    if current_depth == 3:
        return leaf_values[index]

    if maximizing_player:
        max_value = float('-inf')
        for i in range(2):
            value = minimax_algorithm(current_depth + 1, index * 2 + i, False, leaf_values)
            max_value = max(max_value, value)
        return max_value
    else:
        min_value = float('inf')
        for i in range(2):
            value = minimax_algorithm(current_depth + 1, index * 2 + i, True, leaf_values)
            min_value = min(min_value, value)
        return min_value


if __name__ == "__main__":
    leaf_values = [1, 4, 7, 2, 3, 0, 6, 5]
    optimal_result = minimax_algorithm(0, 0, True, leaf_values)
    print(f"Optimal value using Minimax: {optimal_result}")
