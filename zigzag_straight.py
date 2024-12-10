import matplotlib.pyplot as plt

# Define data points for Zigzag or Straight Line
x = [0, 1, 2, 3, 4, 5]  # X-axis values

# Option 1: Zigzag Line
y_zigzag = [0, 2, 1, 3, 2, 4]  # Y-axis values (fluctuates)

# Option 2: Straight Line
y_straight = [2, 2, 2, 2, 2, 2]  # Y-axis values (steady)

# Plot the Zigzag Line
plt.figure(figsize=(10, 6))
plt.plot(x, y_zigzag, label="Zigzag Line", color="blue", marker="o", linestyle="--")

# Plot the Straight Line
plt.plot(x, y_straight, label="Straight Line", color="green", marker="x", linestyle="-")

# Add titles, labels, and legend
plt.title("Line Chart Example", fontsize=16)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True)

# Display the chart
plt.show()
