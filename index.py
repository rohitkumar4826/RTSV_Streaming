from flask import Flask, render_template, request, jsonify
from flask_pymongo import pymongo
from bson import json_util, ObjectId
import json
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='./frontend/build', template_folder='./frontend/build')

# MongoDB connection
CONNECTION_STRING = os.getenv("MONGODB_URI")
db = pymongo.MongoClient(CONNECTION_STRING, connect=False).get_database('rtsp')
user_collection = db['overlays']

# Serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Create a new overlay
@app.route('/overlays', methods=["POST"])
def create_overlay():
    data = request.json
    user_collection.insert_one(data)
    return jsonify({'message': "Overlay created successfully!"})

# Get all overlays
@app.route('/overlays', methods=["GET"])
def get_overlays():
    overlays = json.loads(json_util.dumps(user_collection.find({})))
    return jsonify({'overlays': overlays})

# Update an existing overlay
@app.route('/overlays/<id>', methods=["PUT"])
def update_overlay(id):
    data = request.json
    user_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': "Overlay updated successfully!"})

# Delete an overlay
@app.route('/overlays/<id>', methods=["DELETE"])
def delete_overlay(id):
    user_collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': "Overlay deleted successfully!"})

# Run the server using Waitress
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
