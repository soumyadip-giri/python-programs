import matplotlib.pyplot as plt

# Data for the bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 8, 3, 10, 6]

# Create the bar chart
plt.bar(categories, values, color='skyblue')

# Adding titles and labels
plt.title("Basic Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

# Display the chart
plt.show()
