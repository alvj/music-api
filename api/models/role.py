from api.models import db, ma
from sqlalchemy.dialects.mysql import INTEGER

class RoleModel(db.Model):
    __tablename__ = "roles"
    role_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(255), nullable=False)
    role_permission_level = db.Column(INTEGER(unsigned=True), nullable=False)

class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel
        load_instance = True
