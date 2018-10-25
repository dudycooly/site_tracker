from flask import Flask

from .auth import login_manager
from .dao import db
from .tracker.views import tracker
from .users.views import users

from flask_wtf import CsrfProtect

csrf = CsrfProtect()

app = Flask(__name__)
app.config.from_object('config')


@app.context_processor
def provide_constants():
    return {"constants": {"RIGHTS": "2018 Calvin's Dad"}}


db.init_app(app)
login_manager.init_app(app)
csrf.init_app(app)

app.register_blueprint(tracker)
app.register_blueprint(users)

