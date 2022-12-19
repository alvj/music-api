from api.models import db, ma
from sqlalchemy.dialects.mysql import INTEGER

class UserModel(db.Model):
    __tablename__ = "users"
    user_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(INTEGER(unsigned=True), nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
