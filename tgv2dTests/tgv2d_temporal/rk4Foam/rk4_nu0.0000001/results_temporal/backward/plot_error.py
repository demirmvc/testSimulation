#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:47:30 2024

@author: hakan
"""

import os

def find_deltaT_folders(base_dir='.'):
    """
    Belirtilen dizindeki deltaT_ ile başlayan tüm klasörleri bulur.

    Args:
        base_dir (str): Aranacak temel dizin.

    Returns:
        list: deltaT_ ile başlayan klasörlerin listesi.
    """
    return [f for f in os.listdir(base_dir) if f.startswith('deltaT_')]

def read_max_error_velocity(file_path, time_step='0.3'):
    """
    Belirtilen dosyada zaman adımına karşılık gelen max(error_velocity_mag) değerini okur.

    Args:
        file_path (str): Dosya yolu.
        time_step (str): İlgili zaman adımı.

    Returns:
        str: Zaman adımı ve max(error_velocity_mag) değeri.
    """
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

def read_and_write_results(base_folder, output_file, sub_folder='postProcessing/error_velocity_norm/0/', time_step='0.3'):
    """
    Belirtilen klasördeki tüm deltaT_ klasörlerini okur ve sonuçları bir dosyaya yazar.

    Args:
        base_folder (str): Temel klasör yolu.
        output_file (str): Çıktı dosyası adı.
        sub_folder (str): İç klasör yolu.
        time_step (str): İlgili zaman adımı.

    Returns:
        str: Çıktı dosyasının adı.
    """
    # deltaT_ ile başlayan tüm klasörleri bulun
    deltaT_folders = find_deltaT_folders(base_folder)

    # Çıktıları dosyaya yazmak için dosyayı aç
    with open(output_file, 'w') as output:
        # Başlıkları yaz
        output.write('Folder\tTime\tMax Error Velocity Magnitude\n')

        # Her deltaT klasörü için döngüye gir
        for deltaT_folder in deltaT_folders:
            file_path = os.path.join(base_folder, deltaT_folder, sub_folder, 'volFieldValue_0.dat')

            # Dosyadaki hatayı oku
            max_error = read_max_error_velocity(file_path, time_step)
            if max_error:
                output.write(f"{deltaT_folder}\t{time_step}\t{max_error}\n")
            else:
                print(f"File not found or data not found for folder: {deltaT_folder}")

    print(f"Results have been written to {output_file}")
    return output_file

# Klasör yolları
Euler_path = 'results_temporal/Euler'
backward_path = 'results_temporal/backward'

# Sonuçları dosyaya yaz
backward_values = read_and_write_results(backward_path, 'backward_results.txt')
euler_values = read_and_write_results(Euler_path, 'euler_results.txt')
