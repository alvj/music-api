from flask import Flask, jsonify, request
app = Flask(__name__)

artists = [
]

@app.route('/artists')
def get_artists():
    return jsonify(artists)

@app.route('/artists', methods=['POST'])
def add_artist():
    artists.append(request.get_json())
    return '', 204