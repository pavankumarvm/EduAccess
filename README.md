# EduAccess

_SDL Project_

Website link: _https://eduaccess.herokuapp.com/_

## How to install

1. git clone https://github.com/pavankumarvm/EduAccess.git
2. Change to EduAccess directory
   ```bash
   cd EduAccess
   ```
3. create virtual environment using virtualenv
   Commands are as follows:
   ```bash
   pip install virtualenv
   virtualenv venv
   venv\Scripts\activate
   ```
4. Check in command line if virtualenv is activated or not.
   If activated it will be as follows:
   ```bash
   (venv) A:EduAccess>
   ```
5. Now install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to run project

1. Be sure you have completed above installation steps.
2. Now first connect the project to database.
   - Open eduaccess>settings.py>
   - In this file you have to edit local MySql server login configuration(username and password).
   - After this create database _eduaccess_ on your localhost
   ```bash
   create database eduaccess;
   use eduaccess;
   ```
3. Now first migrate all models.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Now collect a static files.
   ```bash
   python manage.py collectstatic
   ```
5. Now you can run project using command:
   ```bash
   python manage.py runserver
   ```

## Contribute to Repository

```
1. Fork this repository
2. create a branch for your changes
3. configure an upstream to this repository
4. create a pull request
```
