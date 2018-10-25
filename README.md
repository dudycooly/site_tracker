Site Visit Tracking App
==============
This application tracks visits to a particular web site register with this application.

In this, 3 tables (tracking_site, tracking_visit, users) are used to track visits to sites reigstered with this app


Packages Used
==============
* Flask
* WTF forms
* SQLAlchemy

Concetps Explored
==============
* REST API
* Web Application (Unauthenticated Session)
  * Flask
    * request (POST/GET, process body/header)
    * jsonify
  * Flask Forms 
     * validators
     * hidden_tags
  * Jinja templates
  * Design Patterns: 
     * Blueprint
     * MVC
     * DAO
     * Mixins (CRUDMixmin, Flask UserMixin)
* User Session Management
  * Login Manager (login_required decorator with LoginMixIn, anonymous user)
  * Salted/Hased password using backports.pbkdf2 HMAC
  * password property decorator
  * member restricted API 

* Database Management
  * SQLite DB with SQLAlchemy as ORM
  * Linking two tables (back referencing) via Foriegn Keys
  * hybrid_property

* Py2 to Py3 migration issues
  * Py2 cookies may throw [JSON serializable error](https://stackoverflow.com/questions/44605393/object-of-type-bytes-is-not-json-serializable-when-upgrading-my-python-environ), hence clear browser cookies
  * Be specific about Endianness
    * Py2: self._salt = bytes(SystemRandom().getrandbits(128))
    * Py3: self._salt = SystemRandom().getrandbits(128).to_bytes(16, 'little')
  * csrf_token is not valid argument for SQLAlchamey model (Failed to solve this)
  * By manually taking out csrf_tokem, ended up with sqlalchemy.exc.OperationalError (failed to solved this)
 
  
Updates to this branch
==============
As part of previous branch, the content of single monolithic file is refactored  in to appropriate modules/director as recommened by Flask

In this branch, User Accounts are setup to introduce authendticted session via an additional package - Users

Associate Sites to Users by backreferencing them
Move DB related tasks out of views (to dao )
