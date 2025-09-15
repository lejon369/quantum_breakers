from flask import Flask, jsonify

app = Flask(__name__)

# Data from previous problems for testing
voters = {
    1: {
        "voter_id": 1,
        "name": "Alice",
        "age": 22,
        "has_voted": False
    },
    2: {
        "voter_id": 2,
        "name": "Bob",
        "age": 30,
        "has_voted": False
    }
}

@app.route('/api/voters', methods=['GET'])
def list_all_voters():
    return jsonify({"voters": list(voters.values())}), 223

if __name__ == '__main__':
    app.run(debug=True)
