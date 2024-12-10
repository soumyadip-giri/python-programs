import matplotlib.pyplot as plt

# Sample data points for x and y
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create the scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add titles and labels
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()

