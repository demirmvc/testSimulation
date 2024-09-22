#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:36:50 2024

@author: hakan
"""

import os
import matplotlib.pyplot as plt
import numpy as np

""" RUNGE KUTTA 4 and PIMPLE ERROR LOG - LOG """
### 
###
###
###

""" read all data"""
def read_error_data(scheme, time_step, base_dir):
    result_dir = f"{base_dir}/{scheme}/deltaT_{time_step}/postProcessing/error_velocity_norm/0"
    file_path = os.path.join(result_dir, 'volFieldValue_0.dat')

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Find the last line that contains the time and error values
            for line in reversed(lines):
                line = line.strip()
                if line and not line.startswith("#"):
                    _, error_value = line.split()
                    return float(error_value)
    else:
        print(f"File not found: {file_path}")
        return None

# Base directory where results are stored
base_dir_rk4 = '/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal_rk4/results_temporal'
base_dir_pimple = '/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal_pimple/results_temporal'
base_dir_thuc ='/home/hakan/courses/hoof-testing/results_temporal'

# Schemes and time steps to be evaluated
schemes = ['Euler', 'backward', 'CrankNicolson']
time_steps = ['0.0001', '0.00005', '0.000025', '0.0000125']  # Include all relevant time steps
time=np.array([0.0001,0.00005,0.000025,0.0000125])
time_hoof = np.array([0.05,0.025,0.0125,0.00625])


"""RK4"""
# Initialize variables to store error values
backward_0_0001_rk4 = read_error_data('backward', '0.0001', base_dir_rk4)
backward_0_00005_rk4 = read_error_data('backward', '0.00005', base_dir_rk4)
backward_0_000025_rk4 = read_error_data('backward', '0.000025', base_dir_rk4)
backward_0_0000125_rk4 = read_error_data('backward', '0.0000125', base_dir_rk4)
backward_rk4 = np.array([backward_0_0001_rk4, backward_0_00005_rk4, backward_0_000025_rk4, backward_0_0000125_rk4])

""" PIMPLE"""
euler_0_0001 = read_error_data('Euler', '0.0001', base_dir_pimple)
euler_0_00005 = read_error_data('Euler', '0.00005', base_dir_pimple)
euler_0_000025 = read_error_data('Euler', '0.000025', base_dir_pimple)
euler_0_0000125 = read_error_data('Euler', '0.0000125', base_dir_pimple)
euler_pimple = np.array([euler_0_0001, euler_0_00005, euler_0_000025,euler_0_0000125])
backward_0_0001 = read_error_data('backward', '0.0001', base_dir_pimple)
backward_0_00005 = read_error_data('backward', '0.00005', base_dir_pimple)
backward_0_000025 = read_error_data('backward', '0.000025', base_dir_pimple)
backward_0_0000125 = read_error_data('backward', '0.0000125', base_dir_pimple)
backward_pimple = np.array([backward_0_0001, backward_0_00005, backward_0_000025,backward_0_0000125])


# Plot the error values for each scheme
plt.figure(figsize=(10, 6))

x_ = np.geomspace(1e-5, 1e-4, num=1000)
for i in np.geomspace(1,1e-1, num=1):
    pass
    plt.plot(
        x_,
        i * x_,
        color="gray",
        linestyle="dashed",
        alpha=0.2,
        label="_nolegend_",
    )


plt.loglog(time,backward_pimple,label="backward pimple ",color="r",ls="-.",marker="o")
plt.loglog(time,euler_pimple,label="euler pimple ",color="b",ls="dotted",marker="o")
plt.loglog(time,backward_rk4,label="rk4",color="y",ls="--",marker="o")

# Set plot labels and title
plt.xlabel('Log(Time Step)')
plt.ylabel('Log(Error Velocity Value)')


plt.legend()
plt.savefig("error_velocity.pdf")
plt.show()



