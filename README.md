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
  

  
 
  
