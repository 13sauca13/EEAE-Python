# Construcción de un juego con Pygame

Vamos a crear un juego sencillo usando Pygame

> [!CAUTION]
> Pygame no está incluido en python por defecto! Hay que instalar la biblioteca:
> ```bash
> pip install pygame
> ```

## 1. Importar la biblioteca Pygame
Antes de empezar, necesitamos importar Pygame para usar sus funciones de gráficos y eventos.

```python
import pygame
```

Esto carga el módulo Pygame, que nos permite crear ventanas, dibujar formas y manejar eventos como teclas o clicks.

## 2: Inicializar Pygame
Pygame necesita inicializarse antes de usarlo para preparar sus sistemas internos.

```python
pygame.init()
```

`pygame.init()` configura Pygame para que podamos usar sus herramientas, como la pantalla y el manejo de eventos.

## 3: Crear la ventana
Definimos el tamaño de la ventana y la creamos.

```python
ancho, alto = 500, 400
pantalla = pygame.display.set_mode((ancho, alto))
```

- `ancho, alto = 500, 400`: Establece las dimensiones de la ventana (500x400 píxeles).
- `pygame.display.set_mode((ancho, alto))`: Crea la ventana y la almacena en la variable `pantalla`.

## 4: Definir colores
Creamos variables para los colores en formato RGB (rojo, verde, azul).

```python
rojo = (255, 0, 0)
blanco = (255, 255, 255)
```

## 5: Establecer la posición inicial y velocidad del cuadrado

```python
x, y = ancho // 2, alto // 2
velocidad = 5
```

- `x, y = ancho // 2, alto // 2`: Ubica el cuadrado en el centro de la ventana.
- `velocidad = 5`: Define el desplazamiento en cada paso.

## 6: Crear el bucle principal del juego

```python
jugando = True
while jugando:
```

Este bucle mantiene la ventana abierta mientras `jugando` sea `True`.

## 7: Controlar la velocidad de actualización

```python
    pygame.time.delay(30)
```

Esto pausa la ejecución por 30 milisegundos en cada iteración.

## 8: Manejar eventos

```python
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
```

- `pygame.event.get()`: Obtiene eventos del usuario.
- `if evento.type == pygame.QUIT`: Detecta si se cerró la ventana.

## 9: Detectar teclas presionadas y mover el cuadrado

```python
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: x -= velocidad
    if teclas[pygame.K_RIGHT]: x += velocidad
    if teclas[pygame.K_UP]: y -= velocidad
    if teclas[pygame.K_DOWN]: y += velocidad
```

- `pygame.key.get_pressed()`: Verifica las teclas presionadas.
- Las teclas de flecha ajustan la posición del cuadrado.

## 10: Dibujar en la pantalla

```python
    pantalla.fill(blanco)
    pygame.draw.rect(pantalla, rojo, (x, y, 40, 40))
```

- `pantalla.fill(blanco)`: Borra la pantalla.
- `pygame.draw.rect(pantalla, rojo, (x, y, 40, 40))`: Dibuja el cuadrado rojo.

## 11: Actualizar la pantalla

```python
    pygame.display.update()
```

Esto refresca la ventana para reflejar los cambios.

## 12: Cerrar Pygame

```python
pygame.quit()
```

Esto cierra Pygame y libera los recursos usados.
