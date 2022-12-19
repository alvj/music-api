from api.models import db, ma
from sqlalchemy.dialects.mysql import INTEGER

class AlbumModel(db.Model):
    __tablename__ = "albums"
    album_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    album_name = db.Column(db.String(255), nullable=False)
    album_description = db.Column(db.String(2000))
    album_release_date = db.Column(db.Date(), nullable=False)
    album_image = db.Column(db.String(2000))
    album_type = db.Column(db.Enum("Single", "EP", "LP"), nullable=False)
    label_id = db.Column(INTEGER(unsigned=True), nullable=False)
    artist_id = db.Column(INTEGER(unsigned=True), nullable=False)

class AlbumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AlbumModel
        load_instance = True
