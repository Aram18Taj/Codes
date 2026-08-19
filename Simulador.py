import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
#--------------------------------- Paramêtros
e_m_teorico = 1.75882e11  # Razão entre a carga e a massa do elétron (C/kg)
mu_0 = 4 * np.pi * 1e-7  # Permeabilidade magnética do vácuo (H/m)
# Parametros das Bobinas de Helmholtz
N = 130  # Número de espiras  
R_Bobina = 0.15  # Raio da bobina (m)
def campo_magnetico(I):
    """
    Calcula o campo magnético no centro de uma bobina de Helmholtz.
    
    Parâmetros:
    I : float
        Corrente elétrica na bobina (A).
        
    Retorna:
    B : float
        Campo magnético no centro da bobina (T).
    """
    B = (mu_0 * N * I) / R_Bobina  # Campo magnético no centro da bobina
    return B
def gerar_feixe_real(V, I, max_pontos = 500):
    B = campo_magnetico(I)
    if B == 0 or V == 0:
        return np.zeros(max_pontos), np.zeros(max_pontos)
        
    v0 = np.sqrt(2 * V * e_m_teorico)  
    omega = e_m_teorico * B            
    raio = v0 / omega                  
    
    t = np.linspace(0, 2 * np.pi / omega, max_pontos) 
    x = raio * np.sin(omega * t)
    y = raio * (1 - np.cos(omega * t))
    return x, y
#Configuração do gráfico
fig, ax = plt.subplots(figsize=(9, 8))
plt.subplots_adjust(left=0.1, bottom=0.35) # Espaço maior para os 3 sliders
ax.set_aspect('equal', adjustable='box')
limite = 0.14
ax.set_xlim(-0.02, limite)
ax.set_ylim(-limite/2, limite)

ax.set_title('Determinação Experimental da Constante e/m')    
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Fundo da ampola e Canhão
ampola = plt.Circle((0.065, 0), 0.065, color='lightblue', fill=True, alpha=0.15, ec='cadetblue', lw=2)
ax.add_patch(ampola)
ax.plot(0, 0, 'ks', markersize=8, label='Canhão de Elétrons')

# Valores Iniciais
V_inicial = 1500
I_inicial = 1.5
R_medido_inicial = 0.05

# 1. Plot do "Feixe Real" (Verde)
x_real, y_real = gerar_feixe_real(V_inicial, I_inicial)
linha_feixe, = ax.plot(x_real, y_real, '-', color='green', linewidth=3, label='Feixe Observado')

# 2. Plot do "Cursor de Medição" (Amarelo Tracejado)
# Este é o círculo que o usuário ajusta para tentar medir o raio
theta = np.linspace(0, np.pi, 200)
linha_medicao, = ax.plot(R_medido_inicial * np.sin(theta), R_medido_inicial * (1 - np.cos(theta)), 
                         '--', color='orange', linewidth=2, label='Cursor de Medição (R)')

# 3. Painel de Resultados (Cálculo Experimental)
texto_resultados = ax.text(0.05, 0.95, '', transform=ax.transAxes, 
                           fontsize=11, verticalalignment='top',
                           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.legend(loc='lower right')

# Criação dos sliders
ax_V = plt.axes([0.1, 0.22, 0.8, 0.03], facecolor='lightgoldenrodyellow')
ax_I = plt.axes([0.1, 0.17, 0.8, 0.03], facecolor='lightcyan')
ax_R = plt.axes([0.1, 0.10, 0.8, 0.03], facecolor='mistyrose') # Slider de medição

v_slider = Slider(ax_V, 'Tensão (V)', 500, 5000, valinit=V_inicial, valstep=10)
i_slider = Slider(ax_I, 'Corrente (A)', 0.1, 5, valinit=I_inicial, valstep=0.05)
r_slider = Slider(ax_R, 'Medir Raio (m)', 0.01, 0.12, valinit=R_medido_inicial, valstep=0.001)

def atualizar(val):
    V = v_slider.val
    I = i_slider.val
    R_med = r_slider.val
    
    # Atualiza a física real do feixe
    x, y = gerar_feixe_real(V, I)
    linha_feixe.set_data(x, y)
    
    # Atualiza a posição da ferramenta de medição do usuário
    linha_medicao.set_data(R_med * np.sin(theta), R_med * (1 - np.cos(theta)))
    
    # Calcula o e/m experimental com base nos dados que o usuário forneceu
    B = campo_magnetico(I)
    e_m_exp = (2 * V) / ((B**2) * (R_med**2))
    
    # Calcula o erro em relação à literatura
    erro = abs(e_m_exp - e_m_teorico) / e_m_teorico * 100
    
    # Atualiza o placar
    texto_resultados.set_text(
        f'B Calculado = {B*1e3:.2f} mT\n'
        f'e/m Experimental = {e_m_exp:.3e} C/kg\n'
        f'Erro Percentual = {erro:.1f}%'
    )
    fig.canvas.draw_idle()

# Força a primeira atualização para preencher o placar no início
atualizar(0)

for slider in [v_slider, i_slider, r_slider]:
    slider.on_changed(atualizar)

plt.show()