# Flask Base
<p>
A boilerplate setup for the flask framework for using as a building block for medium size applications.
</p>

```
.
├── App
│   ├── admin
│   │   ├── templates
│   │   └── views
│   ├── api
│   ├── auth
│   │   ├── templates
│   │   └── views
│   ├── site
│   │   ├── templates
│   │   └── views
│   ├── static
│   ├── templates
│   └── __init__.py
├── Config
├── Helpers
├── migrations.py
├── Models
├── Pipfile
└── run.py
```

### installation
- install pipenv
```bash
$ sudo -H pip install -U pipenv
```
- clone the repo & cd into it
- install dependencies
```bash
$ pipenv install
```
- create the database
- Set the database credentials inside *Config/config.py* <br> <br>
    DB_HOST = 'your_db_host:port' <br>
    DB_NAME = 'your_db' <br>
    DB_USERNAME = 'db_user' <br>
    DB_PASSWORD = 'db_password' <br><br>
- Create Database tables - 
```bash
$ pipenv run python migrations.py db init
$ pipenv run python migrations.py db migrate
$ pipenv run python migrations.py db upgrade
```
- run the app
```bash
$ pipenv run python run.py
```