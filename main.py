import pandas as pd
import matplotlib.pyplot as plt

ruta_al_archivo = r'C:\\Users\\peraz\\Downloads\\Prueba practica analista programador 18-06-2024.xlsx'

try:
    df = pd.read_excel(ruta_al_archivo, sheet_name='Puntajes')
    
    # columnas de porcentajes de temas
    temas = ['% de logro tema 1', '% de logro tema 2', '% de logro tema 3',
             '% de logro tema 4', '% de logro tema 5', '% de logro tema 6']
    
   
    (porcentajes) = df[temas].mean().multiply(100) 

    # figura y ejes (subplot)
    fig, ax = plt.subplots(figsize=(8, 5))

    # Crear un gráfico de barras horizontal
    bars = ax.barh(temas, porcentajes, color='yellow')

    # etiquetas de datos para cada barra
    for i,bar in enumerate (bars):
        height = porcentajes[i]
        ax.annotate(f'{height:.2f}%', xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + (bar.get_height())/2),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='center', fontsize=10, color='black')

    # título y etiquetas de los ejes
    ax.set_title('Porcentaje de Logro por Tema')
    ax.set_xlabel('Porcentaje (%)')
    ax.set_ylabel('Temas')

 
    #  mostrar el gráfico
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error al leer el archivo: {e}")
