# wayak-website
a travel agency bookings [Django](https://www.djangoproject.com/) website for
[Wayak Viajes](https://www.facebook.com/wayakviajes/)

## Install Django

```pip install Django```

## Django Commands

start development server

```python manage.py runserver```

generate new app structure

```python manage.py startapp bookings```

generate migrations for DB

```python manage.py makemigrations bookings```

peek SQL

```python manage.py sqlmigrate bookings 0001```

migrate DB

```python manage.py migrate```

view DB from shell:

```python manage.py shell```
