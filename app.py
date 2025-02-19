from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.secret_key = "narendra12++&&"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Flask_data"
mongo = PyMongo(app)
    
@app.route('/users', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        id = mongo.db['users'].insert_one({'name': _name, 'email': _email, 'password': _hashed_password})
        resp = jsonify("user added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()
    
@app.route('/users', methods=['GET'])
def users():
    users = mongo.db['users'].find()
    resp = dumps(users)
    return resp

@app.route('/users/<id>', methods=['GET'])
def get_users(id):
    user = mongo.db['users'].find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db['users'].delete_one({'_id': ObjectId(id)})
    resp = jsonify("user deleted.")
    resp.status_code = 200
    return resp

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    
    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)
        
        mongo.db['users'].update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'email': _email, 'password': _hashed_password}})
        
        resp = jsonify("user updated successfully.")
        resp.status_code = 200
        return resp
    else:
        return not_found()
    
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'not found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp

if __name__ == "__main__":
    app.run(debug=True) 
    