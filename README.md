### Project built for Coderhouse Pyhon and Django fullstack course

### Entrega 1 - Marelli

# Blog de finanzas

Readme con el paso a paso para utilizar nuestro proyecto. Requiere:

    -Python 3.8 o superior
    -Git
    -Paquete para creacion y uso de entornos virtuales de Python
    -Editor de texto de preferencia 
    -Navegador web.

## Configuracion del proyecto

### Terminal

Abrimos la terminal y creamos la carpeta para alojar el proyecto(podemos usar otro nombre):

    mkdir blog_de_finanzas


#### Git y github

Creamos un repositorio vacio y traemos desde GitHub el proyecto:

    git init
    
    git pull https://github.com/PabloDerRohe/entrega1_marelli.git

Estructura de carpetas del proyecto:

    < blog_de_finanzas >
            | ->  < blogfinanzas >
            | ->  < index >
            | ->  < pages >
            | ->  < account >
            | ->  < direct >
            | ->  .gitignore
            | ->  manage.py
            | ->  README.md
            | ->  requirements.txt

#### Python

Creamos un entorno virtual e instalamos los paquetes necesarios para poder correr el proyecto:

Python venv:

    python3 -m venv venv
    
    pip install -r requirements.txt

Una vez instalado todo, posicionados en la carpeta root del proyecto realizamos las migraciones para crear la base de datos.

    python3 manage.py migrate

Crear usuario administrador para poder manejar el proyecto desde /admin e engresamos usuario y contrasena para administrador:

    python3 manage.py createsuperuser


Corremos el servidor para poder explorar el proyecto:

    python3 manage.py runserver

Pipenv:

## Exploramos el proyecto

## Navegador web

Una vez que el servidor este corriendo, abrimos nuestro navegador y abrimos  `127.0.0.1:8000` o `localhost:8000` y nos lleva a la pagina de inicio del proyecto.

### Index

La pagina index tiene una introduccion al blog y nos permite a traves de dos botones rapidamente ver los post y crear un usuario.  

En la parte superior se encuentra la barra de navegacion donde podemos acceder al resto de las funcionalidades del proyecto.

### Posts

Una vez abierto la seccion *posts* podemos leer el listado completo de publicaciones con su titulo, autor y contenido.

Podemos tambien crear un nuevo post usando el boton *Crear Post* y ahi dentro completamos los distintos campos y le damos a crear.

Por ultimo podemos buscar un titulo completo usando el buscador con el mismo procedimiento.  

### Usuarios

Cuando ingresamos a la seccion usuarios nos aparece la lista de los mismos y podemos crear uno nuevo, buscar por alguno en particular o varios bajo el mismo nombre, editar alguno o borrar. 

## En construccion
