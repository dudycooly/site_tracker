Site Visit Tracking App
==============
This application tracks visits to a particular web site register with this application.

In this, 2 tables (tracking_site, tracking_visit) are used to track visits to sites reigstered with this app


Packages Used
==============
* Flask
* WTF forms
* SQLAlchemy

Concetps Explored
==============
* REST API
* Web Application (Unauthenticated Session)
  * Using Flask Forms and Jinja templates
  * Design Patterns: 
     MVC
     DAO
     Mixins (CRUDMixmin, Flask UserMixin)
* User Session Management
* Salted/Hased password using backports.pbkdf2 HMAC
* password property

* Database Management
  * SQLite DB with SQLAlchemy as ORM
  * Linking two tables (back referencing) via Foriegn Keys
  * hybrid_property

Updates to this branch
==============
As part of previous branch, the content of single monolithic file is refactored  in to appropriate modules/director as recommened by Flask

In this branch, User Accounts are setup to introduce authendticted session via an additional package - Users
