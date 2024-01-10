# generating unique combinations of one-side package lengths that will sum up to target number 
def unique_sizes_combinations(unique_numbers, target_sum):
    combinations = [[] for _ in range(target_sum + 1)]
    combinations[0] = [[]]

    for num in unique_numbers:
        for i in range(num, target_sum + 1):
            for prev_combo in combinations[i - num]:
                new_combo = prev_combo + [num]
                combinations[i].append(new_combo)

    return combinations[target_sum]

