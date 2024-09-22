import matplotlib.pyplot as plt
import numpy as np

# File paths
file_paths = [
    "results/U_values_0.00390625.txt",
    "results/U_values_0.0078125.txt",
    "results/U_values_0.015625.txt",
    "results/U_values_0.03125.txt"
]

# Dictionaries to store U and t values for each file
u_values_dict = {}
t_values_dict = {}

# Function to sample data
def sample_data(t_values, u_values, n_samples=50):
    if len(t_values) > n_samples:
        indices = np.linspace(0, len(t_values) - 1, n_samples, dtype=int)
        return np.array(t_values)[indices], np.array(u_values)[indices]
    return np.array(t_values), np.array(u_values)

# Read and sample data from files
for file_path in file_paths:
    u_values = []
    t_values = []
    with open(file_path, 'r') as file:
        for line in file:
            if "U:" in line:
                u_values.append(float(line.split()[3]))
            if "Time:" in line:
                t_values.append(float(line.split()[1].replace(',', '')))
    
    # Sample the data
    t_sampled, u_sampled = sample_data(t_values, u_values)
    u_values_dict[file_path] = u_sampled
    t_values_dict[file_path] = t_sampled

# Parameters for exact solution
a = 1
b = 1
omega = 10

# Function to calculate exact solution
# def y_exact(t):
#     return (b / (a**2 + omega**2)) * (omega * np.sin(omega * t) + a * np.cos(omega * t))

def analytic_solution(t, C):
    """Analytic solution of dU/dt = exp(-t)"""
    return -np.exp(-t) + C


# Calculate L2 error norms
# l2_errors = {}
# for file_path in file_paths:
#     t_vals = t_values_dict[file_path]
#     u_vals = u_values_dict[file_path]
#     y_ext = analytic_solution(t_vals)
#     l2_error = np.sqrt(np.mean((u_vals - y_ext)**2))
#     l2_errors[file_path] = l2_error

# Plot all solutions and exact solution in one graph
plt.figure(figsize=(12, 8))
colors = ['red', 'blue', 'green', 'purple']
for file_path, color in zip(file_paths, colors):
    t_vals = t_values_dict[file_path]
    u_vals = u_values_dict[file_path]
    plt.plot(t_vals, u_vals, marker='o', linestyle='-', color=color, 
             label=f'Δt = {file_path.split("_")[-1].split(".txt")[0]}')
# Parameters
t_start = 0
t_end = 1
dt = 0.01
t = np.arange(t_start, t_end + dt, dt)
U0 = 1  # You can change this to match your OpenFOAM initial condition

U_analytic = analytic_solution(t, U0 + 1)  # C = U0 + 1 to match the initial condition

# Plot exact solution
t_exact = np.linspace(0, 1, 200)
plt.plot(t,U_analytic, color='black', linestyle='--', label='Exact Solution')

plt.title('Numerical Solutions and Exact Solution')
plt.xlabel('Time (s)')
plt.ylabel('U value (X component)')
plt.legend()
plt.grid(True)
plt.show()

# Plot L2 error norms
time_steps = [float(path.split('_')[-1].split('.txt')[0]) for path in file_paths]
# error_values = list(l2_errors.values())

# plt.figure(figsize=(10, 6))
# plt.plot(time_steps, error_values, marker='o', linestyle='-', color='red')
# plt.title('L2 Error Norm vs Time Step')
# plt.xlabel('Time Step')
# plt.ylabel('L2 Error Norm')
# plt.xscale('log')
# plt.yscale('log')
# plt.grid(True)
# plt.show()

# # Print L2 error norms
# for file_path, error in l2_errors.items():
#     print(f"L2 Error Norm for {file_path}: {error}")