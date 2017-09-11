#  Materialenapp Buurman

Registratie van het verwerken van materialen van diversen milieuparken in Rotterdam.

###Documentation: 
Createsuperuser in manage.py 

####Commands to Run
- run manage.py migrate

#####Postgres database
db: materialendbv3
User: ...
Pass: ...

####Live Server
db: materialdb
user: nick 
pass: .... 

~/materialapp/manage.py migrate
~/materialapp/manage.py createsuperuser
~/materialapp/manage.py collectstatic
~/materialapp/manage.py runserver 0.0.0.0:8000

#####project env file 
source materialenappenv/bin/activate

#####Server packages: 
- Pip install pillow 
- Pip install reportlab
- pip install django-flat-responsive
- pip install django-resized
- pip install --pre xhtml2pdf

#####Django Flat Responsive
https://github.com/elky/django-flat-responsive

#####Django image:
http://www.bogotobogo.com/python/Django/Python_Django_Image_Files_Uploading_Example.php 

#####Django resize image:
https://github.com/un1t/django-resized

#####Django xhtml2pdf generator
https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django/