import numpy as np
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition (A + B):")
print(A + B)

print("\nMultiplication (A x B):")
print(np.dot(A, B))