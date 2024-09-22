import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io




#%% Lit values

erturkUx = np.array([0,-0.1517,-0.2547,-0.3372,-0.3979,-0.4250,-0.4200,-0.3965,-0.3688,-0.3439,-0.3228,-0.0403,0.4141,0.4256,0.4353,0.4424,0.4470,0.4506,0.4607,0.4971,0.5924,0.7704,1])




liddriven32 = "/home/hakan/courses/testSimulation/cavityTest/cavity/cavity30/cavitycubic30.csv"

liddriven64 = "/home/hakan/courses/testSimulation/cavityTest/cavity/cavity60/cavitycubic60.csv"
liddriven128 = "/home/hakan/courses/testSimulation/cavityTest/cavity/cavity120/cavitycubic120.csv"

liddriven32 = pd.read_csv(liddriven32, sep=',') 
liddriven64= pd.read_csv(liddriven64, sep=',') 
liddriven128= pd.read_csv(liddriven128, sep=',') 

liddriven32Ux = liddriven32["U_0"]
liddriven64Ux = liddriven64["U_0"]
liddriven128Ux = liddriven128["U_0"]

L2_ERROR_liddriven32 = np.sqrt(np.sum((erturkUx - liddriven32Ux) ** 2))
L2_ERROR_liddriven64 = np.sqrt(np.sum((erturkUx - liddriven64Ux) ** 2))
L2_ERROR_liddriven128 = np.sqrt(np.sum((erturkUx - liddriven128Ux) ** 2))

L2_ERROR_liddriven = np.array([L2_ERROR_liddriven32,L2_ERROR_liddriven64,L2_ERROR_liddriven128])

liddriven_xvalues = np.array([0.033333333,0.0166666666,0.008333333])
#%% Get simulation values

# cavity30_rk = "/home/hakan/courses/testSimulation/cavityTest/cavity30_rk/cavity30_rk.csv"
# cavity60_rk = "/home/hakan/courses/testSimulation/cavityTest/cavity60_rk/cavity60_rk.csv"
# cavity120_rk = "/home/hakan/courses/testSimulation/cavityTest/cavity120_rk/cavity120_rk.csv"

#%%
#pimple_linear30 = "/home/hakan/courses/testSimulation/cavityTest/cavity30/pimple_linear30.csv"
# pimple_linear60 = "/home/hakan/courses/testSimulation/cavityTest/cavity60/pimple_linear60.csv"
#pimple_linear120 = "/home/hakan/courses/testSimulation/cavityTest/cavity120/pimple_linear120.csv"
# cavity30new = "/home/hakan/courses/testSimulation/cavityTest/cavity30/cavity30new.csv"
# cavity60new = "/home/hakan/courses/testSimulation/cavityTest/cavity60/cavity60new.csv"


#%%                          PIMPLE

#pimple_linear30 = pd.read_csv(pimple_linear30, sep=',') 
# pimple_linear60=   pd.read_csv(pimple_linear60, sep=',') 
#pimple_linear120=   pd.read_csv(pimple_linear120, sep=',') 
# cavity30new = pd.read_csv(cavity30new, sep=',') 
# cavity60new= pd.read_csv(cavity60new, sep=',') 
#%% pımple
# pimple_linear60Ux = pimple_linear60["U_0"]
# pimple_linear30Ux = pimple_linear30["U_0"]
#pimple_linear120Ux = pimple_linear120["U_0"]
# cavity30newUx = cavity30new["U_0"]
# cavity60newUx = cavity60new["U_0"]

#%%                 RUNGE KUTTA 4TH ORDER
# cavity30_rk = pd.read_csv(cavity30_rk, sep=',') 
# cavity60_rk = pd.read_csv(cavity60_rk, sep=',') 
# cavity120_rk = pd.read_csv(cavity120_rk, sep=',') 

# cavity30_rkUx = cavity30_rk["U_0"]
# cavity60_rkUx = cavity60_rk["U_0"]
# cavity120_rkUx = cavity120_rk["U_0"]

#%% Calculate errors: RUNGE KUTTA 4TH ORDER
# l2_error_rk_30 = np.sqrt(np.sum((erturkUx - cavity30_rkUx) ** 2))
# l2_error_rk_60 = np.sqrt(np.sum((erturkUx - cavity60_rkUx) ** 2))
# l2_error_rk_120 = np.sqrt(np.sum((erturkUx - cavity120_rkUx) ** 2))

# l2_error_rk = np.array([l2_error_rk_30,l2_error_rk_60,l2_error_rk_120])

#%%  Calculate errors:        PIMPLE
# L2 Error hesapla
# l2_error30_new = np.sqrt(np.sum((erturkUx - cavity30newUx) ** 2))
# l2_error60_new = np.sqrt(np.sum((erturkUx - cavity60newUx) ** 2))

# l2_error_linear_30 = np.sqrt(np.sum((erturkUx - pimple_linear30Ux) ** 2))
# l2_error_linear_60 = np.sqrt(np.sum((erturkUx - pimple_linear60Ux) ** 2))
#l2_error_linear_120 = np.sqrt(np.sum((erturkUx - pimple_linear120Ux) ** 2))

# l2_error_linear = np.array([l2_error_linear_60])
l2xvalues = np.array([1/30,1/60])
l2xvalues1 = np.array([1/30,1/60,1/120])


#%% PLOT
plt.figure(figsize=(10, 6))

# Mevcut grafik verilerini ayarlayın (x aralığına göre)
x_ = np.geomspace(5e-3,1, num=10000)  # X ekseninin mevcut aralığına uygun olarak ayarlandı

# Hata çizgileri için uygun 'i' aralığını ayarlayın
for i in np.geomspace(1e-1, 1e4, num=10):  # 'i' aralığı L2 Error aralığına göre ayarlandı
    plt.plot(
        x_,
        i * x_,
        color="gray",
        linestyle="dashed",
        alpha=0.3,
        label="1st order",
    )
    plt.plot(
        x_,
        i * x_**2,
        color="gray",
        linestyle="dotted",
        alpha=0.3,
        label="2nd order",
    )

# Örneğin L2 hatasını loglog formatında çiz
# plt.loglog(l2xvalues, l2_error_linear, linestyle='-', linewidth=2, label='pimple - linear')
# plt.loglog(l2xvalues1, l2_error_rk, linestyle='-', linewidth=2, label='runge kutta 4th ')


plt.loglog(liddriven_xvalues, L2_ERROR_liddriven, linestyle='-', linewidth=2, label='pimple - linear')

# Eksen sınırlarını ayarla
plt.xlim(5e-4, 1)  # X ekseni sınırları
plt.ylim(1e-3, 1e2)  # Y ekseni sınırları, L2 Error verilerine göre ayarlandı

# Eksen etiketlerini ve diğer ayarları yap
plt.xlabel("x", fontsize=16)
plt.ylabel("L2 Error", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper left')  # Legend konumunu ayarla
#plt.grid(True, which="both", ls="--", linewidth=0.5, alpha=0.7)  # Izgara ekle
plt.tight_layout()
plt.savefig("L2error.pdf")
plt.show()
