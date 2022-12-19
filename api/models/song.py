from api.models import db, ma
from sqlalchemy.dialects.mysql import INTEGER

class SongModel(db.Model):
    __tablename__ = "songs"
    song_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    song_name = db.Column(db.String(255), nullable=False)
    song_duration = db.Column(INTEGER(unsigned=True), nullable=False)
    album_id = db.Column(INTEGER(unsigned=True), nullable=False)

class SongSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SongModel
        load_instance = True
