from flask import Blueprint, request, jsonify
from app.database import mongo

api = Blueprint("api", __name__)

@api.route("/")
def home():
    return jsonify({"message": "Welcome to Flask with MongoDB"})

@api.route("/add", methods=["POST"])
def add_data():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    record_id = mongo.db.records.insert_one(data).inserted_id
    return jsonify({"message": "Data added", "id": str(record_id)})

@api.route("/records", methods=["GET"])
def get_records():
    records = mongo.db.records.find()
    result = [{"id": str(record["_id"]), "name": record["name"]} for record in records]
    return jsonify(result)
