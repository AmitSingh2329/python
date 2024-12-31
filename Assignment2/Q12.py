from statistics import mean, median, mode

numbers = [1, 2, 3, 2, 3, 4, 4, 4, 5, 4, 5, 6]

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
