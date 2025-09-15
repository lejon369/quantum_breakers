from flask import Flask, request, jsonify

app = Flask(__name__)

voters = {}

@app.route('/api/voters', methods=['POST'])
def create_voter():
    data = request.get_json()
    voter_id = data.get('voter_id')
    name = data.get('name')
    age = data.get('age')

    if not all([voter_id, name, age]):
        return jsonify({"message": "Missing required fields"}), 400

    if voter_id in voters:
        return jsonify({"message": f"voter with id: {voter_id} already exists"}), 409

    if age < 18:
        return jsonify({"message": f"invalid age: {age}, must be 18 or older"}), 422

    voters[voter_id] = {
        "voter_id": voter_id,
        "name": name,
        "age": age,
        "has_voted": False
    }

    return jsonify(voters[voter_id]), 218

if __name__ == '__main__':
    app.run(debug=True)
