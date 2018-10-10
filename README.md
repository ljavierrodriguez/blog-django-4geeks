# BLOG EN DJANGO
## INSTRUCCIONES

#### Ejecutar para clonar el repositorio
git clone https://github.com/ljavierrodriguez/blog-django-4geeks.git

##### Ingresamos dentro de la carpeta del proyecto
cd blog-django-4geeks

##### Creamos el entorno virtual para el proyecto
python -m venv env

##### Instalamos todas las dependencias del proyecto
pip install -r requeriments.txt

##### Creamos la base de datos y migramos todas las tablas a la misma
python manage.py migrate

##### Seguimos las instrucciones para crear el super usuario
python manage.py createsuperuser

##### Ponemos en marcha nuestro servidor web con el siguiente comando
python manage.py runserver

##### En el navegador escribimos y entramos con el usuario que hemos creado anteriormente
http://localhost:8000/admin/