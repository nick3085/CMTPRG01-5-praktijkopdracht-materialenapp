# CMTPRG01-5-praktijkopdracht-materialenapp

:recycle: Registratie van het verwerken van materialen van diversen milieuparken in Rotterdam. :recycle:

**Info:**
- python 3.5.2
- pip 9.0.1
- Django 1.10.6.

**Start-up development**

Activate virtual environment:  
    `$ source venv/bin/activate`
    
Start server:
    `$ python manage.py runserver`
    
Deactivate virtual environment:  
    `$ deactivate`

**Local Database:**  
        `'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'materialdbv3',
        'USER': '',
        'PASSWORD': '', 
        'HOST': 'localhost',
        'PORT': '54321'`


**Server packages:**
- pip install psycopg2
- Pip install pillow 
- Pip install reportlab
- pip install django-flat-responsive
- Pip install django-resized
- pip install --pre xhtml2pdf


**Links to packages**
- Django Flat Responsive: https://github.com/elky/django-flat-responsive
- Django resize image: https://github.com/un1t/django-resized
- XHTML2PDF: https://github.com/xhtml2pdf/xhtml2pdf