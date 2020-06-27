# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

''' 
python manage.py makemigrations
python manage.py sqlmigrate miapp 0001  -> ver codigo SQL generado para la migracion
python manage.py migrate

'''

''' 
METODOS HTTP : 
    GET viaja en la ruta url
    POST viaja en el cabecero HTTP
'''


'''
pip install django-ckeditor 
model:
    content = RichTextField(verbose_name="Contenido")
INSTALLED_APPS += 'ckeditor',
'''