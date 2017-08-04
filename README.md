Django Rest JWT
---------------
JWT authentication in your Django Rest Framework project with Postgres.

Requirements
------------
Django Rest JWT is a Python Django based platform. 

- Python 3.4.3
- Django 1.11.3
- Postgres

Installation
------------
Following are the steps to install this platform.

- Get in the root directory of the project
- Create Virtual Environment
```sh
$ cd ..
$ virtualenv -p python3 django_rest_jwt_venv
$ cd django_rest_jwt
$ source ../django_rest_jwt_venv/bin/activate
```
- Install Requirements
```sh
$ pip install -r requirements.txt
```
- Setting up the Database
```sh
$ cd django_rest_jwt
$ pwd //It should display like this "/Users/(user)/django_rest_jwt/django_rest_jwt"
$ sudo vim local_settings.py
    //Add the code below and save the file
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_rest_jwt',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    // Note: Settings are for POSTGRES SQL
$ cd .. 
$ python manage.py migrate 
```

Testing
-------
I have added the unit tests as well. Through following commands you can run all the tests.

```sh
python manage.py test  
```
To run any specific test if you want to:
```sh
python manage.py test authentication.tests.UserLoginAPITests.test_login_user 
```

Don't forget to give Star to the repo. Happy Coding!