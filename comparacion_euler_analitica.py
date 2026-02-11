"""
COMPARACIÓN: SOLUCIÓN ANALÍTICA vs MÉTODO DE EULER
===================================================
Problema: Modelo de Crecimiento Poblacional Exponencial

Ecuación Diferencial: dy/dt = k*y
Condición inicial: y(0) = y₀

Donde:
- y(t) = Población en el tiempo t
- k = Tasa de crecimiento (constante)
- y₀ = Población inicial

Intervalo: t ∈ [0, 1]
Paso de Euler: h = 0.2
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple

# ============================================================
# PARÁMETROS DEL PROBLEMA
# ============================================================
k = 1.5        # Tasa de crecimiento poblacional
y0 = 100       # Población inicial
t_inicio = 0   # Tiempo inicial
t_final = 1    # Tiempo final
h = 0.2        # Paso para método de Euler

print("=" * 70)
print("COMPARACIÓN: SOLUCIÓN ANALÍTICA vs MÉTODO DE EULER")
print("=" * 70)
print(f"\nProblema: Crecimiento Poblacional Exponencial")
print(f"Ecuación Diferencial: dy/dt = {k}*y")
print(f"Condición inicial: y(0) = {y0}")
print(f"\nParámetros:")
print(f"  - Intervalo: [{t_inicio}, {t_final}]")
print(f"  - Paso de Euler (h): {h}")
print(f"  - Tasa de crecimiento (k): {k}")

# ============================================================
# PARTE 1: SOLUCIÓN ANALÍTICA (SEPARACIÓN DE VARIABLES)
# ============================================================

def solucion_analitica(t: float, y0: float, k: float) -> float:
    """
    Solución analítica obtenida por separación de variables.
    
    Proceso de resolución:
    1. dy/dt = k*y
    2. dy/y = k*dt  (separación de variables)
    3. ∫(1/y)dy = ∫k*dt
    4. ln|y| = kt + C
    5. y = e^(kt + C) = e^C * e^(kt)
    6. Aplicando y(0) = y₀: y₀ = e^C
    7. Solución: y(t) = y₀ * e^(kt)
    
    Args:
        t: Tiempo
        y0: Población inicial
        k: Tasa de crecimiento
    
    Returns:
        Valor de y en el tiempo t
    """
    return y0 * np.exp(k * t)


print("\n" + "=" * 70)
print("PARTE 1: SOLUCIÓN ANALÍTICA")
print("=" * 70)
print("\nMétodo de Separación de Variables:")
print("  1. dy/dt = k*y")
print("  2. dy/y = k*dt  (separando variables)")
print("  3. ∫(1/y)dy = ∫k*dt")
print("  4. ln|y| = kt + C")
print("  5. y = e^(kt+C) = A*e^(kt), donde A = e^C")
print("  6. Con y(0) = y₀: y₀ = A*e^0 → A = y₀")
print(f"\nSolución exacta: y(t) = {y0} * e^({k}*t)")

# Generar puntos para la solución analítica (curva suave)
t_analitica = np.linspace(t_inicio, t_final, 100)
y_analitica = solucion_analitica(t_analitica, y0, k)

# ============================================================
# PARTE 2: SOLUCIÓN NUMÉRICA (MÉTODO DE EULER)
# ============================================================

def ecuacion_diferencial(t: float, y: float, k: float) -> float:
    """
    Función que define la ecuación diferencial dy/dt = f(t, y)
    
    Args:
        t: Tiempo (no usado en este caso, pero se incluye por convención)
        y: Valor actual de y
        k: Tasa de crecimiento
    
    Returns:
        Valor de dy/dt
    """
    return k * y


def metodo_euler(
    f: Callable,
    t0: float,
    y0: float,
    t_final: float,
    h: float,
    k: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Implementación del Método de Euler para EDOs de primer orden.
    
    Fórmula: y_{n+1} = y_n + h * f(t_n, y_n)
    
    Args:
        f: Función de la EDO dy/dt = f(t, y)
        t0: Tiempo inicial
        y0: Condición inicial
        t_final: Tiempo final
        h: Tamaño del paso
        k: Parámetro adicional para la ecuación
    
    Returns:
        Arrays de tiempo y valores aproximados de y
    """
    # Número de pasos
    n_pasos = int((t_final - t0) / h)
    
    # Inicializar arrays
    t_valores = np.zeros(n_pasos + 1)
    y_valores = np.zeros(n_pasos + 1)
    
    # Condición inicial
    t_valores[0] = t0
    y_valores[0] = y0
    
    # Aplicar método de Euler
    for i in range(n_pasos):
        t_valores[i + 1] = t_valores[i] + h
        y_valores[i + 1] = y_valores[i] + h * f(t_valores[i], y_valores[i], k)
    
    return t_valores, y_valores


print("\n" + "=" * 70)
print("PARTE 2: SOLUCIÓN NUMÉRICA (MÉTODO DE EULER)")
print("=" * 70)
print(f"\nFórmula de Euler: y_{{n+1}} = y_n + h * f(t_n, y_n)")
print(f"Donde f(t, y) = {k}*y")

# Aplicar método de Euler
t_euler, y_euler = metodo_euler(ecuacion_diferencial, t_inicio, y0, t_final, h, k)

print(f"\nNúmero de pasos: {len(t_euler) - 1}")
print("\nIteraciones del Método de Euler:")
print(f"{'n':<5} {'t_n':<10} {'y_n (Euler)':<20} {'y(t_n) (Exacta)':<20} {'Error Absoluto':<15}")
print("-" * 75)

for i, (t, y_e) in enumerate(zip(t_euler, y_euler)):
    y_exacta = solucion_analitica(t, y0, k)
    error = abs(y_e - y_exacta)
    print(f"{i:<5} {t:<10.2f} {y_e:<20.6f} {y_exacta:<20.6f} {error:<15.6f}")

# ============================================================
# PARTE 3: ANÁLISIS COMPARATIVO
# ============================================================

print("\n" + "=" * 70)
print("PARTE 3: ANÁLISIS COMPARATIVO")
print("=" * 70)

# Calcular errores
y_exacta_euler = solucion_analitica(t_euler, y0, k)
errores_absolutos = np.abs(y_euler - y_exacta_euler)
errores_relativos = (errores_absolutos / y_exacta_euler) * 100

# Estadísticas
error_max_abs = np.max(errores_absolutos)
error_promedio_abs = np.mean(errores_absolutos)
error_max_rel = np.max(errores_relativos)
error_promedio_rel = np.mean(errores_relativos)

print("\n📊 ESTADÍSTICAS DE ERROR:")
print(f"  Error absoluto máximo:    {error_max_abs:.6f}")
print(f"  Error absoluto promedio:  {error_promedio_abs:.6f}")
print(f"  Error relativo máximo:    {error_max_rel:.4f}%")
print(f"  Error relativo promedio:  {error_promedio_rel:.4f}%")

print(f"\n📈 VALORES FINALES (t = {t_final}):")
print(f"  Solución analítica:  {y_exacta_euler[-1]:.6f}")
print(f"  Método de Euler:     {y_euler[-1]:.6f}")
print(f"  Diferencia:          {abs(y_euler[-1] - y_exacta_euler[-1]):.6f}")

# ============================================================
# PARTE 4: VISUALIZACIÓN
# ============================================================

print("\n" + "=" * 70)
print("PARTE 4: GENERANDO VISUALIZACIONES")
print("=" * 70)

# Crear figura con 3 subgráficas
fig, axes = plt.subplots(3, 1, figsize=(12, 10))
fig.suptitle('Comparación: Solución Analítica vs Método de Euler\ndy/dt = ky, k=1.5, y(0)=100', 
             fontsize=14, fontweight='bold')

# Gráfica 1: Comparación de soluciones
ax1 = axes[0]
ax1.plot(t_analitica, y_analitica, 'b-', linewidth=2, label='Solución Analítica (Exacta)')
ax1.plot(t_euler, y_euler, 'ro-', markersize=8, linewidth=1.5, label=f'Método de Euler (h={h})')
ax1.set_xlabel('Tiempo (t)', fontsize=11)
ax1.set_ylabel('Población y(t)', fontsize=11)
ax1.set_title('Comparación de Soluciones', fontsize=12, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Gráfica 2: Error absoluto
ax2 = axes[1]
ax2.plot(t_euler, errores_absolutos, 'r^-', markersize=8, linewidth=2)
ax2.fill_between(t_euler, 0, errores_absolutos, alpha=0.3, color='red')
ax2.set_xlabel('Tiempo (t)', fontsize=11)
ax2.set_ylabel('Error Absoluto', fontsize=11)
ax2.set_title(f'Error Absoluto del Método de Euler (Máx: {error_max_abs:.4f})', 
              fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)

# Gráfica 3: Error relativo porcentual
ax3 = axes[2]
ax3.plot(t_euler, errores_relativos, 'gs-', markersize=8, linewidth=2)
ax3.fill_between(t_euler, 0, errores_relativos, alpha=0.3, color='green')
ax3.set_xlabel('Tiempo (t)', fontsize=11)
ax3.set_ylabel('Error Relativo (%)', fontsize=11)
ax3.set_title(f'Error Relativo Porcentual (Máx: {error_max_rel:.2f}%)', 
              fontsize=12, fontweight='bold')
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/comparacion_euler_analitica.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfica guardada como 'comparacion_euler_analitica.png'")

# Crear segunda figura: Zoom en los puntos de Euler
fig2, ax = plt.subplots(figsize=(10, 6))
ax.plot(t_analitica, y_analitica, 'b-', linewidth=2, alpha=0.7, label='Solución Exacta')
ax.plot(t_euler, y_euler, 'ro', markersize=10, label='Puntos de Euler')
ax.plot(t_euler, y_euler, 'r--', linewidth=1, alpha=0.5)

# Añadir flechas mostrando el error
for i in range(len(t_euler)):
    y_exacta_punto = solucion_analitica(t_euler[i], y0, k)
    ax.annotate('', xy=(t_euler[i], y_exacta_punto), xytext=(t_euler[i], y_euler[i]),
                arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))

ax.set_xlabel('Tiempo (t)', fontsize=12)
ax.set_ylabel('Población y(t)', fontsize=12)
ax.set_title('Visualización del Error en cada Paso de Euler', fontsize=13, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/error_visual_euler.png', dpi=300, bbox_inches='tight')
print("✓ Gráfica de error visual guardada como 'error_visual_euler.png'")

# ============================================================
# CONCLUSIONES
# ============================================================

print("\n" + "=" * 70)
print("CONCLUSIONES")
print("=" * 70)

print(f"""
1. SOLUCIÓN ANALÍTICA:
   La separación de variables proporciona la solución exacta:
   y(t) = {y0} * e^({k}*t)
   
2. MÉTODO DE EULER:
   Con un paso h = {h}, el método proporciona una aproximación
   razonable pero con error acumulativo.
   
3. PRECISIÓN:
   - El error absoluto máximo es {error_max_abs:.6f}
   - El error relativo máximo es {error_max_rel:.4f}%
   - El error crece con el tiempo debido a la naturaleza del método
   
4. OBSERVACIONES:
   - Un paso h más pequeño mejoraría la precisión
   - Para ecuaciones con crecimiento exponencial, el error se amplifica
   - El método de Euler es simple pero efectivo para análisis inicial
   
5. RECOMENDACIONES:
   - Para mayor precisión: usar h < 0.1
   - Considerar métodos más avanzados (Runge-Kutta) para mejor exactitud
   - Siempre comparar con solución analítica cuando sea posible
""")

print("=" * 70)
print("ANÁLISIS COMPLETADO")
print("=" * 70)

plt.show()
