import matplotlib.pyplot as plt

# Data
data = [7, 8, 9, 15, 22, 25, 26, 28, 30, 42, 45, 100]

# Create boxplot
plt.boxplot(data, vert=False)
plt.title("Boxplot Example")
plt.xlabel("Values")
plt.show()
