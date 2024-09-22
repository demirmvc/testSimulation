#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lit: E.Erturk, T.C.Corke and C.Gökçöl. Numerical solutions of 2-D steady incompressible driven cavity flow at high Reynolds numbers. Int. J. Numer. Meth. Fluids 2005; 48:747-77
"""

import pandas as pd
import matplotlib.pyplot as plt

""" cavity pimple cubic interpolation """
cavity_pimple_cubic = 'cavity_pimple/simvalues.csv'  # CSV dosyanızın yolunu buraya yazın
read_cubic_values = pd.read_csv(cavity_pimple_cubic)
#horizantal velocity vertical points
selected_columns_cubic = ['Points_1', 'U_0']
selected_data_cubic = read_cubic_values[selected_columns_cubic]
selected_data_cubic = selected_data_cubic.sort_values(by='Points_1')

""" cavity icoFoam linear interpolation """
cavity_ico_linear = 'cavity_ico_linear/simvalues.csv'  # CSV dosyanızın yolunu buraya yazın
read_linear_values = pd.read_csv(cavity_ico_linear)
#horizantal velocity vertical points
selected_columns_linear = ['Points_1', 'U_0']
selected_data_linear = read_cubic_values[selected_columns_linear]
selected_data_linear = selected_data_linear.sort_values(by='Points_1')

""" cavity runge kutta 4th order """
cavity_ico_rk = 'cavity_rk/simvalues.csv'  # CSV dosyanızın yolunu buraya yazın
read_rk_values = pd.read_csv(cavity_ico_rk)
#horizantal velocity vertical points
selected_columns_rk = ['Points_1', 'U_0']
selected_data_rk = read_rk_values[selected_columns_rk]
selected_data_rk = selected_data_rk.sort_values(by='Points_1')



# CSV dosyasını oku
file_path = 'lit/lit.csv'  # CSV dosyanızın yolunu buraya yazın
df = pd.read_csv(file_path)
# x ekseni y sütunu olsun ve y ekseni de x=0.5 sütunu olsun
x = df['yvalues']
y = df['Ux']

# Grafik boyutunu ayarla
plt.figure(figsize=(20,16))

# Çizgiler ve noktalar için farklı renkler ve stiller kullan
plt.plot(selected_data_cubic['Points_1'], selected_data_cubic['U_0'], color='r', linestyle='-', marker='o', linewidth=2, markersize=10, label="pimpleFoam - cubic")
plt.plot(selected_data_rk['Points_1'], selected_data_rk['U_0'], color='y', linestyle='--', marker='s', linewidth=2, markersize=10, label="runge kutta 4$^{th}$ order")
#plt.plot(selected_data_linear['Points_1'], selected_data_linear['U_0'], color='y', linestyle='-',marker='o',label="icoFoam-linear")
plt.plot(x, y, marker='^', linestyle='-.', color='g', linewidth=2, markersize=10, label='E.Erturk 2005')

# Eksen etiketleri, başlık ve grid ayarları
plt.xlabel('Y coordinates', fontsize=35)
plt.ylabel('$U_x$', fontsize=35, fontweight='bold')
#plt.title('Cavity 2D Lid Problem', fontsize=30)
plt.grid(True, linestyle='--', linewidth=0.7)
plt.legend(fontsize=35)
# Eksenlerin kalınlıklarını ayarla
ax = plt.gca()
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.tick_params(axis='both', which='major', labelsize=35, width=10)
ax.tick_params(axis='both', which='minor', labelsize=35, width=10)

# Grafiği PDF olarak kaydet
plt.savefig("cavity.pdf", format='pdf')

# Grafik gösterimi
plt.show()

