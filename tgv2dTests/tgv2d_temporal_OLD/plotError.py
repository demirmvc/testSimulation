import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob






#%%          
"""
error_velocity_norm
"""


time_steps = np.array([0.03,0.015,0.0075,0.00375])
pimple_Euler_nu1 = np.array([9.772713915620e-03,4.959382151260e-03,2.522440864020e-03,1.296726051600e-03])
pimple_backward_nu1 = np.array([1.303342401610e-03,3.663315881450e-04,1.395350624790e-04,8.403627271020e-05])

pimple_Euler_nu0_0000001 = np.array([5.123274399880e-04,5.093617351630e-04,5.044754408640e-04,4.960482374310e-04])
pimple_backward_nu0_0000001 = np.array([5.108376701010e-04,5.070738477450e-04,5.004021379690e-04,4.888906795930e-04])

RK4Foam_nu0_0000001 = np.array([1.468150843690e-04,7.225719993670e-05, 3.776830436860e-05,1.901448353330e-05])
rkFoam_nu0_0000001= np.array([5.371340541550e-05,2.689501830820e-05,1.345737236600e-05,6.731179178820e-06])

x_ = np.geomspace(1e-3,1e1, num=10000)  # X ekseninin mevcut aralığına uygun olarak ayarlandı
plt.figure(figsize=(10, 6))
for idx, i in enumerate(np.geomspace(1e-3, 1e4, num=10)):  # 'i' aralığı L2 Error aralığına göre ayarlandı
    label = "1st Order" if idx == 0 else None  # İlk çizim için etiket
    plt.plot(
        x_,
        i * x_,
        color="gray",
        linestyle="dashed",
        alpha=0.3,
        label=label,
    )

    label = "2nd Order" if idx == 0 else None  # İlk çizim için etiket
    plt.plot(
        x_,
        i * x_**2,
        color="gray",
        linestyle="dotted",
        alpha=0.3,
        label=label,
    )
    


plt.loglog(time_steps, pimple_Euler_nu1, linestyle='-',marker='o', linewidth=2, label='Pimple - Euler,ν=1')
plt.loglog(time_steps, pimple_backward_nu1, linestyle='-',marker='o', linewidth=2, label='Pimple - backward ,ν=1')

plt.loglog(time_steps, pimple_Euler_nu0_0000001, linestyle='--',marker='o', linewidth=2, label='Pimple - Euler,ν=0_0000001')
plt.loglog(time_steps, pimple_backward_nu0_0000001, linestyle='--',marker='o', linewidth=1, label='Pimple - backward ,ν=0_0000001')


plt.loglog(time_steps, rkFoam_nu0_0000001, linestyle='-',marker='o', linewidth=2, label='rk4Foam ,ν=0.0000001')
plt.loglog(time_steps, RK4Foam_nu0_0000001, linestyle='-',marker='o', linewidth=2, label='RK4FOAM,ν=0.0000001')



# Eksen sınırlarını ayarla
plt.xlim(2e-3, 5e-2)  # X ekseni sınırları
plt.ylim(1e-6, 2e-2)  # Y ekseni sınırları, L2 Error verilerine göre ayarlandı
# Eksen etiketlerini ve diğer ayarları yap
plt.xlabel("Δt", fontsize=16)
plt.ylabel("Error Velocity Mag", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("TGV 128X128", fontsize=16)

plt.legend(loc='upper left')  # Legend konumunu ayarla
#plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)  # Izgara ekle
plt.tight_layout()
plt.savefig("plot1.pdf")
plt.show()

