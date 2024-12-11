import matplotlib.pyplot as plt

# Sample data points for x and y
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]

# Create the scatter plot
plt.scatter(x, y, color='blue', marker='o')

# Add titles and labels
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Display the plot
plt.show()

