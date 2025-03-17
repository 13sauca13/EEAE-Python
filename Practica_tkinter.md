# Construccion de un entorno gráfico con Tkinter

Esta guía detalla paso a paso la creación de una interfaz gráfica para la clase `Calculadora` de los ejercios de repaso de la asignatura usando la biblioteca `tkinter` (incluida en Python).

## 1. Importar las bibliotecas necesarias
Antes de comenzar, necesitamos importar `tkinter` para crear la interfaz gráfica y `messagebox` para mostrar mensajes de error.

> [!TIP]
> Podríamos importar toda la librería como hacíamos hasta ahora ```from tkinter import *```, eso nos ahorraría tener que poner ```tkinter.``` antes de cada uso de las funciones de la librería, pero a la larga podríamos tener problemas usando como nombres
> de variables elementos de tkinter y viceversa.
>
> En Python, usar import * no es recomendado (según la guía de estilo PEP 8) porque:
> - Hace difícil rastrear de dónde vienen las funciones o clases.
> - Puede ocultar errores al sobrescribir nombres sin darnos cuenta.
> 
> **Importar solo lo necesario o usar un alias como tk mejora la legibilidad y mantenibilidad del código.**
> *tkinter es un módulo grande con muchos submódulos y messagebox no está incluido directamente en el espacio de nombres principal de tkinter, por lo que necesitamos importarlo explícitamente si queremos usarlo.*

```python
import tkinter as tk
from tkinter import messagebox
```

- `tkinter`: Biblioteca principal para crear ventanas y elementos gráficos.
- `messagebox`: Módulo para mostrar mensajes emergentes (como errores).

Tambien podemos utilizar la clase `Calculadora` desde su archivo original haciendo una importación:
```python
from calculadora_base import Calculadora
```
De esta manera, si habíamos creado un menú en la línea de comandos con ```if __name__ == "__main__" .... ``` el menú no saltará y además reaprovechamos código. **WIN - WIN** :wink:

## 2. Definir la clase CalculadoraGUI
Creamos una clase llamada `CalculadoraGUI` que manejará toda la interfaz gráfica. Esta clase necesita una ventana principal (`root`).
El nombre "root" no es obligatorio; es solo una variable, sin embargo se ha convertido en una convención ampliamente aceptada en tutoriales y la comunidad de Python.

```python
class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
```

- `__init__`: Método constructor que se ejecuta al crear la clase.
- `self.root`: Guarda la ventana principal pasada como parámetro.
- `title`: Define el título de la ventana como "Calculadora".
- `geometry`: Establece el tamaño de la ventana (300 píxeles de ancho por 400 de alto).

## 3. Crear los elementos de la interfaz
Añadimos etiquetas, campos de entrada, botones y un área para mostrar resultados dentro del constructor `__init__`:

### 3.1 Etiquetas y campos de entrada
```python
tk.Label(root, text="Número 1:").pack(pady=5)
self.entry1 = tk.Entry(root)
self.entry1.pack(pady=5)

tk.Label(root, text="Número 2:").pack(pady=5)
self.entry2 = tk.Entry(root)
self.entry2.pack(pady=5)
```

- `tk.Label`: Crea una etiqueta con texto.
- `tk.Entry`: Crea un campo donde el usuario puede escribir números.
- `self.entry1` y `self.entry2`: Guardamos los campos como atributos para usarlos más tarde.
- `pack(pady=5)`: Coloca los elementos en la ventana con 5 píxeles de espacio vertical (como el padding de HTML...).

### 3.2 Botones para las operaciones
```python
tk.Button(root, text="Sumar", command=self.calcular_suma).pack(pady=5)
tk.Button(root, text="Restar", command=self.calcular_resta).pack(pady=5)
tk.Button(root, text="Multiplicar", command=self.calcular_multiplicacion).pack(pady=5)
tk.Button(root, text="Dividir", command=self.calcular_division).pack(pady=5)
```

- `tk.Button`: Crea botones con texto.
- `command`: Vincula cada botón a un método que definiremos luego (ej. `calcular_suma`).
- `pack(pady=5)`: Coloca los botones con espacio vertical.

### 3. Área para mostrar el resultado
```python
self.resultado_label = tk.Label(root, text="Resultado: ")
self.resultado_label.pack(pady=20)
```

- `self.resultado_label`: Etiqueta donde se mostrará el resultado, guardada como atributo.
- `pady=20`: Mayor espacio vertical para separar del resto.

## 4. Método para obtener y validar los números
Creamos un método auxiliar para leer los números ingresados por el usuario y ya que estamos, usamos ```try - except``` para verificar que sean válidos.

```python
def get_numeros(self):
    try:
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        return num1, num2
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos")
        return None, None
```

- `self.entry1.get()`: Obtiene el texto del primer campo.
- `float()`: Convierte el texto a número decimal.
- `try/except`: Maneja errores si el usuario ingresa letras u otros valores no numéricos.
- `messagebox.showerror`: Muestra un mensaje emergente si hay error.
- `return`: Devuelve los números si son válidos, o `None` si hay error.

## 5. Métodos para las operaciones
Creamos un método por cada operación. Cada uno usa la clase `Calculadora` para calcular y muestra el resultado.

> [!WARNING]
> :eyes: **OJO!** Mi calculadora recibe los números como argumentos en el constructor.
>
> Si nuestra clase Calculadora pide input se cortaría "la experiencia gráfica" y nos pediría introducirlos por consola... :vomiting_face:
> Hay que atender a las particularidades de como hayamos programado la calculadora... FÍJATE EN TU CONSTRUCTOR y en como instanciar tu clase.

### 5.1 Método para sumar
```python
def calcular_suma(self):
    num1, num2 = self.get_numeros()
    if num1 is not None:
        calc = Calculadora(num1, num2)
        resultado = calc.sumar()
        self.resultado_label.config(text=f"Resultado: {resultado}")
```

- `get_numeros()`: Obtiene los números ingresados.
- `if num1 is not None`: Verifica que los números sean válidos.
- `Calculadora(num1, num2)`: Crea una instancia de la clase `Calculadora`.
- `calc.sumar()`: Llama al método `sumar` de `Calculadora`.
- `config(text=...)`: Actualiza la etiqueta con el resultado.

### 5.2 Métodos para las otras operaciones
Repetimos el mismo proceso para restar, multiplicar y dividir:

```python
def calcular_resta(self):
    num1, num2 = self.get_numeros()
    if num1 is not None:
        calc = Calculadora(num1, num2)
        resultado = calc.restar()
        self.resultado_label.config(text=f"Resultado: {resultado}")

def calcular_multiplicacion(self):
    num1, num2 = self.get_numeros()
    if num1 is not None:
        calc = Calculadora(num1, num2)
        resultado = calc.multiplicar()
        self.resultado_label.config(text=f"Resultado: {resultado}")

def calcular_division(self):
    num1, num2 = self.get_numeros()
    if num1 is not None:
        calc = Calculadora(num1, num2)
        resultado = calc.dividir()
        self.resultado_label.config(text=f"Resultado: {resultado}")
```

## 6. Ejecutar la aplicación
Añadimos el código para iniciar la ventana al final del archivo.

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
```

- `tk.Tk()`: Crea la ventana principal.
- `CalculadoraGUI(root)`: Crea una instancia de nuestra interfaz.
- `mainloop()`: Inicia el bucle que mantiene la ventana abierta.

## 7. Probar la calculadora
1. Ejecuta el código completo.
2. Ingresa dos números en los campos.
3. Haz clic en un botón (Sumar, Restar, etc.).
4. Observa el resultado en la etiqueta inferior.
5. Prueba con valores inválidos (letras) o división por cero para ver los mensajes de error.
