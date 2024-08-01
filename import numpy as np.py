import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, dstep, dlti, cont2discrete, lti, step, impulse

# Sistema 1: Modelo con parámetros m, b, k
# Parámetros del sistema
m = 1.0  # masa (kg)
b = 0.2  # coeficiente de fricción (Ns/m)
k = 1.0  # constante de restauración (N/m)
# Tiempo de muestreo
T1 = 0.5  # segundos
# Función de transferencia en el dominio continuo
num1 = [1]
den1 = [m, b, k]
G_s1 = lti(num1, den1)
# Transformación al dominio discreto usando Tustin
G_z1 = cont2discrete((num1, den1), T1, method='bilinear')
G_z1 = dlti(*G_z1[:2])

# Sistema 2: Modelo con parámetros K, zeta, omega_n
# Parámetros del sistema
K = 1.0  # Ganancia
zeta = 0.7  # Coeficiente de amortiguamiento
omega_n = 5.0  # Frecuencia natural
# Función de transferencia en el dominio continuo
num2 = [K]
den2 = [1, 2*zeta*omega_n, omega_n**2]
G_s2 = lti(num2, den2)
# Tiempo de muestreo para el dominio discreto
T2 = 0.1
# Discretización usando la transformación de Tustin
G_z2 = cont2discrete((num2, den2), T2, method='bilinear')
G_z2 = dlti(*G_z2[:2])

# Crear una figura para todas las gráficas
plt.figure(figsize=(12, 10))

# Respuesta al escalón en el dominio continuo (Sistema 1)
t_cont, y_cont_step = step(G_s1)
plt.subplot(2, 2, 1)
plt.plot(t_cont, y_cont_step)
plt.title('Escalón Continuo (Sistema 1)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Respuesta al impulso en el dominio continuo (Sistema 1)
t_cont, y_cont_impulse = impulse(G_s1)
plt.subplot(2, 2, 2)
plt.plot(t_cont, y_cont_impulse)
plt.title('Impulso Continuo (Sistema 1)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Respuesta al escalón en el dominio discreto (Sistema 1)
t_disc, y_disc_step = dstep(G_z1)
t_disc = np.squeeze(t_disc) * T1
y_disc_step = np.squeeze(y_disc_step)
plt.subplot(2, 2, 3)
plt.step(t_disc, y_disc_step)
plt.title('Escalón Discreto (Sistema 1)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Respuesta al impulso en el dominio discreto (Sistema 1)
t_disc, y_disc_impulse = dstep(G_z1)
t_disc = np.squeeze(t_disc) * T1
y_disc_impulse = np.squeeze(y_disc_impulse)
plt.subplot(2, 2, 4)
plt.step(t_disc, y_disc_impulse)
plt.title('Impulso Discreto (Sistema 1)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Mostrar la figura
plt.tight_layout()
plt.show()

# Nueva figura para el Sistema 2
plt.figure(figsize=(12, 10))

# Respuesta al escalón en el dominio continuo (Sistema 2)
t_cont, y_cont_step = step(G_s2)
plt.subplot(2, 2, 1)
plt.plot(t_cont, y_cont_step)
plt.title('Escalón Continuo (Sistema 2)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Respuesta al impulso en el dominio continuo (Sistema 2)
t_cont, y_cont_impulse = impulse(G_s2)
plt.subplot(2, 2, 2)
plt.plot(t_cont, y_cont_impulse)
plt.title('Impulso Continuo (Sistema 2)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Respuesta al escalón en el dominio discreto (Sistema 2)
t_disc, y_disc_step = dstep(G_z2)
t_disc = np.squeeze(t_disc) * T2
y_disc_step = np.squeeze(y_disc_step)
plt.subplot(2, 2, 3)
plt.step(t_disc, y_disc_step)
plt.title('Escalón Discreto (Sistema 2)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Respuesta al impulso en el dominio discreto (Sistema 2)
t_disc, y_disc_impulse = dstep(G_z2)
t_disc = np.squeeze(t_disc) * T2
y_disc_impulse = np.squeeze(y_disc_impulse)
plt.subplot(2, 2, 4)
plt.step(t_disc, y_disc_impulse)
plt.title('Impulso Discreto (Sistema 2)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Mostrar la figura
plt.tight_layout()
plt.show()

# Mostrar las funciones de transferencia
print('Función de transferencia en el dominio continuo (Sistema 1):')
print(G_s1)

print('Función de transferencia en el dominio discreto (Sistema 1):')
print(G_z1)

print('Función de transferencia en el dominio continuo (Sistema 2):')
print(G_s2)

print('Función de transferencia en el dominio discreto (Sistema 2):')
print(G_z2)
