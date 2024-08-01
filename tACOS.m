clc;
clear all;

% Sistema 1: Modelo con parámetros m, b, k
% Parámetros del sistema
m = 1.0;  % masa (kg)
b = 0.2;  % coeficiente de fricción (Ns/m)
k = 1.0;  % constante de restauración (N/m)
% Tiempo de muestreo
T1 = 0.5;  % segundos
% Definición de la función de transferencia en el dominio continuo
s = tf('s');
G_s1 = 1 / (m*s^2 + b*s + k);
% Transformación al dominio discreto usando Tustin
G_z1 = c2d(G_s1, T1, 'tustin');

% Sistema 2: Modelo con parámetros K, zeta, omega_n
% Parámetros del sistema
K = 1.0;         % Ganancia
zeta = 0.7;    % Coeficiente de amortiguamiento
omega_n = 5.0;   % Frecuencia natural
% Función de transferencia en el dominio continuo
num = K;
den = [1 2*zeta*omega_n omega_n^2];
G_s2 = tf(num, den);
% Tiempo de muestreo para el dominio discreto
T2 = 0.1;
% Discretización usando la transformación de Tustin
G_z2 = c2d(G_s2, T2, 'tustin');

% Crear una figura para todas las gráficas
figure;

% Respuesta al escalón en el dominio continuo (Sistema 1)
subplot(2,2,1);
step(G_s1,10);
title('Escalón Continuo (Sistema 1)');
grid on;

% Respuesta al impulso en el dominio continuo (Sistema 1)
subplot(2,2,2);
impulse(G_s1);
title('Impulso Continuo (Sistema 1)');
grid on;

% Respuesta al escalón en el dominio discreto (Sistema 1)
subplot(2,2,3);
step(G_z1);
title('Escalón Discreto (Sistema 1)');
grid on;

% Respuesta al impulso en el dominio discreto (Sistema 1)
subplot(2,2,4);
impulse(G_z1);
title('Impulso Discreto (Sistema 1)');
grid on;

% Nueva figura para el Sistema 2
figure;

% Respuesta al escalón en el dominio continuo (Sistema 2)
subplot(2,2,1);
step(G_s2);
title('Escalón Continuo (Sistema 2)');
grid on;

% Respuesta al impulso en el dominio continuo (Sistema 2)
subplot(2,2,2);
impulse(G_s2);
title('Impulso Continuo (Sistema 2)');
grid on;

% Respuesta al escalón en el dominio discreto (Sistema 2)
subplot(2,2,3);
step(G_z2);
title('Escalón Discreto (Sistema 2)');
grid on;

% Respuesta al impulso en el dominio discreto (Sistema 2)
subplot(2,2,4);
impulse(G_z2);
title('Impulso Discreto (Sistema 2)');
grid on;

% Mostrar las funciones de transferencia
disp('Función de transferencia en el dominio continuo (Sistema 1):');
G_s1
disp('Función de transferencia en el dominio discreto (Sistema 1):');
G_z1

disp('Función de transferencia en el dominio continuo (Sistema 2):');
G_s2
disp('Función de transferencia en el dominio discreto (Sistema 2):');
G_z2
