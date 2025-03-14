# Importamos las librerías necesarias
import random  # Para generar números aleatorios
import tkinter as tk  # Para la interfaz gráfica

# Función que simula el lanzamiento de un dado
def lanzar_dado():
    # Genera un número aleatorio entre 1 y 6
    numero = random.randint(1, 6)
    # Actualiza el texto de la etiqueta con el resultado del lanzamiento
    label_resultado.config(text=f"Su número es: {numero}")

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Lanzar dado")  # Establecer el título de la ventana

# Crear un botón que, al ser presionado, llama a la función 'lanzar_dado'
boton = tk.Button(root, text="Lanzar dado", command=lanzar_dado)
boton.pack(pady=10)  # Agregar el botón a la ventana con un espacio vertical

# Crear una etiqueta que mostrará el resultado del lanzamiento
label_resultado = tk.Label(root, text="Presiona para lanzar el dado")
label_resultado.pack(pady=10)  # Agregar la etiqueta con espacio vertical

# Iniciar el bucle principal de la ventana para que la interfaz sea interactiva
root.mainloop()
