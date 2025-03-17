# Construcción de un juego con Pygame

Vamos a crear un juego sencillo usando Pygame

> [!CAUTION]
> Pygame no está incluido en python por defecto! Hay que instalar la biblioteca:
> ```bash
> pip install pygame
> ```

## 1. Importar la biblioteca Pygame
Como siempre, necesitamos importar Pygame para usar sus funciones de gráficos y eventos.

```python
import pygame
```

Esto carga el módulo Pygame, que nos permite crear ventanas, dibujar formas y manejar eventos como teclas o clicks.

## 2. Inicializar Pygame
Pygame necesita inicializarse antes de usarlo para preparar sus sistemas internos.

```python
pygame.init()
```

`pygame.init()` configura Pygame para que podamos usar sus herramientas, como la pantalla y el manejo de eventos.

## 3. Crear la ventana
Definimos el tamaño de la ventana y la creamos.

```python
ancho, alto = 500, 400
pantalla = pygame.display.set_mode((ancho, alto))
```

- `ancho, alto = 500, 400`: Establece las dimensiones de la ventana (500x400 píxeles).
- `pygame.display.set_mode((ancho, alto))`: Crea la ventana y la almacena en la variable `pantalla`.

> [!TIP]
> También podemos darle un título a la ventana:
> ```python
> pygame.display.set_caption("Juego con Pygame")
> ```

## 4. Definir colores
Creamos variables para los colores. En pygame, los colores se definen usando valores RGB (Rojo, Verde, Azul).

```python
rojo = (255, 0, 0)
blanco = (255, 255, 255)
```

## 5. Establecer la posición inicial y velocidad del cuadrado

```python
x, y = ancho // 2, alto // 2
velocidad = 5
```

- `x, y = ancho // 2, alto // 2`: Ubica el cuadrado en el centro de la ventana independientemente de las dimensiones.
- `velocidad = 5`: Define el desplazamiento en cada paso (en pixeles).

## 6. Crear el bucle principal del juego

```python
jugando = True
while jugando:
  pygame.time.delay(30)
```

Este bucle mantiene la ventana abierta mientras `jugando` sea `True`.
Opcionalmente, dentro del bucle añadimos un delay que hace que el juego espere 30 milisegundos en cada iteración, evitando que el juego vaya demasiado rápido.

## 7. Manejar eventos
***Seguimos dentro del bucle ```wile```***
```python
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
```

- `pygame.event.get()`: Obtiene eventos del usuario.
- `if evento.type == pygame.QUIT`: Detecta si se cerró la ventana para salir del bucle.

## 8. Detectar teclas presionadas y mover el cuadrado

```python
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: x -= velocidad
    if teclas[pygame.K_RIGHT]: x += velocidad
    if teclas[pygame.K_UP]: y -= velocidad
    if teclas[pygame.K_DOWN]: y += velocidad
```

- `pygame.key.get_pressed()`: Verifica las teclas presionadas.
- Las teclas de flecha ajustan la posición del cuadrado.

## 9. Dibujar en la pantalla
Cada vez que el jugador se mueve, necesitamos limpiar la pantalla y volver a dibujar el cuadrado en su nueva posición:

```python
    pantalla.fill(blanco)
    pygame.draw.rect(pantalla, rojo, (x, y, 40, 40))
    pygame.display.update()
```

- `pantalla.fill(blanco)`: Borra la pantalla.
- `pygame.draw.rect(pantalla, rojo, (x, y, 40, 40))`: Dibuja el cuadrado rojo.
- `pygame.display.update()`: Actualiza la pantalla

## 10. Cerrar Pygame

```python
pygame.quit()
```

Esto cierra Pygame correctamente y libera los recursos usados (nos evitamos errores al ejecutar siguientes veces el programa).

---

Al final queda algo así:
```python
import pygame

pygame.init()

ancho, alto = 500, 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego con Pygame")

rojo = (255, 0, 0)
blanco = (255, 255, 255)

x, y = ancho // 2, alto // 2
velocidad = 5

jugando = True
while jugando:
    pygame.time.delay(30)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: x -= velocidad
    if teclas[pygame.K_RIGHT]: x += velocidad
    if teclas[pygame.K_UP]: y -= velocidad
    if teclas[pygame.K_DOWN]: y += velocidad
    
    pantalla.fill(blanco)
    pygame.draw.rect(pantalla, rojo, (x, y, 40, 40))
    pygame.display.update()

pygame.quit()
```

---

## Ideas de modificaciones:
- Añadir colisiones: Evita que el cuadrado salga de la pantalla.
- Cambiar de color: Haz que el cuadrado cambie de color al moverse.
- Incluir sonido: Usa ```pygame.mixer``` para agregar efectos de sonido. *Consulta la documentación oficial de la librería [AQUI](https://www.pygame.org/docs/ref/mixer.html)*
- Agregar un enemigo: Introduce un obstáculo que se mueva por la pantalla.
