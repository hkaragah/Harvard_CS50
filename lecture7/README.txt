Django:
    - Similar to Flask is used to build web app, but with more features

    - It is suggested to have a dedicated virtual environment for each Django project, 
        and one way to manage a virtual environment is venv, which is included in Python.
        - Windows: py -m venv venv
        - MacOS: python -m venv venv

    - Then you have to activate the environment
        - window: venv\Scripts\activate
        - MacOS: source venv/bin/activate

    - we are ready to install Django.
        - Windows: py -m pip install Django
        - MacOS: python -m pip install Django
    - Check Django version;
        - django-admin --version

    - Create a new project:
        - django-admin startproject <projectname>
        - The following files are created with each new project:
            - __init__.py: indicates that 'mysite' directory is a Python package
            - manage.py: used to perform operation on the web app
            - setting.py: contains all settings for the app, e.g. type of database
            - urls.py: determine what urls users can go to when the visit the app 
                (simialr to @app.route decorator in Flask, but Django separates 
                these files and stores them into urls.py)
                App directories will be included in this files as they are created.
            - wsgi.py: allow to deploy the app to a web-server
            - asgi.py:
            - project_name/: folder containing all the above files
        - Apps run from the parent project directory. So it is aware of all sub-directory apps

    - Create a basic web app inside this folder using the CLI and 'manage.py':
        - python manage.py startapp hello
        - This create a new folder inside the project folder with the specified name 'hello'
            containing new files
            - views.py: similar to app.py in flask app (determine what users see)
            - urls.py: contains all urls specific to this app
                (different from urls.py in the project folder which is related to project urls)
        - Add the new app to the list of installed apps in settings.py

    - Run project:
        - python manage.py runserver

    - Migrations: look for any changes in app files and 
        automatically make changes the database accordingly to match
        - python manage.py makemigrations
        - python manage.py sqlmigrate <app_name> <migration_number>
            (e.g., python manage.py sqlmigrate flights 0001)
        
    - Apply Migrations:
        - python manage.py migrate
        - The database to apply the migration is inside the settings.py, in DATABASES section
        - The default DB is sqlite, but it can be change to Postgres
            - In case of Postgres, rather than specifying NAME, we specify:
                - host, where the DB exists
                - port
                - username
                - password

    - Edit DB through shell using Python commands:
        - python manage.py shell

        >>> from flights.models import Flight
        >>> f = Flight(origin="New York", destination="London", duration=415)
        >>> f.save()
        >>> Flight.objects.all()
        <QuerySet [<Flight: 1: New York to London>]>
        >>> f = Flight.objects.first()
        >>> f
        <Flight: 1: New York to London>
        >>> f.origin
        'New York'
        >>> f.destination
        'London'
        >>> f.id
        1
        >>> f.delete()
        (1, {'flights.Flight': 1})

        ***After creating Flight table***
        >>> from flights.models import Airport, Flight
        >>> jfk = Airport(code="JFK", city="New York City") 
        >>> lhr = Airport(code="LHR", city="London")
        >>> jfk.save()
        >>> lhr.save()
        >>> f = Flight(origin=jfk, destination=lhr, duration=415)
        >>> f.save()
        >>> f.origin
        <Airport: New York City (JFK)>
        >>> f.origin.code
        'JFK'
        >>> jfk.departures.all()
        <QuerySet [<Flight: 1: New York City (JFK) to London (LHR)>]>


    - Create a super user account (built-in feature)
        -python manage.py createsuperuser

    - Authentication and autorization app is a built-in app in Django project

    - Admin app is built-in in Django project
        that let you manage the project database using proper credentials
        
        - modify admin.py file inside flights folder/app
            and add the models to manage in admin