import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distributions
mean = 0
std_dev1 = 0.5  # First standard deviation
std_dev2 = 2    # Second standard deviation

# Generate x values
x = np.linspace(-10, 10, 1000)

# Compute PDFs
pdf1 = norm.pdf(x, mean, std_dev1)
pdf2 = norm.pdf(x, mean, std_dev2)

# Plot both PDFs
plt.figure(figsize=(10, 6))
plt.plot(x, pdf1, label="σ = 0.5", color='blue')
plt.plot(x, pdf2, label="σ = 2", color='red')
plt.title("Probability Density Functions of Normal Distributions")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid()
plt.show()