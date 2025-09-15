from flask import Flask, jsonify

app = Flask(__name__)

# Data from problem 1 for testing
voters = {
    1: {
        "voter_id": 1,
        "name": "Alice",
        "age": 22,
        "has_voted": False
    }
}

@app.route('/api/voters/<int:voter_id>', methods=['GET'])
def get_voter_info(voter_id):
    voter = voters.get(voter_id)
    if voter:
        return jsonify(voter), 222
    else:
        return jsonify({"message": f"voter with id: {voter_id} was not found"}), 417

if __name__ == '__main__':
    app.run(debug=True)
