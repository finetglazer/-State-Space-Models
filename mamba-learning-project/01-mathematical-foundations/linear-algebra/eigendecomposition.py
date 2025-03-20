# 01-mathematical-foundations/linear-algebra/eigendecomposition.py
import numpy as np
import matplotlib.pyplot as plt

def demonstrate_eigendecomposition():
    """
    Demonstrate eigendecomposition of a matrix and its applications
    in the context of state space models.
    """
    # Create a simple 2x2 matrix
    A = np.array([[0.9, 0.1],
                  [0.1, 0.9]])

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("Matrix A:")
    print(A)
    print("\nEigenvalues:")
    print(eigenvalues)
    print("\nEigenvectors:")
    print(eigenvectors)

    # Verify decomposition: A = P * D * P^-1
    P = eigenvectors
    D = np.diag(eigenvalues)
    P_inv = np.linalg.inv(P)

    reconstructed_A = P @ D @ P_inv

    print("\nReconstructed A:")
    print(reconstructed_A)
    print("\nIs reconstruction close to original?")
    print(np.allclose(A, reconstructed_A))

    # Show why eigendecomposition is useful for state space models
    # For a linear system x(t+1) = A * x(t), the solution involves powers of A
    # A^n = P * D^n * P^-1, which is much easier to compute

    # Visualize how the system evolves
    x0 = np.array([1, 0])  # Initial state
    steps = 10

    states = [x0]
    x = x0

    for _ in range(steps):
        x = A @ x
        states.append(x)

    states = np.array(states)

    plt.figure(figsize=(10, 6))
    plt.plot(range(steps+1), states[:, 0], 'b-o', label='State 1')
    plt.plot(range(steps+1), states[:, 1], 'r-o', label='State 2')
    plt.title('State Evolution for Linear System')
    plt.xlabel('Time Step')
    plt.ylabel('State Value')
    plt.grid(True)
    plt.legend()
    plt.savefig('01-mathematical-foundations/linear-algebra/visualizations/eigendecomposition_state_evolution.png')
    plt.show()

if __name__ == "__main__":
    demonstrate_eigendecomposition()