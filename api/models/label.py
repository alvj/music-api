from api.models import db, ma
from sqlalchemy.dialects.mysql import INTEGER

class LabelModel(db.Model):
    __tablename__ = "labels"
    label_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    label_name = db.Column(db.String(255), nullable=False)

class LabelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LabelModel
        load_instance = True
