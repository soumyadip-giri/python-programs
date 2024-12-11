import matplotlib.pyplot as plt

# Data for the departments
labels = ['Marketing', 'Development', 'Operations', 'Customer Support']
sizes = [25, 30, 15, 30]  # Percentage allocation
colors = ['blue','red','green','yellow']  # Colors for each section

# Plotting the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title("Resource Allocation Across Departments")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
