print("Tuple Activities")
# Activity 1: Access Elements
colors = ("red", "green", "blue")

# Print the first and last item
print(colors[0])
print(colors[2])

# Activity 2: Slicing
numbers = (10, 20, 30, 40, 50)

# Print (20, 30, 40)
print(numbers[1:4])

# Activity 3: Tuple Methods
nums = (1, 2, 2, 3, 2)
# Count how many times 2 appears
x = nums.count(2)
x = nums.index(3)
point = (5, 10)
x, y = point
print("x = ", x, " y =", y)


# Activity 5 (Challenge): Combine Tuples
print("\nCombine Tuples")
t1 = (1, 2)
t2 = (3, 4)

t3 = t1 + t2 * 2
print(t3)


