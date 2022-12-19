from flask import Flask, jsonify, request
from marshmallow.exceptions import ValidationError
from api.models import db, ma
from api.models.artist import ArtistModel, ArtistSchema
from api.models.label import LabelModel, LabelSchema
from api.models.playlist import PlaylistModel, PlaylistSchema
from api.models.album import AlbumModel, AlbumSchema
from api.models.song import SongModel, SongSchema

from api.models.user import UserModel, UserSchema
from api.models.role import RoleModel, RoleSchema


app = Flask(__name__)
# Load db connection string
app.config.from_pyfile("../config.cfg")

db.init_app(app)
ma.init_app(app)

@app.route('/health')
def health_check():
    return 'OK', 200

# ARTISTS #
@app.route('/artists')
def get_artists():
    if authenticate(request) not in (1, 2, 3):
        return '', 401
    all_artists = ArtistModel.query.all()
    return jsonify(ArtistSchema(many=True).dump(all_artists))

@app.route('/artists', methods=['POST'])
def create_artist():
    if authenticate(request) not in (2, 3):
        return '', 401
    try:
        artist = ArtistSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(artist)
    db.session.commit()
    return ArtistSchema().jsonify(artist), 201

@app.route('/artists/<int:artist_id>', methods=['PATCH'])
def modify_artist(artist_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    # Load schema partially so the existing data is not overwritten undesirably
    artist = ArtistSchema().load(
        request.json,
        instance=ArtistModel.query.get(artist_id),
        partial=True)

    if artist.artist_id is None:
        return '', 404

    db.session.commit()
    return ArtistSchema().jsonify(artist), 200

@app.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    artist = ArtistModel.query.get(artist_id)
    if artist is None:
        return '', 404

    db.session.delete(artist)
    db.session.commit()
    return ArtistSchema().jsonify(artist), 200

# LABELS #
@app.route('/labels')
def get_labels():
    if authenticate(request) not in (1, 2, 3):
        return '', 401
    all_labels = LabelModel.query.all()
    return jsonify(LabelSchema(many=True).dump(all_labels))

@app.route('/labels', methods=['POST'])
def create_label():
    if authenticate(request) not in (2, 3):
        return '', 401
    try:
        label = LabelSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(label)
    db.session.commit()
    return LabelSchema().jsonify(label), 201

@app.route('/labels/<int:label_id>', methods=['PATCH'])
def modify_label(label_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    # Load schema partially so the existing data is not overwritten undesirably
    label = LabelSchema().load(
        request.json,
        instance=LabelModel.query.get(label_id),
        partial=True)

    if label.label_id is None:
        return '', 404

    db.session.commit()
    return LabelSchema().jsonify(label), 200

@app.route('/labels/<int:label_id>', methods=['DELETE'])
def delete_label(label_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    label = LabelModel.query.get(label_id)
    if label is None:
        return '', 404

    db.session.delete(label)
    db.session.commit()
    return LabelSchema().jsonify(label), 200

# PLAYLISTS #
@app.route('/playlists')
def get_playlists():
    if authenticate(request) not in (1, 2, 3):
        return '', 401
    all_playlists = PlaylistModel.query.all()
    return jsonify(PlaylistSchema(many=True).dump(all_playlists))

@app.route('/playlists', methods=['POST'])
def create_playlist():
    if authenticate(request) not in (2, 3):
        return '', 401
    try:
        playlist = PlaylistSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(playlist)
    db.session.commit()
    return PlaylistSchema().jsonify(playlist), 201

@app.route('/playlists/<int:playlist_id>', methods=['PATCH'])
def modify_playlist(playlist_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    # Load schema partially so the existing data is not overwritten undesirably
    playlist = PlaylistSchema().load(
        request.json,
        instance=PlaylistModel.query.get(playlist_id),
        partial=True)

    if playlist.playlist_id is None:
        return '', 404

    db.session.commit()
    return PlaylistSchema().jsonify(playlist), 200

@app.route('/playlists/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    playlist = PlaylistModel.query.get(playlist_id)
    if playlist is None:
        return '', 404

    db.session.delete(playlist)
    db.session.commit()
    return PlaylistSchema().jsonify(playlist), 200

# ALBUMS #
@app.route('/albums')
def get_albums():
    if authenticate(request) not in (1, 2, 3):
        return '', 401
    all_albums = AlbumModel.query.all()
    return jsonify(AlbumSchema(many=True).dump(all_albums))

@app.route('/albums', methods=['POST'])
def create_album():
    if authenticate(request) not in (2, 3):
        return '', 401
    try:
        album = AlbumSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(album)
    db.session.commit()
    return AlbumSchema().jsonify(album), 201

@app.route('/albums/<int:album_id>', methods=['PATCH'])
def modify_album(album_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    # Load schema partially so the existing data is not overwritten undesirably
    album = AlbumSchema().load(
        request.json,
        instance=AlbumModel.query.get(album_id),
        partial=True)

    if album.album_id is None:
        return '', 404

    db.session.commit()
    return AlbumSchema().jsonify(album), 200

@app.route('/albums/<int:album_id>', methods=['DELETE'])
def delete_album(album_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    album = AlbumModel.query.get(album_id)
    if album is None:
        return '', 404

    db.session.delete(album)
    db.session.commit()
    return AlbumSchema().jsonify(album), 200

# SONGS #
@app.route('/songs')
def get_songs():
    if authenticate(request) not in (1, 2, 3):
        return '', 401
    all_songs = SongModel.query.all()
    return jsonify(SongSchema(many=True).dump(all_songs))

@app.route('/songs', methods=['POST'])
def create_song():
    if authenticate(request) not in (2, 3):
        return '', 401
    try:
        song = SongSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(song)
    db.session.commit()
    return SongSchema().jsonify(song), 201

@app.route('/songs/<int:song_id>', methods=['PATCH'])
def modify_song(song_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    # Load schema partially so the existing data is not overwritten undesirably
    song = SongSchema().load(
        request.json,
        instance=SongModel.query.get(song_id),
        partial=True)

    if song.song_id is None:
        return '', 404

    db.session.commit()
    return SongSchema().jsonify(song), 200

@app.route('/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    if authenticate(request) not in (2, 3):
        return '', 401
    song = SongModel.query.get(song_id)
    if song is None:
        return '', 404

    db.session.delete(song)
    db.session.commit()
    return SongSchema().jsonify(song), 200

# TABLES #
@app.route('/tables', methods=['POST'])
def create_table():
    if authenticate(request) not in (3):
        return '', 401
    db.session.execute(request.get_data(as_text=True))

    return '', 204

@app.route('/tables/<table_name>', methods=['DELETE'])
def delete_table(table_name):
    if authenticate(request) not in (3):
        return '', 401
    try:
        db.session.execute(f"DROP TABLE {table_name}")
        return '', 204
    except:
        return "There was an error", 400

# USERS #
@app.route('/users', methods=['POST'])
def create_user():
    if authenticate(request) not in (3):
        return '', 401
    try:
        user = UserSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(user)
    db.session.commit()
    return UserSchema().jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def modify_user(user_id):
    if authenticate(request) not in (3):
        return '', 401
    # Load schema partially so the existing data is not overwritten undesirably
    user = UserSchema().load(
        request.json,
        instance=UserModel.query.get(user_id),
        partial=True)

    if user.user_id is None:
        return '', 404

    db.session.commit()
    return UserSchema().jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if authenticate(request) not in (3):
        return '', 401
    user = UserModel.query.get(user_id)
    if user is None:
        return '', 404

    db.session.delete(user)
    db.session.commit()
    return UserSchema().jsonify(user), 200

# ROLES #
@app.route('/roles', methods=['POST'])
def create_role():
    if authenticate(request) not in (3):
        return '', 401
    try:
        role = RoleSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(role)
    db.session.commit()
    return RoleSchema().jsonify(role), 201

@app.route('/roles/<int:role_id>', methods=['PATCH'])
def modify_role(role_id):
    if authenticate(request) not in (3):
        return '', 401
    # Load schema partially so the existing data is not overwritten undesirably
    role = RoleSchema().load(
        request.json,
        instance=RoleModel.query.get(role_id),
        partial=True)

    if role.role_id is None:
        return '', 404

    db.session.commit()
    return RoleSchema().jsonify(role), 200

@app.route('/roles/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    if authenticate(request) not in (3):
            return '', 401
    role = RoleModel.query.get(role_id)
    if role is None:
        return '', 404

    db.session.delete(role)
    db.session.commit()
    return RoleSchema().jsonify(role), 200


def authenticate(request):
    try:
        user = db.session.execute(db.select(UserModel).
            filter_by(
                user_name=request.authorization["username"], 
                user_password=request.authorization["password"])).one()

        role = db.session.execute(db.select(RoleModel).
            filter_by(
                role_id=user[0].role_id)).one()

        return(role[0].role_permission_level)
    except:
        return 0