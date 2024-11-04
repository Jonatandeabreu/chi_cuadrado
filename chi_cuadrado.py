import tkinter as tk
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def run_chi_squared():
    try:
        # Obtener los valores de entrada
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        d = int(entry_d.get())

        # Crear la tabla de contingencia
        data = np.array([[a, b],
                         [c, d]])

        # Realizar la prueba de chi-cuadrado
        chi2, p, dof, expected = stats.chi2_contingency(data)

        # Mostrar resultados en la ventana
        result_text = (f"Estadístico chi-cuadrado: {chi2:.4f}\n"
                       f"Valor p: {p:.4f}\n"
                       f"Grados de libertad: {dof}\n"
                       f"Frecuencias esperadas:\n{expected}")

        # Interpretar el valor p
        alpha 
        = 0.05
        if p < alpha:
            result_text += "\nSe rechaza la hipótesis nula (hay una asociación significativa)."
        else:
            result_text += "\nNo se rechaza la hipótesis nula (no hay asociación significativa)."

        # Mostrar los resultados en el label
        results_label.config(text=result_text)

        # Graficar las frecuencias observadas y esperadas
        plot_frequencies(data, expected)

    except ValueError:
        results_label.config(text="Por favor, ingrese solo números enteros.")

def plot_frequencies(observed, expected):
    labels = ['Grupo A Éxitos', 'Grupo A Fallos', 'Grupo B Éxitos', 'Grupo B Fallos']
    
    # Convertir a un solo vector para la gráfica
    observed_flat = observed.flatten()
    expected_flat = expected.flatten()
    
    x = np.arange(len(labels))  # las etiquetas para los grupos
    width = 0.35  # el ancho de las barras

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    bars1 = ax.bar(x - width/2, observed_flat, width, label='Observadas', color='skyblue')
    bars2 = ax.bar(x + width/2, expected_flat, width, label='Esperadas', color='orange')

    # Añadir etiquetas y título
    ax.set_ylabel('Frecuencia')
    ax.set_title('Frecuencias Observadas vs Esperadas')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Añadir anotaciones
    for bar in bars1 + bars2:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 puntos de desplazamiento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# Crear la ventana principal
root = tk.Tk()
root.title("Prueba de Chi-Cuadrado")

# Etiquetas y entradas para los datos
tk.Label(root, text="Grupo A Éxitos:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Grupo A Fallos:").grid(row=0, column=2)
entry_b = tk.Entry(root)
entry_b.grid(row=0, column=3)

tk.Label(root, text="Grupo B Éxitos:").grid(row=1, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=1, column=1)

tk.Label(root, text="Grupo B Fallos:").grid(row=1, column=2)
entry_d = tk.Entry(root)
entry_d.grid(row=1, column=3)

# Botón para ejecutar la prueba
button = tk.Button(root, text="Ejecutar Prueba", command=run_chi_squared)
button.grid(row=2, columnspan=4)

# Etiqueta para mostrar resultados
results_label = tk.Label(root, text="", justify=tk.LEFT)
results_label.grid(row=3, columnspan=4)

# Iniciar el bucle principal
root.mainloop()
