# microblog_flask
Flask based project

Run Flask app: 
- `flask --app microblog run`

Run Flask app: 
- `flask run`


## Working with DB:

`pip install flask-sqlalchemy`
`pip install flask-migrate`


## Flask-WFT

`pip install flask-wtf`

## DB commnds:

`flask db init`
`flask db migrate -m "users table"`
`flask db migrate -m "posts table"`

### do updates of DB

`flask db upgrade`
`flask db downgrade` команда, которая отменяет последнюю миграцию

### очистка базы данных:
(venv) $ flask db downgrade base
(venv) $ flask db upgrade

## Extra info
- [Miguel's blog](https://blog.miguelgrinberg.com/)
- [Ru Translation](https://habr.com/ru/articles/804245/)

## Loggining

` pip install flask-login`

## Email valication

`pip install email-validator`

`flask db migrate -m "new fields in user model"`

## Влкючить режим отладки Flask
`export FLASK_DEBUG=1`