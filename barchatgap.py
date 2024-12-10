import matplotlib.pyplot as plt

# Data for the bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 8, 3, 10, 6]

# Create the bar chart with gaps (reduce the bar width)
plt.bar(categories, values, width=0.4, color='skyblue', edgecolor='black')

# Adding titles and labels
plt.title("Bar Chart with Gaps Between Bars")
plt.xlabel("Categories")
plt.ylabel("Values")

# Display the chart
plt.show()
