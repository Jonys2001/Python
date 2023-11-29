# PEP8

### ¿Qué  es?
PEP 8 es una guía de estilo para escribir código Python de manera legible y consistente. PEP significa "Propuesta de Mejora de Python" y el número 8 es el número de esta propuesta en particular.

### ¿Para qué sirve?
PEP 8 sirve para que los desarrolladores sigan un estilo de codificación uniforme, lo que hace que el código sea más fácil de leer y entender para otros programadores. Además, ayuda a mantener la consistencia en proyectos grandes y colaborativos.

### ¿Cómo funciona?
PEP 8 establece reglas y recomendaciones sobre la estructura del código, la indentación, el espaciado, el nombramiento de variables y funciones, entre otros aspectos. Al seguir estas reglas, los desarrolladores pueden escribir código que sea fácilmente comprensible para otros y para ellos mismos en el futuro.

### Ejemplo
```python
def calcular_promedio(lista):
    total = sum(lista)
    cantidad_elementos = len(lista)
    promedio = total / cantidad_elementos
    return promedio

numeros = [1, 2, 3, 4, 5]
resultado = calcular_promedio(numeros)
print("El promedio es:", resultado)
```

# Modulos y Paquetes de Python

### ¿Por qué existen?
Los módulos y paquetes en Python existen para organizar el código en archivos reutilizables y estructurados. Los módulos son archivos individuales que contienen funciones, variables y clases, mientras que los paquetes son colecciones de módulos organizados en directorios.

### Diferencias
Módulos: Son archivos individuales que contienen código Python reutilizable. Pueden ser importados en otros scripts para utilizar las funciones y clases definidas en ellos.

Paquetes: Son directorios que contienen múltiples archivos de módulos y un archivo especial llamado __init__.py. Los paquetes permiten organizar los módulos relacionados en una estructura jerárquica.
### Ejemplo
#### 1 .- Módulo
El archivo operaciones.py tendra las siguientes funciones.
```python
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

```
Para utilizar esas funciones en otro archivo podemos importar estas funciones mediante el uso de import operaciones.
```python
import operaciones

resultado_suma = operaciones.suma(5, 3)
print("La suma es:", resultado_suma)

```
#### 2 .- Paquete
Tenemos la siguiente estructura de directorio.

    mi_paquete/
        init.py
        operaciones/
            init.py
            suma.py
            resta.py

Dentro de suma.py esta siguiente funcion.
```python
def suma(a, b):
    return a + b
```

Dentro de resta.py esta siguiente funcion.
```python
def resta(a, b):
    return a - b
```
Y para importar en forma de paquede se hara de la siguiente forma.
```python
from mi_paquete.operaciones import suma, resta

resultado_suma = suma(5, 3)
resultado_resta = resta(5, 3)

print("La suma es:", resultado_suma)
print("La resta es:", resultado_resta)
```
# Entornos Virtuales en Python

### ¿Qué son?
Los entornos virtuales en Python son herramientas que permiten crear entornos aislados donde puedes instalar paquetes y dependencias específicas para un proyecto, sin afectar el sistema o otros proyectos.

### ¿Cómo funcionan?
Cuando creas un entorno virtual, se crea una copia aislada del intérprete de Python y un espacio de trabajo separado para las bibliotecas y los paquetes. Esto te permite gestionar las dependencias de tu proyecto de forma independiente.

### Ejemplo
Para usar entornos virutales deberemos hacer lo siguiente en una linea de comandos.
```
python -m venv mi_entorno_virtual
```
Para esto ocuparemos pip, pip es un sistema de gestión de paquetes para Python. El nombre "pip" se deriva de la frase recursiva "Pip Installs Packages". En resumen, pip es una herramienta que te permite instalar y gestionar bibliotecas y paquetes de Python desde el Python Package Index (PyPI) de forma sencilla.

Ahora, para crear un entorno virtual lo podemos hace de dos manera:

Usando venv:
```
python -m venv mi_entorno_virtual
```

Usando virtualenv: 
```
virtualenv mi_entorno_virtual
```

Despues de crearlo deberemos activarlo, hay dos formas, una en sistemas linux y otra para sistemas Windows.

En sistemas Linux:
```
source mi_entorno_virtual/bin/activate
```
En sistemas Windows:
```
mi_entorno_virtual\Scripts\activate
```

Una vez qie el entorno este activo se podra instalar paquetes especificos usando 'pip'
```
pip install nombre_del_paquete
```

Y para apagar o dejar de usar el entorno virtual se debera usar el comando..

En linux:
```
deactivate
```
En windows:
```
mi_entorno_virtual\Scripts\deactivate
```
