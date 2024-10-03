# Práctica de laboratorio 7: Build a CI/CD Pipeline Using Jenkins

### Part 1: Launch the DEVASC VM

![alt text](images/image.png)

### Part 2: Commit the Sample App to Git

Creando repositorio en GitHub:
![alt text](images/image-1.png)

Configurando credenciales en la máquina virtual:

![alt text](images/image-2.png)

Inicializando repositorio local:

![alt text](images/image-3.png)

Enlazando con el repositorio remoto y agregando los archivos con add, commiteando y puseando a master:

![alt text](images/image-4.png)

El uso de contraseñas para la autenticación es más fácil de implementar, pero Github deprecó el uso de contraseñas para la autenticación por lo que se uso claves ssh.
Por ello tengo que crear una clave ssh:

![alt text](images/image-5.png)

con

```
cat ~/.ssh/id_rsa.pub
```

vemos la clave. Esta clave se añade a las llaves de mi cuenta de github:

![alt text](images/image-6.png)

Finalmente puedo pushear a mi repositorio remoto:

![alt text](images/image-7.png)

### Part 3: Modify the Sample App and Push Changes to Git

Ahora cambiemos achivos...

Se cambia el puerto en el .py y .hs:

![alt text](images/image-8.png)

![alt text](images/image-9.png)

Tenía el contenedor creado así que tuve que eliminar y volver a crearlo:

![](image-10.png)

![alt text](images/image-11.png)

Y vuelvo a ejecutar el .sh:

![alt text](images/image-12.png)

Listo, ya tenemos el contenedor funcionando con el nuevo puerto.

Por ultimo subimos los cambios a mi repositorio remoto:

![alt text](images/image-13.png)

Efectivamente se pushearon los cambios.

![alt text](images/image-14.png)

### Part 4: Download and Run the Jenkins Docker Image

#### Descargamos la imagen lts de jenkins con el comando:

```
docker pull jenkins/jenkins:lts
```

![alt text](images/image-15.png)

#### Empezamos el contenedor con el comando:

```
docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home --name jenkins_server jenkins/jenkins:lts
```

Tuve un error al iniciar el contenedor, por falta de memoria RAM; pero por más que le puse +10GB de RAM no me dejaba iniciar el contenedor.

![alt text](images/image-16.png)

Luego de insistentes errores al seguir con el laboratorio, decidí proseguir usando el Windows Subsytem for Linux (WSL). En particular estoy usando Arch Linux WSL.

Prendo docker daemon

![alt text](images/image-17.png)

Descargo la imagen de jenkins 2.414.3-slim-jdk17 que es compatible con la clave ssh con la que enlazé mi repositorio remoto:

![alt text](images/image-18.png)

Ejecuto el contenedor con el comando:

```
docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home --name jenkins_server jenkins/jenkins:2.414.3-slim-jdk17
```

![alt text](images/image-19.png)

Ahora sí me salió el mensaje con la contraseña:

![alt text](images/image-20.png)

1c50ae0907ff46828edce82287cd93e7

También me cersioro que esa es la contraseña al entrar al contenedor:

![alt text](images/image-21.png)

#### Configuramos jenkins:

Entramos con la contraseña que obtuvimos en localhost:8080

![alt text](images/image-22.png)

Instalamos los plugins sugeridos.

Skipeamos crear un usuario.

Dejé la config como estaba.

![alt text](images/image-23.png)

Listo! Ya estamos en el panel de jenkins.

![alt text](images/image-24.png)

#### Usamos jenkins para construir nuestra app:

Creamos un job BuildAppJob. Se eligió un Freestyle project.

![alt text](images/image-25.png)

Se establecieron el link del repositorio remoto y las credenciales de github en la configuración del job.

![alt text](images/image-26.png)

Se agregó un Build Step de tipo Execute shell con el comando de construcción del contenedor:

![alt text](images/image-27.png)

Se guardó la configuración.

#### Usamos jenkins para testear la construcción de nuestra app:

Le di a Build Now. Salida de consola:

![alt text](images/image-28.png)

![alt text](images/image-31.png)

Además observamos que se creó el contenedor `sampleapp` con el build. Se ve en la consola y también en mi WSL:

![alt text](images/image-29.png)

Y se puede acceder a la app:

![alt text](images/image-30.png)

#### Usamos jenkins para testear nuestra app

Se para y remueve el contenedor:

![alt text](images/image-32.png)

Creamos nuevo job para testing TestAppJob. Como Freestyle project.

![alt text](images/image-33.png)

Configuramos el job:

![alt text](images/image-34.png)

![alt text](images/image-35.png)

Corremos el BuildAppJob:

![alt text](images/image-36.png)

Como vemos se ejecutaron ambos jobs con éxito:

![alt text](images/image-37.png)

Log del testing:

![alt text](images/image-38.png)

Funcionando la app!:
![alt text](images/image-39.png)

#### Creamos pipeline en jenkins:

Cremos el item SamplePipeline de tipo Pipeline.

![alt text](images/image-40.png)

Configuramos la pipeline:

Agregamos Script:
![alt text](images/image-41.png)

Ejecutamos el pipeline:

![alt text](images/image-42.png)

Resultados:

Stage View:
![alt text](images/image-44.png)

Logs:

![alt text](images/image-43.png)

Además se comprobó que la app funcionaba.
