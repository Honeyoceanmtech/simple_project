from flask_cors import CORS
from flask import Flask , request,jsonify
from pymongo import MongoClient

app=Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello():
    values = "Hello world"
    return jsonify(values)



if __name__=="__main__":
    app.run(debug=True)
