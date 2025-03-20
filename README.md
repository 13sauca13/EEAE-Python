# Python
Python: de 0 a E2T

---

| :bookmark_tabs: **Índice de contenidos** | |
| --- | --- |
| [Introducción](#introduccion) | Qué es python y como preparar el equipo para usarlo |
| [Fase online](#fase-online) | Muy "self-explanatory"... Los contenidos de la fase Online |
| [Fase presencial](#fase-presencial) | Importar librerías |
| | Uso de listas |
| | Clases |
| | Uso de diccionarios |
| | Archivos JSON |
| | Libreria OS |
| | Manejo de excepciones: try - except |

> [!IMPORTANT]
>
> Los ejercicios pueden entregarse por GIT en este repositorio: [EEAE-Python2025](https://github.com/13sauca13/EEAE-Python2025) o por medio del [NCVCDEF](https://www.campusdefensa.es/mod/assign/view.php?id=211394)
> 
> :memo: [Ejercicios de repaso](https://github.com/13sauca13/EEAE-Python/blob/main/Ejercicios_repaso.md)
>
> :brain: [Práctica avanzada 1: Tkinter](https://github.com/13sauca13/EEAE-Python/blob/main/Practica_tkinter.md)
>
> :brain:[Práctica avanzada 2: Pygame](https://github.com/13sauca13/EEAE-Python/blob/main/Practica_pygame.md)
---
## Introducción
### Qué es python y por qué python?
Python es un lenguaje de programación de alto nivel para programación de propósito general. Es un lenguaje de programación de código abierto, interpretado y orientado a objetos (veremos más adelante lo que es esto).
Python fue creado por un programador holandés, Guido van Rossum. El nombre del lenguaje de programación deriva de una serie de comedia británica, Monty Python's Flying Circus, y la primera versión se lanzó el 20 de febrero de 1991.

Es un lenguaje de programación muy parecido al lenguaje humano y por eso es fácil de aprender y usar, también al ser de propósito general se ha utilizado para desarrollar aplicaciones web, aplicaciones de escritorio, administración de sistemas, etc. Python también es un lenguaje muy utilizado en la comunidad de la ciencia de datos y aprendizaje automático.
### Comenzar a usar Python
Para empezar a usar python es necesaio preparar nuestro equipo (aunque la mayoría de distribuciones de sistemas UNIX ya lo traen por defecto, incluido macOS).
#### Instalar Python
Lo primero es acceder a la web de [Python](https://www.python.org/) para descargar la distribución que nuestro equipo necesite en función de su sistema operativo

![Descarga python](https://github.com/13sauca13/Python/assets/33026257/f40e77f5-5e42-4675-bd6f-b48821e2dcba)

Al ejecutar el instalador es importante añadir python al PATH (El PATH es una variable de entorno del sistema que le indica al sistema operativo dónde buscar los ejecutables de los programas cuando los ejecutamos), de no acerlo habría que indicarle al sistema la ruta de python cada vez que queramos ejecutar algo. Usaremos la instalación completa y ya iremos viendo lo que incluye a medida que lo vayamos utilizando.

![Captura de pantalla 2024-07-02 230132](https://github.com/13sauca13/Python/assets/33026257/d22fe7c8-b54d-4515-82bc-22a1c9254e90)

>[!TIP]
>Finalizando la instalación nos saldrá un aviso sobre si queremos "Disable path length limit", esto es porque Windows tiene un límite de caracteres en la ruta de los archivos (260 caracteres) y se nos ofrece la opción de deshabilitarlo (cosa que no se podía hacer hasta 2016 y que en UNIX no ocurría)
>
>Puedes deshabilitarlo o no, no es relevante

Una vez lo hayamos descargado e instalado podemos verificar que todo ha salido bien y comprobar la versión que tenemos instalada accediendo a la terminal si usamos UNIX o al símbolo de sistema si usamos Windows y ejecutando el siguiente comando:
```shell
python --version
```
![image](https://github.com/13sauca13/Python/assets/33026257/e1699c89-29a4-4a15-ab8d-35f5b9c6c86e)

Como se puede ver en la foto estoy utilizando la version 3.12.4 de python. Si has llegado hasta aquí y puedes ver la versión tienes python correctamente instalado en tu máquina, enhorabuena, estás preparado para continuar y empezar a escribir código en python.
#### La shell de Python
Python es un lenguaje interpretado, por lo que no es necesario compilarlo. Python viene con un Python Shell (Python Interactive Shell) que se utiliza para ejecutar un único comando de Python y obtener el resultado.

Python Shell espera el código python del usuario, lo interpreta y muestra el resultado en la siguiente línea.

Vamos a abrir la consola de comandos para escribir:
```shell
python
```
Al hacer esto se nos abrirá la shell de python y podremos empezar a escribir código después de ```>>>```.
![image](https://github.com/13sauca13/Python/assets/33026257/a0526241-ad36-4ffc-9382-b1628ab0f157)

Vamos a probar a escibir algo, probemos con:
```shell
3 + 6
```

Funciona?

Pronto veremos el lenguaje en si, por ahora es una prueba de que todo marcha como debería.

Para salir de la shell de python basta con escribir ```exit()```. De este modo volveremos a la terminal del sistema.

### El "Visual Studio Code"
La shell de Python es buena para probar códigos pequeños, pero no para un proyecto grande. En un entorno de trabajo real, los desarrolladores utilizan diferentes editores de código. Nosotros usaremos Visual Studio Code, que siendo puristas es un editor de código, no un IDE, pero siendo gratuito y con todas las extensiones y la comunidad detrás es probablemente de las mejores opciones para empezar.

Empezamos por descargar el programa de la web oficial de [Visual Studio Code](https://code.visualstudio.com/Download) ( :warning: *OJO!! No confundir Visual Studio con Visual Studio Code... No son lo mismo*)

![image](https://github.com/13sauca13/Python/assets/33026257/f8f1db2c-6b7e-4a63-8cda-9645d0283322)
Durante la instalación debemos marcar la opción de agregar Code al PATH (ya vimos los motivos anteriormente), por lo demás podemos elegir lo que queramos. Una vez instalado tendremos el editor sin ninguna extensión, las iremos agregando a medida que avancemos, la primera apertura se verá así:

![image](https://github.com/13sauca13/Python/assets/33026257/9a7d923e-c082-410e-af40-9cf300c94cba)

Ahora toca instalar la extensión de python. Como ya dijimos, el Visual Studio Code es un editor de texto, necesitamos una extensión para que pueda ejecutar python, pulsamos en la barra izquierda el acceso a Extensions o usamos el atajo ```Ctrl+Shift+X``` y en la barra de búsqueda ponemos "python" e instalamos la extensión con ese nombre.

![image](https://github.com/13sauca13/Python/assets/33026257/b8b1a692-7d62-4388-b9b6-e6a2254f5d94)

Ahora crearemos una carpeta para nuestros archivos en cualquier lugar del equipo y en el acceso de Explorer de la barra izquierda o con el atajo ```Ctrl+Shift+E``` pulsamos en "Open Folder", seleccionamos nuestra carpeta y en el aviso de seuridad decimos "Yes, I trust the authors".

**Ahora si que ya estamos listos para empezar**

## Fase online
Los contenidos de la fase online son los impartidos en el [Python Essentials 1 de Cisco](https://www.netacad.com/courses/python-essentials-1?courseLang=es-XL)

## Fase presencial
### 1. Uso e importación de librerías

#### Concepto de librerías
Las librerías en Python son colecciones de módulos que contienen funciones y clases predefinidas que facilitan la programación. Utilizar librerías permite reutilizar código y simplificar tareas complejas.

#### Importación de librerías
Para utilizar una librería en Python, primero debes importarla. Hay varias formas de hacerlo:

1. **Importación básica**:
   ```python
   import math
   ```
   Esto importa toda la librería `math`, y puedes acceder a sus funciones usando el prefijo `math.`.

2. **Importación específica**:
   ```python
   from math import sqrt, pi
   ```
   Esto importa solo las funciones `sqrt` y `pi` de la librería `math`, permitiendo su uso directo sin prefijo.

3. **Uso de alias**:
   ```python
   import numpy as np
   ```
   Esto importa la librería `numpy` y le asigna el alias `np`, facilitando su uso con un nombre más corto.

#### Librerías estándar
Python viene con una gran cantidad de librerías estándar que puedes usar sin necesidad de instalación adicional. Algunos ejemplos incluyen:

- **math**: Funciones matemáticas como `sqrt()`, `sin()`, `cos()`, `pi`.
  ```python
  import math
  print(math.sqrt(16))  # Output: 4.0
  ```

- **datetime**: Manejo de fechas y horas.
  ```python
  import datetime
  now = datetime.datetime.now()
  print(now)  # Output: Current date and time
  ```

- **random**: Generación de números aleatorios.
  ```python
  import random
  print(random.randint(1, 10))  # Output: Random integer between 1 and 10
  ```
  
#### Ejecución de funciones con `if __name__ == "__main__":`
Cuando se ejecuta un script de Python, la variable especial `__name__` se establece en `"__main__"`. Esto permite que el código dentro del bloque `if __name__ == "__main__":` se ejecute solo cuando el script se ejecuta directamente, y no cuando se importa como un módulo.

```python
def main():
    print("Esta función se ejecuta cuando el script se ejecuta directamente.")

if __name__ == "__main__":
    main()
```

#### Instalación de librerías externas
Para utilizar librerías que no están incluidas en la instalación estándar de Python, puedes usar `pip`, el gestor de paquetes de Python. Por ejemplo, para instalar `numpy` y `pandas`:

```bash
pip install numpy pandas
```

Una vez instaladas, puedes importarlas en tu código:

```python
import numpy as np
import pandas as pd
```

#### Ejemplo práctico
Vamos a ver un ejemplo práctico que utiliza varias librerías:

```python
import math
import datetime
import random

# Uso de math
print(f"Raíz cuadrada de 25: {math.sqrt(25)}")

# Uso de datetime
now = datetime.datetime.now()
print(f"Fecha y hora actuales: {now}")

# Uso de random
random_number = random.randint(1, 100)
print(f"Número aleatorio entre 1 y 100: {random_number}")
```

### 2. Manejo de listas

#### Creación de listas
Las listas en Python son colecciones ordenadas y mutables que permiten almacenar elementos de diferentes tipos. Se crean utilizando corchetes `[]`.

```python
# Lista vacía
lista_vacia = []

# Lista con elementos
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]
```

#### Acceso a elementos
Puedes acceder a los elementos de una lista utilizando índices, que comienzan en 0. También puedes usar índices negativos para acceder a los elementos desde el final de la lista.

```python
lista = [10, 20, 30, 40, 50]

# Acceso a elementos
print(lista[0])  # Output: 10
print(lista[-1]) # Output: 50

# Slicing
print(lista[1:3])  # Output: [20, 30]
print(lista[:3])   # Output: [10, 20, 30]
print(lista[2:])   # Output: [30, 40, 50]
```

#### Métodos de listas
Las listas en Python tienen varios métodos incorporados que permiten manipular sus elementos:

- **append()**: Añade un elemento al final de la lista.
  ```python
  lista = [1, 2, 3]
  lista.append(4)
  print(lista)  # Output: [1, 2, 3, 4]
  ```

- **extend()**: Extiende la lista añadiendo todos los elementos de otra lista.
  ```python
  lista = [1, 2, 3]
  lista.extend([4, 5])
  print(lista)  # Output: [1, 2, 3, 4, 5]
  ```

- **insert()**: Inserta un elemento en una posición específica.
  ```python
  lista = [1, 2, 3]
  lista.insert(1, 1.5)
  print(lista)  # Output: [1, 1.5, 2, 3]
  ```

- **remove()**: Elimina la primera aparición de un elemento.
  ```python
  lista = [1, 2, 3, 2]
  lista.remove(2)
  print(lista)  # Output: [1, 3, 2]
  ```

- **pop()**: Elimina y devuelve el elemento en una posición específica (por defecto, el último).
  ```python
  lista = [1, 2, 3]
  elemento = lista.pop()
  print(elemento)  # Output: 3
  print(lista)    # Output: [1, 2]
  ```

- **sort()**: Ordena los elementos de la lista.
  ```python
  lista = [3, 1, 2]
  lista.sort()
  print(lista)  # Output: [1, 2, 3]
  ```

- **reverse()**: Invierte el orden de los elementos de la lista.
  ```python
  lista = [1, 2, 3]
  lista.reverse()
  print(lista)  # Output: [3, 2, 1]
  ```

#### Listas por comprensión
Las listas por comprensión son una forma concisa de crear listas. Permiten generar listas nuevas aplicando una expresión a cada elemento de una secuencia.

```python
# Lista de cuadrados de números del 0 al 9
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

También puedes añadir condiciones a las listas por comprensión:

```python
# Lista de números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Output: [0, 2, 4, 6, 8]
```

### Ejemplo práctico
Vamos a ver un ejemplo práctico que utiliza varios métodos de listas y listas por comprensión:

```python
# Crear una lista de números del 1 al 10
numeros = list(range(1, 11))

# Añadir un número al final de la lista
numeros.append(11)

# Insertar un número en la segunda posición
numeros.insert(1, 1.5)

# Eliminar el número 1.5
numeros.remove(1.5)

# Ordenar la lista en orden descendente
numeros.sort(reverse=True)

# Crear una lista de cuadrados de los números en la lista
cuadrados = [x**2 for x in numeros]

print("Números:", numeros)
print("Cuadrados:", cuadrados)
```

### 3. Clases: Métodos (constructor, getters y setters) y Atributos

#### Concepto de clases y objetos
La programación orientada a objetos (POO) es un paradigma de programación que utiliza "objetos" y "clases". Una **clase** es un molde o plantilla que define las propiedades y comportamientos (métodos) que tendrán los objetos creados a partir de ella. Un **objeto** es una instancia de una clase.

#### Definición de clases
Para definir una clase en Python, se utiliza la palabra clave `class` seguida del nombre de la clase y dos puntos. Dentro de la clase, se definen los atributos y métodos.

```python
class Persona:
    pass  # Una clase vacía
```

#### Métodos
Los métodos son funciones definidas dentro de una clase que describen los comportamientos de los objetos de esa clase.

##### Constructor
El **constructor** es un método especial que se llama automáticamente cuando se crea un nuevo objeto. En Python, el constructor se define con el método `__init__()`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
```

##### Getters y Setters
Los **getters** y **setters** son métodos que permiten acceder y modificar los atributos de una clase de manera controlada.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado

    # Getter para nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter para edad
    def get_edad(self):
        return self.__edad

    # Setter para edad
    def set_edad(self, edad):
        self.__edad = edad
```

#### Atributos
Los atributos son variables que pertenecen a una clase. Pueden ser de instancia (pertenecen a cada objeto) o de clase (compartidos por todos los objetos de la clase).

##### Atributos de instancia
Se definen dentro del método `__init__()` y son únicos para cada objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

##### Atributos de clase
Se definen fuera de cualquier método y son compartidos por todos los objetos de la clase.

```python
class Persona:
    especie = "Humano"  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

### Ejemplo práctico
Vamos a ver un ejemplo práctico que utiliza clases, métodos (incluyendo constructor, getters y setters) y atributos:

```python
class Persona:
    especie = "Humano"  # Atributo de clase

    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo de instancia privado
        self.__edad = edad      # Atributo de instancia privado

    # Getter para nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter para edad
    def get_edad(self):
        return self.__edad

    # Setter para edad
    def set_edad(self, edad):
        self.__edad = edad

    # Método para mostrar información
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, Especie: {Persona.especie}")

# Crear un objeto de la clase Persona
persona1 = Persona("Alice", 30)

# Usar getters y setters
print(persona1.get_nombre())  # Output: Alice
persona1.set_nombre("Bob")
print(persona1.get_nombre())  # Output: Bob

# Mostrar información
persona1.mostrar_informacion()  # Output: Nombre: Bob, Edad: 30, Especie: Humano
```

### 4. Manejo de diccionarios

#### Creación de diccionarios
Los diccionarios en Python son colecciones desordenadas de pares clave-valor. Se crean utilizando llaves `{}` y cada par clave-valor se separa por dos puntos `:`.

```python
# Diccionario vacío
diccionario_vacio = {}

# Diccionario con elementos
diccionario = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}
```

#### Acceso a elementos
Puedes acceder a los valores de un diccionario utilizando sus claves.

```python
print(diccionario["nombre"])  # Output: Alice
print(diccionario["edad"])    # Output: 30
```

Para evitar errores si la clave no existe, puedes usar el método `get()`.

```python
print(diccionario.get("nombre"))  # Output: Alice
print(diccionario.get("pais", "No especificado"))  # Output: No especificado
```

#### Métodos de diccionarios
Los diccionarios en Python tienen varios métodos incorporados que permiten manipular sus elementos:

- **keys()**: Devuelve una vista de las claves del diccionario.
  ```python
  print(diccionario.keys())  # Output: dict_keys(['nombre', 'edad', 'ciudad'])
  ```

- **values()**: Devuelve una vista de los valores del diccionario.
  ```python
  print(diccionario.values())  # Output: dict_values(['Alice', 30, 'Madrid'])
  ```

- **items()**: Devuelve una vista de los pares clave-valor del diccionario.
  ```python
  print(diccionario.items())  # Output: dict_items([('nombre', 'Alice'), ('edad', 30), ('ciudad', 'Madrid')])
  ```

- **update()**: Actualiza el diccionario con los pares clave-valor de otro diccionario.
  ```python
  diccionario.update({"pais": "España"})
  print(diccionario)  # Output: {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid', 'pais': 'España'}
  ```

- **pop()**: Elimina y devuelve el valor asociado a una clave.
  ```python
  edad = diccionario.pop("edad")
  print(edad)  # Output: 30
  print(diccionario)  # Output: {'nombre': 'Alice', 'ciudad': 'Madrid', 'pais': 'España'}
  ```

- **clear()**: Elimina todos los elementos del diccionario.
  ```python
  diccionario.clear()
  print(diccionario)  # Output: {}
  ```

#### Diccionarios por comprensión
Los diccionarios por comprensión son una forma concisa de crear diccionarios. Permiten generar diccionarios nuevos aplicando una expresión a cada par clave-valor de una secuencia.

```python
# Diccionario de cuadrados de números del 1 al 5
cuadrados = {x: x**2 for x in range(1, 6)}
print(cuadrados)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

También puedes añadir condiciones a los diccionarios por comprensión:

```python
# Diccionario de números pares y sus cuadrados del 1 al 10
pares_cuadrados = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(pares_cuadrados)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

### Ejemplo práctico
Vamos a ver un ejemplo práctico que utiliza varios métodos de diccionarios y diccionarios por comprensión:

```python
# Crear un diccionario con información de una persona
persona = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a elementos
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")

# Añadir un nuevo par clave-valor
persona["pais"] = "España"

# Actualizar un valor existente
persona["edad"] = 31

# Eliminar un par clave-valor
ciudad = persona.pop("ciudad")

# Mostrar claves, valores y pares clave-valor
print("Claves:", persona.keys())
print("Valores:", persona.values())
print("Pares clave-valor:", persona.items())

# Crear un diccionario de cuadrados de números del 1 al 5
cuadrados = {x: x**2 for x in range(1, 6)}
print("Cuadrados:", cuadrados)
```

### 5. Archivos JSON: estructura de un JSON y librería JSON

#### Estructura de un JSON
JSON (JavaScript Object Notation) es un formato de texto ligero para el intercambio de datos. Es fácil de leer y escribir para los humanos y fácil de analizar y generar para las máquinas. La estructura de un JSON se basa en pares clave-valor y puede incluir los siguientes tipos de datos:

- **Objetos**: Colecciones de pares clave-valor encerradas entre llaves `{}`.
  ```json
  {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
  }
  ```

- **Arrays**: Listas ordenadas de valores encerradas entre corchetes `[]`.
  ```json
  {
    "nombres": ["Alice", "Bob", "Charlie"]
  }
  ```

- **Valores**: Pueden ser cadenas de texto, números, booleanos, nulos, objetos o arrays.
  ```json
  {
    "cadena": "Hola",
    "numero": 123,
    "booleano": true,
    "nulo": null
  }
  ```

#### Librería JSON
Python incluye una librería estándar llamada `json` que permite trabajar con archivos JSON. Esta librería proporciona métodos para convertir datos entre JSON y Python, así como para leer y escribir archivos JSON.

##### Conversión de Python a JSON
Para convertir un objeto de Python a una cadena JSON, se utiliza el método `json.dumps()`.

```python
import json

# Diccionario de Python
persona = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}

# Convertir a JSON
persona_json = json.dumps(persona)
print(persona_json)  # Output: {"nombre": "Alice", "edad": 30, "ciudad": "Madrid"}
```

##### Conversión de JSON a Python
Para convertir una cadena JSON a un objeto de Python, se utiliza el método `json.loads()`.

```python
import json

# Cadena JSON
persona_json = '{"nombre": "Alice", "edad": 30, "ciudad": "Madrid"}'

# Convertir a diccionario de Python
persona = json.loads(persona_json)
print(persona)  # Output: {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid'}
```

##### Lectura y escritura de archivos JSON
Para leer y escribir archivos JSON, se utilizan los métodos `json.dump()` y `json.load()`.

###### Escritura de archivos JSON
```python
import json

# Diccionario de Python
persona = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}

# Escribir en un archivo JSON
with open("persona.json", "w") as archivo:
    json.dump(persona, archivo)
```

###### Lectura de archivos JSON
```python
import json

# Leer desde un archivo JSON
with open("persona.json", "r") as archivo:
    persona = json.load(archivo)
    print(persona)  # Output: {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid'}
```

### Ejemplo práctico
Vamos a ver un ejemplo práctico que utiliza la librería `json` para convertir datos entre JSON y Python, y para leer y escribir archivos JSON:

```python
import json

# Diccionario de Python
persona = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}

# Convertir a JSON
persona_json = json.dumps(persona)
print("JSON:", persona_json)

# Convertir de JSON a diccionario de Python
persona_dict = json.loads(persona_json)
print("Diccionario:", persona_dict)

# Escribir en un archivo JSON
with open("persona.json", "w") as archivo:
    json.dump(persona, archivo)

# Leer desde un archivo JSON
with open("persona.json", "r") as archivo:
    persona_leida = json.load(archivo)
    print("Leído desde archivo:", persona_leida)
```

### 6. Librería OS

#### Concepto de librería OS
La librería `os` en Python proporciona una forma de interactuar con el sistema operativo. Permite realizar operaciones como manipulación de archivos y directorios, ejecución de comandos del sistema, y obtención de información del entorno del sistema.

#### Métodos comunes
La librería `os` incluye muchos métodos útiles. Aquí hay algunos de los más comunes:

##### `os.getcwd()`
Devuelve el directorio de trabajo actual.

```python
import os

directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")
```

##### `os.listdir()`
Devuelve una lista con los nombres de los archivos y directorios en el directorio especificado. Si no se especifica ningún directorio, usa el directorio actual.

```python
import os

contenido = os.listdir()
print(f"Contenido del directorio actual: {contenido}")
```

##### `os.mkdir()`
Crea un nuevo directorio con el nombre especificado.

```python
import os

os.mkdir("nuevo_directorio")
print("Directorio 'nuevo_directorio' creado.")
```

##### `os.rename()`
Renombra un archivo o directorio.

```python
import os

os.rename("nuevo_directorio", "directorio_renombrado")
print("Directorio renombrado a 'directorio_renombrado'.")
```

##### `os.remove()`
Elimina un archivo.

```python
import os

# Crear un archivo para eliminar
with open("archivo_para_eliminar.txt", "w") as archivo:
    archivo.write("Este archivo será eliminado.")

# Eliminar el archivo
os.remove("archivo_para_eliminar.txt")
print("Archivo 'archivo_para_eliminar.txt' eliminado.")
```

##### `os.rmdir()`
Elimina un directorio vacío.

```python
import os

os.rmdir("directorio_renombrado")
print("Directorio 'directorio_renombrado' eliminado.")
```

#### Manipulación de rutas
La librería `os` también proporciona funciones para manipular rutas de archivos y directorios a través del módulo `os.path`.

##### `os.path.join()`
Une uno o más componentes de ruta de manera inteligente.

```python
import os

ruta = os.path.join("directorio", "subdirectorio", "archivo.txt")
print(f"Ruta unida: {ruta}")
```

##### `os.path.exists()`
Comprueba si una ruta especificada existe.

```python
import os

existe = os.path.exists("directorio")
print(f"¿Existe el directorio 'directorio'? {existe}")
```

##### `os.path.isfile()`
Comprueba si una ruta especificada es un archivo.

```python
import os

es_archivo = os.path.isfile("archivo.txt")
print(f"¿Es 'archivo.txt' un archivo? {es_archivo}")
```

##### `os.path.isdir()`
Comprueba si una ruta especificada es un directorio.

```python
import os

es_directorio = os.path.isdir("directorio")
print(f"¿Es 'directorio' un directorio? {es_directorio}")
```

### Ejemplo práctico
Vamos a ver un ejemplo práctico que utiliza varios métodos de la librería `os` y `os.path` para manipular archivos y directorios:

```python
import os

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Listar el contenido del directorio actual
contenido = os.listdir()
print(f"Contenido del directorio actual: {contenido}")

# Crear un nuevo directorio
os.mkdir("nuevo_directorio")
print("Directorio 'nuevo_directorio' creado.")

# Renombrar el nuevo directorio
os.rename("nuevo_directorio", "directorio_renombrado")
print("Directorio renombrado a 'directorio_renombrado'.")

# Crear un archivo en el nuevo directorio
ruta_archivo = os.path.join("directorio_renombrado", "archivo.txt")
with open(ruta_archivo, "w") as archivo:
    archivo.write("Contenido del archivo.")

# Comprobar si el archivo existe
existe_archivo = os.path.exists(ruta_archivo)
print(f"¿Existe el archivo 'archivo.txt'? {existe_archivo}")

# Eliminar el archivo
os.remove(ruta_archivo)
print("Archivo 'archivo.txt' eliminado.")

# Eliminar el directorio
os.rmdir("directorio_renombrado")
print("Directorio 'directorio_renombrado' eliminado.")
```

¡Claro! Aquí tienes el punto 7 añadido al esquema:

### 7. Manejo de excepciones: `try - except`

#### Concepto de excepciones
Las excepciones son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de las instrucciones. En Python, las excepciones se manejan utilizando bloques `try` y `except`.

#### Uso de `try - except`
El bloque `try` contiene el código que puede generar una excepción, mientras que el bloque `except` contiene el código que se ejecutará si ocurre una excepción.

```python
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción de tipo ZeroDivisionError
    print("Error: División por cero.")
```

#### Múltiples excepciones
Puedes manejar múltiples excepciones utilizando varios bloques `except`.

```python
try:
    # Código que puede generar una excepción
    resultado = int("texto")
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Valor no válido.")
```

#### Excepción genérica
Si no sabes qué tipo de excepción puede ocurrir, puedes usar una excepción genérica.

```python
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except Exception as e:
    print(f"Error: {e}")
```

#### Bloques `else` y `finally`
El bloque `else` se ejecuta si no ocurre ninguna excepción, y el bloque `finally` se ejecuta siempre, ocurra o no una excepción.

```python
try:
    # Código que puede generar una excepción
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: División por cero.")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Este bloque se ejecuta siempre.")
```

### Ejemplo práctico
Vamos a ver un ejemplo práctico que utiliza el manejo de excepciones para controlar errores en la entrada de datos:

```python
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: División por cero.")
        return None
    else:
        return resultado
    finally:
        print("Operación de división completada.")

# Solicitar entrada de datos al usuario
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = dividir(num1, num2)
    if resultado is not None:
        print(f"Resultado: {resultado}")
except ValueError:
    print("Error: Entrada no válida.")
```
