from flask import Flask, request, jsonify

app = Flask(__name__) 

users = {}
user_id = 1

@app.route('/user/create', methods=['POST']) 
def create_user():
    global user_id
    data = request.json
    if 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing email or name"}), 400

    id = user_id
    user_id += 1

    users[id] = {
        'name': data['name'],
        'email': data['email'],
        'salary': data.get('salary', None),
        'designation': data.get('designation', None)
    }

    return jsonify({"message": "User creation successful", "user_id": id}), 201  

@app.route('/user/search', methods=['GET'])
def search_users():
    search_query = request.args
    found_users = {uid: user for uid, user in users.items()
                   if all(user.get(key) == str(value) for key, value in search_query.items())}

    if found_users:
        return jsonify(found_users)
    else:
        return jsonify({"message": "No users found matching the criteria"}), 404

if __name__ == '__main__':
    app.run(debug=True)
