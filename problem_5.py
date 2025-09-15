from flask import Flask, jsonify

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

@app.route('/api/voters/<int:voter_id>', methods=['DELETE'])
def delete_voter(voter_id):
    if voter_id in voters:
        del voters[voter_id]
        return jsonify({"message": f"voter with id: {voter_id} deleted successfully"}), 225
    else:
        return jsonify({"message": f"voter with id: {voter_id} was not found"}), 417

if __name__ == '__main__':
    app.run(debug=True)
