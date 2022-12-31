# django_restaurant_menu

*Django сайт, отображающий меню ресторана, с возможностью изменения и редактирования меню из панели администратора, просмотра отчетов в виде графиков и импорта в различных форматах.
В проекте реализована кастомная админ-панель jazzmin.*

*Пользователь может просматривать категории меню, смотреть информацию о блюде в выбранной категории.*
![1vp2nRyANA](https://user-images.githubusercontent.com/84034483/210130936-d53e02d0-cfd5-4e94-9639-9cd84a85b7e9.gif)


*Администратору предоставляется возможность вносить меню и редактировать его из панели администратора. Для доступа к панели администратора нужно иметь права staff или superuser.*
![hv8GLNonta](https://user-images.githubusercontent.com/84034483/210131006-9a718cc6-8657-442c-9b7c-c332df30eb48.gif)


*Администратор может формировать отчеты по лучшим позициям в меню, самым активным пользователям и тп.*
![JM19qVFy4J](https://user-images.githubusercontent.com/84034483/210131049-25cd6d22-ab82-4472-8ee2-7c7eb9b63c6c.gif)

## Запуск проекта
   * Версия python 3.10+
   * База данных PostgreSQL 15.1
   * Устанавливаем зависимости из requirements.txt: `pip install -r requirements.txt` Для Unix-систем вместо `pip` потребуется `pip3`.
   * Для подключения к базе данных добавьте в переменные окружения:
     - `DB_NAME` (имя вашей базы данных PostgreSQL)
     - `DB_USER` (имя вашего пользователя PostgreSQL)
     - `DB_PASSWORD` (пароль вашего пользователя PostgreSQL)
     - `DB_HOST` (хост вашей базы данных PostgreSQL)
     - `DB_PORT` (порт вашей базы данных PostgreSQL)
     
     
     Либо пропишите данные непосредственно в файле settings.py:   
     ```
     DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': your-db-name,
            'USER': your-db-user,
            'PASSWORD': your-db-password,
            'HOST': your-db-host-ip,
            'PORT': your-db-port,
        }
      }
     ```  
   * После подключения базы данных проведите миграции командами `python manage.py makemigration` и `python manage.py migrate`. Это создаст стандартные django таблицы и пользовательские таблицы для формирования меню.
   * Для доступа к панели администратора и отчетам нужно создать суперпользователя командой `python manage.py createsuperuser`. Перейти в админ панель на сайте можно нажатием мыши в левый верхний угол.
   * Проект запускается командой `python manage.py runserver`

     
