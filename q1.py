import matplotlib.pyplot as plt

# Creating data
x = range(10)  # x values from 0 to 9
y1 = [val**2 for val in x]  # y1 = x^2
y2 = [val**3 for val in x]  # y2 = x^3

# Creating subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns of subplots

# Plotting on the first subplot
ax1.plot(x, y1, label="y = x^2")  # Quadratic plot
ax1.set_title("Quadratic")  # Title for the first subplot
ax1.legend()  # Display legend for the first subplot

# Plotting on the second subplot
ax2.plot(x, y2, label="y = x^3", color="red")  # Cubic plot
ax2.set_title("Cubic")  # Title for the second subplot
ax2.legend()  # Display legend for the second subplot

# Display the plots
plt.show()
