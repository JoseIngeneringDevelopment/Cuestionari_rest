# Cuestionari_rest
Cuestionari_rest pretende ser un API para realizar cuestionarios que pueda ser consumida desde diferentes clientes.
La API  está desarrollada sobre Django REST Framework.

# Requerimientos
- Python 2.7+
- Django 1.9+
- Django CORS 1.1
- Django REST Framework 3.3.3

# Instalación (Develop)
- git clone git://github.com/JoseIngeneringDevelopment/Cuestionari_rest.git
- pip install -r requirements.txt
- python manage.py makemigrations cuestionario
- python manage.py makemigrations muestra
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

Con esto ya tenemeos el backend de Django y la API funcionando ahora sólo necesitamos ejecutar el cliente desde un navegador.
