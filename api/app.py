from flask import Flask, jsonify, request
from marshmallow.exceptions import ValidationError
from api.models import db, ma
from api.models.artist import ArtistModel, ArtistSchema
from api.models.label import LabelModel, LabelSchema


app = Flask(__name__)
app.config.from_pyfile("config.cfg")

db.init_app(app)
ma.init_app(app)

@app.route('/artists')
def get_artists():
    all_artists = ArtistModel.query.all()
    return jsonify(ArtistSchema(many=True).dump(all_artists))

@app.route('/artists', methods=['POST'])
def create_artist():
    try:
        artist = ArtistSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(artist)
    db.session.commit()
    return ArtistSchema().jsonify(artist), 201

@app.route('/artists/<int:artist_id>', methods=['PATCH'])
def modify_artist(artist_id):
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
    artist = ArtistModel.query.get(artist_id)
    if artist is None:
        return '', 404

    db.session.delete(artist)
    db.session.commit()
    return ArtistSchema().jsonify(artist), 200


@app.route('/labels')
def get_labels():
    all_labels = LabelModel.query.all()
    return jsonify(LabelSchema(many=True).dump(all_labels))

@app.route('/labels', methods=['POST'])
def create_label():
    try:
        label = LabelSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    db.session.add(label)
    db.session.commit()
    return LabelSchema().jsonify(label), 201

@app.route('/labels/<int:label_id>', methods=['PATCH'])
def modify_label(label_id):
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
    label = LabelModel.query.get(label_id)
    if label is None:
        return '', 404

    db.session.delete(label)
    db.session.commit()
    return LabelSchema().jsonify(label), 200
