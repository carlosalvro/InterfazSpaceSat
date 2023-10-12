# Interfaz SpaceSat
Interfaz para las misiones de SpaceSat

Proyecto realizado para mostrar los datos recibidos por un cansat.

Los datos son enviados por el cansat y recibidos por una antena que manda los datos por el puerto serial a la computadora.

La interfaz está desarrollada con Flask, utilizando principalmente las librerias de Flask-SocketIO y Flask-Serial.

Se recomienda utilizar un ambiente virtual e instalar las librerías que se encuentran en `requirements.txt`

La estructura del projecto es la siguiente 

```txt
| --Maquetas/             #son las maquetas en html
|-- |----- index.html
|-- |----- styles.css
|
| -- static/              #Son los archivos externos
|----|--- css/
|---------|--- styles.css
       |        
|----|--- images/
|----------|--- LogoSpaceSatArea.png
|----------|--- LogoSpaceSatArea.svg
|
| -- templates/           #Son las plantillas en html de las rutas 
|----|--- ajustes.html
|----|--- conexion.html
|----|--- dashboard.html
|----|--- layout.html     #Esta es la plantilla principal 
|
|
| -- app.py       #El archivo principal 
| -- config.py    #configuración de parametros de la pagina 
| -- rutas.py     #Aqui se definen las distintas rutas de la pagina 
| -- requirements.txt  #se definen todas las librerias utilizadas en el proyecto 
| -- data.json    #Aqui se definen los valores que se mostraran en el dashboard
| -- .gitignore
```



------------
Para correr el programa basta con correr en la terminal 
    `flask run`

------------

La antena tiene que mandar una trama como la siguiente 
`{'Al':13, 'Lo':45,'La':21}`
En este caso la antena recibe los datos de 'Al' que podria ser altitud, 'Lo' longitud y 'La' Latitud, cada uno con sus respectivos valores

Para que se presenten estos datos en la interfaz, en el documento `data.json`
Se tienen que definir de la siguiente manera
```json
[
  {
    "name": "Altitud",
    "short_name": "Al"
  },
  {
    "name": "Longitud",
    "short_name": "Lo"
  },
  {
    "name": "Latitud",
    "short_name": "La"
  }
]
```
Así la interfaz sabrá que el valor que aparece en la trama como 'Al':83, es la latitud y que tiene un valor de 83. Si en la trama el valor aparece como "AL" y en el `data.json` como "Al", la interfaz no mostrará dicho valor.

Para más información consultar la documentación de Flask 

https://flask.palletsprojects.com/en/3.0.x/
