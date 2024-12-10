import random

# 1. Generate a random float between 0 and 1
random_float = random.random()
print("Random float (0 to 1):", random_float)

# 2. Generate a random float between a specific range
random_uniform = random.uniform(5, 10)
print("Random float (5 to 10):", random_uniform)

# 3. Generate a random integer between two values
random_int = random.randint(1, 100)
print("Random integer (1 to 100):", random_int)

# 4. Choose a random element from a list
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_fruit = random.choice(fruits)
print("Random choice from list:", random_fruit)

# 5. Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)

# 6. Get a random sample of unique elements from a list
sampled_numbers = random.sample(numbers, 3)
print("Random sample of 3 elements:", sampled_numbers)

# 7. Generate a random number using Gaussian distribution
gaussian_number = random.gauss(0, 1)
print("Random number from Gaussian distribution (mean=0, std=1):", gaussian_number)

# 8. Generate multiple random choices with replacement
multiple_choices = random.choices(fruits, k=3)
print("Multiple random choices with replacement:", multiple_choices)

# 9. Generate a random number from a range with a step
random_range = random.randrange(0, 50, 5)
print("Random number from range (0 to 50 with step 5):", random_range)

# 10. Set a random seed for reproducibility
random.seed(42)
print("Random integer with seed 42:", random.randint(1, 100))

