#Questão 1
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Mb = 1 #kg
v0 = 27.78 #m/s
g = 10 #m/s^2
Acm = 5e-3
coeficiente_a1 = 0.004 #m^-1
coeficiente_a2 = 0.006 #m^-1
vd = 35 #m/s
Parametro_Transicao = 5 #m/s
dt = 0.01 #s

angulos_theta = np.arange(68, 76, 1) 
angulos_phi = np.arange(-25, 15, 1) 
Pontos = 10000
Omega = 164 #rad/s

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

try:
    from IPython import get_ipython
    get_ipython().run_line_magic('matplotlib', 'qt')
except:
    pass

trajetorias_para_animar = []
print("Calculando trajetórias... Aguarde.")

for theta in angulos_theta:
    for phi in angulos_phi:
        x = [0]
        y = [0]
        z = [0]
        v_x = [v0*np.cos(np.deg2rad(phi))*np.sin(np.deg2rad(theta))]
        v_y = [v0*np.sin(np.deg2rad(theta))*np.sin(np.deg2rad(phi))]
        v_z = [v0*np.cos(np.deg2rad(theta))]
        acertou = False
        
        for i in range(0, Pontos):
            vi = np.sqrt((v_x[i])**2 + (v_y[i])**2 + (v_z[i])**2)
            DPNL = coeficiente_a1 + (coeficiente_a2 / (1 + np.exp((vi-vd) / Parametro_Transicao)))
            
            proximo_x = x[i] + v_x[i] * dt
            proximo_y = y[i] + v_y[i] * dt
            proximo_z = z[i] + v_z[i] * dt
            
            proximo_v_x = v_x[i] - (DPNL*vi*v_x[i] + Acm*Omega*v_y[i])*dt
            proximo_v_y = v_y[i] - (DPNL*vi*v_y[i] - Acm*Omega*v_x[i])*dt
            proximo_v_z = v_z[i] - (g + DPNL*vi*v_z[i])*dt
            
            x.append(proximo_x)
            y.append(proximo_y)
            z.append(proximo_z)
            v_x.append(proximo_v_x)
            v_y.append(proximo_v_y)
            v_z.append(proximo_v_z)
            
            if abs(x[i] - 30) < 0.2:
                if 4 < y[i] < 10 and 0 < z[i] < 2.5:
                    print(f"Alvo atingido! Angulos: theta={theta}, phi={phi}")
                    print(f"Posição exata: x={x[i]:.2f}, y={y[i]:.2f}, z={z[i]:.2f}")
                    acertou = True
                    break
            
            if z[-1] < -0.5 or x[-1] > 40:
                break
                
        if acertou:
            trajetorias_para_animar.append((x, y, z))

# O script de animação da barreira, do campo, e da câmera omitidos para manter as funções base matemáticas.
# Caso precise das linhas de formatação estética da matplotlib completas deste script, elas seguem a lógica de FuncAnimation.