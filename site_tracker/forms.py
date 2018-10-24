from flask.ext.wtf import Form
from wtforms import fields
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .models import Site


class SiteForm(Form):
    base_url = fields.StringField()


class VisitForm(Form):
    browser = fields.StringField()
    date = fields.DateField()
    event = fields.StringField()
    url = fields.StringField()
    ip_address = fields.StringField("IP Address")
    site = QuerySelectField(query_factory=lambda: Site.query.all())
    """
    Using lambda here, because db is not bound to an application (in models.py),
    which would throw error to access Site.query when VisitForm is being constructed 
    Creating a function that will call Site.query only when VisitForm is instantiated
    (e. g. in our views we call form = VisitForm()) ensures that we will only access Site.query 
    when we will have access to a Flask application instance.
    """
