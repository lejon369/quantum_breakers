from flask import Flask, jsonify

app = Flask(__name__)

# Data from previous problems for testing
candidates = {
    1: {
        "candidate_id": 1,
        "name": "John Doe",
        "party": "Green Party",
        "votes": 30
    },
    2: {
        "candidate_id": 2,
        "name": "Jane Roe",
        "party": "Red Party",
        "votes": 45
    }
}

@app.route('/api/results', methods=['GET'])
def get_voting_results():
    sorted_candidates = sorted(candidates.values(), key=lambda c: c['votes'], reverse=True)
    return jsonify({"results": sorted_candidates}), 231

if __name__ == '__main__':
    app.run(debug=True)
