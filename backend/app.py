from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json
from dotenv import load_dotenv
import os


load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client["testdb"]
collection = db["users"]
app = Flask(__name__)


# API: Read from file
@app.route('/api', methods=['GET'])
def get_data():
    with open('data.json') as file:
        data = json.load(file)
    return jsonify(data)

# API: Insert into MongoDB
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        print("Received Data:", data)   
        result = collection.insert_one(data)
        print("Inserted ID:", result.inserted_id)  
        print("DB NAME:", db.name)
        print("TOTAL DOCUMENTS:", collection.count_documents({}))


        return jsonify({"message": "Success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)