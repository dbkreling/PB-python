# PB-python - a place for running tests in Python

PB-python is a web application created with the purpose to serve as a central place to run python-based tests locally.

## Getting Started

Clone PB-python and once you are all set, create an in-memory DataBase and then run web_app.py from your web browser.

### Prerequisites

This application uses python Flask and SQLAlchemy to manage its server and database. To install those issue:

```
pip install Flask

pip install Flask-SQLAlchemy
```

If you need pip in your system, follow the steps at https://packaging.python.org/install_requirements_linux/ to get it into your system.

### Installing

Before running the application, one must create the database on the memory. To do so, open a terminal window in your system and issue:

```
$ cd PB-python/
$ python
>>> from web_app import db
>>> db.create_all()
```

See "room_for_improvement.txt" for further insights about the database creation and model.


## Running the application

To run the application, change directory to PB-python and issue:

```
$ python web_app.py
```

Move to a web browser and access your localhost server using port 5000:

From the browser, issue:
```
http://127.0.0.1:5000/  or localhost:5000/
```

## Optional

In order to view the database, I used SQLManager Firefox addon on my browser, available at https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/
After you install it, go to Firefox's Tools > SQLite Manager. There you should:

- Connect database (either by File > Connect Database menu) or clicking on the folder icon at the top toolbar.
- Select "profitbricks.sqlite" database.


## Author

* **Daniel Kreling** - *Initial work* - [github](https://github.com/dbkreling)


## Built With

* [Flask 0.12](http://flask.pocoo.org/) - The web framework used
* [Python](https://www.python.org/) - Python 2.7.13
* [SQlite](https://www.sqlite.org/download.html) - SQlite database
