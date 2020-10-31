# EduAccess
*SDL Project*

## How to install
```
1. git clone https://github.com/pavankumarvm/EduAccess.git
2. create virtual environment using virtualenv
    Commands are as follows:
    - pip install virtualenv
    - venv\Scripts\activate
3. Check in command line if virtualenv is activated or not.
    If activated it will be as follows:
    - (venv) A:EduAccess>
3. Now install required packages (pip install -r requirements.txt)
```

## How to run project
```
1. Be sure you have completed above installation steps.
2. Now first migrte all models.
    - python manage.py makemigrations
    - python manage.py migrate
3. Now collect a static files.
    - python manage.py collectstatic
4. Now you can run project using command:
    - python managee.py runserver
```

## Contribute to Repository
```
1. Fork this repository
2. create a branch for your changes
3. configure an upstream to this repository
4. create a pull request
