from flask_login import AnonymousUserMixin, LoginManager

from site_tracker.users.models import User

login_manager = LoginManager()


class AnonymousUser(AnonymousUserMixin):
    id = None


login_manager.anonymous_user = AnonymousUser
login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
