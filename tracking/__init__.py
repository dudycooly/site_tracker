from flask import Flask

from .models import db
from .views import tracking

app = Flask(__name__)
app.config.from_object('config')


@app.context_processor
def provide_constants():
    return {"constants": {"RIGHTS": "2018 Calvin's Dad"}}

db.init_app(app)

app.register_blueprint(tracking)