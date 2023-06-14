from flask import Flask, jsonify
from parser.booru import SafeBooru  # Replace 'your_parser_file' with the actual filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/images/<tags>/<int:limit>')
def get_images(tags, limit):
    try:
        booru = SafeBooru(tags, limit)
        links = booru.parse()

        return jsonify({'images': links})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()

