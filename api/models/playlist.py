from api.models import db, ma
from sqlalchemy.dialects.mysql import INTEGER

class PlaylistModel(db.Model):
    __tablename__ = "playlists"
    playlist_id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    playlist_name = db.Column(db.String(255), nullable=False)
    playlist_description = db.Column(db.String(2000))
    playlist_image = db.Column(db.String(2000))

class PlaylistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlaylistModel
        load_instance = True
