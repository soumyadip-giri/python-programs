import numpy as np

# Define a matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
b = np.array([5, 6])

# Operations
print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition and Subtraction
print("A + B:\n", A + B)
print("A - B:\n", A - B)

# Dot Product
print("A dot B:\n", np.dot(A, B))

# Determinant
print("Determinant of A:", np.linalg.det(A))

# Inverse
print("Inverse of A:\n", np.linalg.inv(A))

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Solve Ax = b
x = np.linalg.solve(A, b)
print("Solution to Ax = b:", x)

# Singular Value Decomposition
U, S, V = np.linalg.svd(A)
print("SVD - U:\n", U)
print("SVD - Singular Values:", S)
print("SVD - V:\n", V)
