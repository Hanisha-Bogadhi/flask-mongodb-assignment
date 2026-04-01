from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client.test

collection = db["flask_tutorials"]

app = Flask(__name__) 

@app.route('/signup', methods=['POST'])
def signup():
    try:
        signup_data = request.get_json()
        collection.insert_one(signup_data)
        return redirect('/success')
    except Exception as e:
        return render_template('index.html', error=str(e))

@app.route('/success')
def success():
     return render_template('success.html')

@app.route('/api')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        del item['_id']
    data ={
        'data': data
    }

    return jsonify(data)

if __name__ == '__main__': #calling function

    app.run(host='0.0.0.0', port=5000, debug=True)