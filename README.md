# wayak-website
a travel agency bookings [Django](https://github.com/erickbytes/wayak-website) website for
[Wayak Viajes](https://www.facebook.com/wayakviajes/)

**Install Python Libraries**
```pip install Django```

**Django Commands**


Start dev server:
```python manage.py runserver```

generate new app structure:
```python manage.py startapp bookings```

Generate migrations for DB
```python manage.py makemigrations bookings```

peek SQL
```python manage.py sqlmigrate bookings 0001```

Migrate DB
```python manage.py migrate```

View DB from shell:
```python manage.py shell```
