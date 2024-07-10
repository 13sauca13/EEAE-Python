# Python
Python: de 0 a E2T

---

:bookmark_tabs: **Índice de contenidos**

| --- | --- |
| [Introducción](#introduccion) | Qué es python y como preparar el equipo para usarlo |

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
