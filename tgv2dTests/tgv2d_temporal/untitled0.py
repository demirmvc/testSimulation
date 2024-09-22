import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the L2 error function
def compute_L2_error(exact_vals, numerical_vals, dt):
    L2_error = np.sqrt(np.sum((exact_vals - numerical_vals)**2) )
    return L2_error

# Parameters
a = 1
b = 1
omega = 10

# Time array
t = np.linspace(0, 1, 1000)

# Calculate y
y = (b / (a**2 + omega**2)) * (omega * np.sin(omega * t) + a * np.cos(omega * t))


# Plot the exact solution
plt.figure(figsize=(8, 5))
plt.plot(t, y, label='Exact Solution y(t)', color='orange')
plt.title('Exact Solution of the ODE from 0 to 0.1')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()

# Define the parameters for Runge-Kutta method
a = 1.0
b = 1.0
omega = 10.0
y0 = (a * b) / (a**2 + omega**2)  # Initial condition

# Define the ODE as a function
def dydt(t, y):
    return -a * y + b * np.cos(omega * t)

# Runge-Kutta 4th order method implementation
def runge_kutta_4(f, y0, t0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt)
    print(len(t_values))
    y_values = np.zeros_like(t_values)
    y_values[0] = y0

        
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        # print(f" y :",y)
        k1 = f(t, y)
        k2 = f(t + 0.5*dt, y + 0.5*k1*dt)
        k3 = f(t + 0.5*dt, y + 0.5*k2*dt)
        k4 = f(t + dt, y + k3*dt)
        
        y_values[i] = y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return t_values, y_values

# Solve the ODE using Runge-Kutta
t0 = 0.0
t_end = 1
dt = 0.01  # Time step
t_values, y_values_rk4 = runge_kutta_4(dydt, y0, t0, t_end, dt)

# Plot the Runge-Kutta solution
plt.figure(figsize=(8, 5))
plt.plot(t_values, y_values_rk4, label='Runge-Kutta Solution y(t)', color='blue')
plt.title('Solution of the ODE using Runge-Kutta method')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()

# Compute L2 error using the function
L2_error = compute_L2_error(y, y_values_rk4, dt)

# Plot the L2 error
plt.figure(figsize=(8, 5))
plt.loglog(t_values, np.abs(y - y_values_rk4), label=f'L2 Error: {L2_error:.5e}', color='red')
plt.title('L2 Error between Exact Solution and Runge-Kutta Solution')
plt.xlabel('Time (t)')
plt.ylabel('Error')
plt.grid(True)
plt.legend()
plt.show()

print(f"L2 Error between Exact Solution and Runge-Kutta Solution: {L2_error:.5e}")
