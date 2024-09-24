#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:47:30 2024

@author: hakan
"""

import os
import numpy as np
import matplotlib.pyplot as plt 
def find_deltaT_folders(base_dir='.'):
    return [f for f in os.listdir(base_dir) if f.startswith('deltaT_')]

def read_max_error_velocity(file_path, time_step='0.3'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # İlk iki satır başlık olduğu için onları atlayın
            for line in lines[2:]:
                # Satırı boşluklara göre ayırın
                columns = line.split()

                # Eğer ilk sütun "time_step" ise, ikinci sütunu döndür
                if columns[0] == time_step:
                    return columns[1]
    return None

def read_results_to_variable(base_folder, sub_folder='postProcessing/error_velocity_norm/0/', time_step='0.3'):
    # deltaT_ ile başlayan tüm klasörleri bulun
    deltaT_folders = find_deltaT_folders(base_folder)

    # Sonuçları saklamak için bir liste oluştur
    results = []

    # Her deltaT klasörü için döngüye gir
    for deltaT_folder in deltaT_folders:
        file_path = os.path.join(base_folder, deltaT_folder, sub_folder, 'volFieldValue_0.dat')

        # Dosyadaki hatayı oku
        max_error = read_max_error_velocity(file_path, time_step)
        if max_error:
            # Sonuçları listeye ekle
            results.append((deltaT_folder, time_step, max_error))
        else:
            print(f"File not found or data not found for folder: {deltaT_folder}")

    return results

# Klasör yolu
time =np.array([0.03,0.015,0.0075,0.00375])
backward_path = 'results_temporal/backward'
# Sonuçları bir değişkene kaydet
backward_results = read_results_to_variable(backward_path)
rk4Foam_0_0000001= []

# Sonuçları işleme ve numpy dizisine koyma
for i, result in enumerate(backward_results):
    # Her bir max error velocity magnitude değerini listeye ekle
    rk4Foam_0_0000001.append(float(result[2]))

# Tüm değerleri bir numpy dizisi olarak kaydet
error_values_array = np.array(rk4Foam_0_0000001).T


plt.loglog(time,error_values_array)
