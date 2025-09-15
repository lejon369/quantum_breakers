from flask import Flask, request, jsonify

app = Flask(__name__)

# Data from previous problems for testing
voters = {
    1: {
        "voter_id": 1,
        "name": "Alice",
        "age": 22,
        "has_voted": False
    }
}

@app.route('/api/voters/<int:voter_id>', methods=['PUT'])
def update_voter_info(voter_id):
    if voter_id not in voters:
        return jsonify({"message": f"voter with id: {voter_id} was not found"}), 417

    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    if age is not None and age < 18:
        return jsonify({"message": f"invalid age: {age}, must be 18 or older"}), 422

    if name:
        voters[voter_id]['name'] = name
    if age:
        voters[voter_id]['age'] = age

    return jsonify(voters[voter_id]), 224

if __name__ == '__main__':
    app.run(debug=True)
