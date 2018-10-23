Flask Tracking
==============

An example a single module (Monolithic) Flask application.  

This application tracks visit to a particular site. 
Used 2 tables to track visits of a given site

* tracking_site
** id
** base_url
** visits (links to `tracking_visit` to track site visits)

* tracking_visit
** id
** browser name
** date visited
** event on site during visit
** url or endpoint of the site visited
** ip_address of visitor
** site_id (links back to `tracking_site`)


Used
* Flask
* WTF forms
* SQLite DB with SQLAlchemy as ORM
