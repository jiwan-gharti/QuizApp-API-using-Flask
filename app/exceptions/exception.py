from app import create_app
from flask import jsonify

app = create_app()


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Resource not found"}), 404

@app.errorhandler(500)
def internal_server(error):
    return jsonify({"message":"There is a problem"}), 500
