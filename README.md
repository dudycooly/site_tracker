Site Visit Tracking
==============
This application tracks visits to a particular web site register with this application.

Used 2 tables to track visits of a given site

* tracking_site
  * id
  * base_url
  * visits (links to `tracking_visit` to track site visits)

* tracking_visit
  * id
  * browser name
  * date visited
  * event on site during visit
  * url or endpoint of the site visited
  * ip_address of visitor
  * site_id (links back to `tracking_site`)

Used
==============

* Flask
* WTF forms
* SQLite DB with SQLAlchemy as ORM


Updates in this branch
==============

In this branch, monolithic version of the app (checkout branch monolithic) is improved by fixing dir structure as recommended by Flask

```
app-name/       # Our working root
    app-name/   # The application package (has to match working root to avoid confusing with publishing modules)
        __init__.py
    requirements.txt  # dependencies and other Meta data needed by our application resides at this level
    README.md         
```

Separting models, forms, and views modules from one single file to hold our domain models, our data translation layer, and our view code respectively to get the final form like this


```    
├── README.md
├── config.py
├── flask-tracking.db
├── requirements.txt
├── run.py
└── tracking
    ├── __init__.py # General application setup
    ├── forms.py    # User data to domain data mappers and validators
    ├── models.py   # Domain models used to define DB
    ├── templates   # Holds html Jinja templates
    └── views.py    # route/end point configuration or controlllers
```

from 

```
├── flask-tracking.db
├── requirements.txt
├── templates
│   ├── data_list.html
│   ├── helpers
│   │   ├── forms.html
│   │   └── tables.html
│   ├── index.html
│   ├── layout.html
│   └── validation_error.html
└── tracking.py
```

