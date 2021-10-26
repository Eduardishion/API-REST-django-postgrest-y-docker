# API-REST-django-postgrest-y-docker
Una API REST que pueda implementarse de manera local y que sus endpoints puedan ser accedidos por cualquier frontend (navegador) o programas como Postman, donde  se usa un contenedor de docker para la aplicación 


La versión de docker que se uso es:

    Docker version 20.10.9
    docker-compose version 1.26.0
 
 
Las imagenes usadas de python y postgrest son:

    imagen de python:3.7
    imagen de postgrest 11
    
Una ves instalados tanto docker y docker-compose

para constrir las images y descargar las dependecias 

    docker-compose build

iniciamos el servicio momentaniamente para crear usuario en django  

    docker-compose up -d
    

hacemos la migracion de los modelos a la base de datos 
    
    docker-compose exec web python manage.py makemigrations api
    docker-compose exec web python manage.py migrate


creamos un usuario para al admin de django 
    
    docker-compose exec web python manage.py createsuperuser

Elegimos el nombre y contrasela de usuario 
    
    
los comandos usados para poder iniciar el contenedor  y sus servicios
   
    docker-compose up

los entpoint para poder usar el api son:
  Para ver los recursos 
  
      http://0.0.0.0:8000/api/  
      
  
  Para ver un recurso mediante su ID
  
     http://0.0.0.0:8000/api/1
  
  Para modificarlo 
  
    http://0.0.0.0:8000/api/1/update
    
  Para eliminarlo 
  
    http://0.0.0.0:8000/api/1/delete
    
  Si desean detener el servicio 
    
    Ctrl + c
  
  

  
 
  
