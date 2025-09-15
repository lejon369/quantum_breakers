from flask import Flask, jsonify

app = Flask(__name__)

# Data from previous problems for testing
candidates = {
    1: {
        "candidate_id": 1,
        "name": "John Doe",
        "party": "Green Party",
        "votes": 0
    },
    2: {
        "candidate_id": 2,
        "name": "Jane Roe",
        "party": "Red Party",
        "votes": 0
    }
}

@app.route('/api/candidates', methods=['GET'])
def list_candidates():
    return jsonify({"candidates": list(candidates.values())}), 227

if __name__ == '__main__':
    app.run(debug=True)
