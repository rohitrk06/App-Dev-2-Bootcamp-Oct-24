from flask_security import SQLAlchemySessionUserDatastore
from applications.models import User, Role
from applications.database import db

user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)