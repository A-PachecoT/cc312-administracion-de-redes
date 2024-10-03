# Laboratorio 3a - Crear una prueba unitaria de Python

## Instrucciones

### Parte 1: Iniciar la máquina virtual (Virtual Machine) de DEVASC

Hecho!

### Parte 2: Explorar las opciones en el framework unittest

![alt text](images/image.png)

### Parte 3: Probar una función Python con unittest

#### Paso 1: Revisar el archivo test_data.py

![alt text](images/image-1.png)

#### Paso 2: Crear la función json_search() que se va a probar

```
nano recursive_json_search.py
```

![alt text](images/image-2.png)

Como es de esperar no funciona
![alt text](images/image-3.png)

#### Paso 3: Crear algunas pruebas unitarias

Se arreglo los errores de sintáxis de recursive_json_search.py
![alt text](images/image-7.png)
Prueba unitaria:
![alt text](images/image-6.png)

#### Paso 4: Ejecutar la prueba para ver los resultados iniciales

![alt text](images/image-5.png)

Como vemos hay errores.

#### Paso 5: Investigar y corregir el primer error

#### Paso 6: Ejecutar la prueba de nuevo

![alt text](images/image-9.png)

#### Paso 7: Investigar y corregir el segundo error

![alt text](images/image-8.png)

### Extra pasos

Me di cuenta que el error que me salía era porque puse una mayúscula `S` en lugar de `s` en `test_json_search.py`, en `self.asertisInstance`. Además que es `self.asertIsInstance`.
![alt text](images/image-10.png)

Luego de esos 2 cambios, la prueba unitaria funcionó.

![alt text](images/image-11.png)

## Reflexión

En este laboratorio se aprendió a crear pruebas unitarias en Python utilizando el framework unittest. Se exploraron los conceptos de clases de prueba, métodos de prueba, y manejo de aserciones. Además, se trabajó con estructuras de datos JSON y se aplicaron técnicas de recursividad para buscar información dentro de los datos.

Este conocimiento es esencial para garantizar la calidad del software, ya que permite verificar que el código funcione correctamente bajo diferentes escenarios y condiciones. Las pruebas unitarias son fundamentales para asegurar que los cambios en el código no introduzcan nuevos errores y para garantizar que el software cumpla con los requisitos esperados.
