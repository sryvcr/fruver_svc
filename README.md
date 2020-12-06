# API REST con Django-Rest-Framework para Tienda de Víveres


#### Crear proyecto

```sh
$ mkdir groceries_store_svc
$ cd groceries_store_svc
$ virtualenv . -p python3
$ mkdir src
$ cd src
```

#### Aplicar requerimientos
```sh
$ source ../bin/activate
$ (groceries_store_svc) pip install -r requirements.txt
```

#### Configurar base de datos
```sh
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg',
            'NAME': 'groceries_store_db',
            'USER': 'admin',
            'PASSWORD': 'secret',
            'HOST': '0.0.0.0',
            'PORT': '5432',
        }
}
```
 
### Crear proyecto y apps
En cada carpeta nueva que se crea en el project no olvidar el archivo __init__.py si no se crea
automaticamente, para que Django reconozca el directorio como parte del proyecto
```sh
$ (groceries_store_svc) cd src/
$ (groceries_store_svc) django-admin startproject groceries_store
$ (groceries_store_svc) cd groceries_store
$ (groceries_store_svc) mkdir apps/
$ (groceries_store_svc) cd apps/
$ (groceries_store_svc) django-admin startapp products_providers

```

#### Aplicar migraciones

```sh
$ (groceries_store_svc) cd src/
$ (groceries_store_svc) python manage.py makemigrations
$ (groceries_store_svc) python manage.py migrate
```

#### Iniciar
```sh
$ (groceries_store_svc) python manage.py runserver
```