import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
a, b, omega = 1, 1, 10
t_end = 1
y0 = b / (a**2 + omega**2)

def analytic_solution(t, a, b, omega):
    return b / (a**2 + omega**2) * (omega * np.sin(omega*t) + a * np.cos(omega*t))

def l2_error(analytical, numerical):
    return np.sqrt(np.mean((analytical - numerical)**2))

def f(t, y):
    return -a * y + b * np.cos(omega * t)

def runge_kutta_step(t, y, h):
    k1 = h * f(t, y)
    k2 = h * f(t + 0.5*h, y + 0.5*k1)
    k3 = h * f(t + 0.5*h, y + 0.5*k2)
    k4 = h * f(t + h, y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6

def solve_ode(dt):
    t = np.arange(0, t_end + dt, dt)
    y_rk = np.zeros_like(t)
    y_rk[0] = y0
    
    for i in range(1, len(t)):
        y_rk[i] = runge_kutta_step(t[i-1], y_rk[i-1], dt)
    
    y_analytical = analytic_solution(t, a, b, omega)
    l2_error_val = l2_error(y_analytical, y_rk)
    
    return t, y_rk, y_analytical, l2_error_val

# Time steps and colors
time_steps = [1/256, 1/128, 1/64, 1/32]
colors = ['m', 'b', 'g', 'r']

# Set the base directory for OpenFOAM results
base_dir = "/home/hakan/OpenFOAM/hakan-v2406/applications/solvers/incompressible/oderkFoam"

# File paths for local data
file_paths = [
    "results/U_values_0.00390625.txt",
    "results/U_values_0.0078125.txt",
    "results/U_values_0.015625.txt",
    "results/U_values_0.03125.txt"
]

# Initialize error lists
errors_openfoam = []
errors_file = []
errors_rk = []

# Plot setup
plt.figure(figsize=(12, 8))
# Process file data
t_arrays = []
u_arrays = []
for file_path, dt in zip(file_paths, time_steps):
    t_values = []
    u_values = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            if "Time:" in line and "U:" in line:
                parts = line.split(',')
                time = float(parts[0].split(':')[1].strip())
                u_value = float(parts[1].split(':')[1].strip())
                t_values.append(time)
                u_values.append(u_value)
    
    t_array = np.array(t_values)
    u_array = np.array(u_values)
    
    t_arrays.append(t_array)
    u_arrays.append(u_array)
    
    u_analytical = analytic_solution(t_array, a, b, omega)
    error = l2_error(u_analytical, u_array)
    errors_file.append(error)
    
    plt.plot(t_array, u_array, '--', label=f'Runge Kutta 4th dt={dt}')


# Plot analytical solution
t_fine = np.linspace(0, t_end, 1000)
y_analytical_fine = analytic_solution(t_fine, a, b, omega)
plt.plot(t_fine, y_analytical_fine, 'k-', label='Analytical')

plt.xlabel('Time')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.savefig('ResultGraph.pdf')  # Doğru kullanım budur

plt.show()

# Error analysis plot
plt.figure(figsize=(10, 6))
plt.loglog(time_steps, errors_file, 'go-', label='Runge Kutta 4th order')
# plt.loglog(time_steps, errors_rk, 'ro-', label='Runge-Kutta')
plt.loglog(time_steps, np.array(time_steps)**4, 'k--', label='4th Order Reference')
plt.xlabel('Time Step (dt)')
plt.ylabel('L2 Error')
plt.legend()
plt.grid(True)
plt.savefig('L2Error.pdf')  # Doğru kullanım budur

plt.show()

# Calculate and print convergence rates
for errors, method in zip([errors_openfoam, errors_file, errors_rk], ['OpenFOAM', 'File Data', 'Runge-Kutta']):
    print(f"\nConvergence rates for {method}:")
    convergence_rates = []
    for i in range(1, len(errors)):
        rate = np.log(errors[i] / errors[i-1]) / np.log(time_steps[i] / time_steps[i-1])
        convergence_rates.append(rate)
        print(f"  Between dt={time_steps[i]:.6f} and dt={time_steps[i-1]:.6f}: {rate:.4f}")
    
    avg_rate = np.mean(convergence_rates)
    print(f"Average convergence rate: {avg_rate:.4f}")