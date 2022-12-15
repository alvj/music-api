from api.models import db, ma
from sqlalchemy.dialects.mysql import INTEGER

class ArtistModel(db.Model):
    __tablename__ = "artists"
    artist_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(255), nullable=False)
    artist_description = db.Column(db.String(2000))
    artist_image = db.Column(db.String(2000))

class ArtistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ArtistModel
        load_instance = True
