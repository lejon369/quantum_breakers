from flask import Flask, jsonify

app = Flask(__name__)

# Data from previous problems for testing
candidates = {
    1: {
        "candidate_id": 1,
        "name": "John Doe",
        "party": "Green Party",
        "votes": 40
    },
    2: {
        "candidate_id": 2,
        "name": "Jane Roe",
        "party": "Red Party",
        "votes": 40
    }
}

@app.route('/api/results/winner', methods=['GET'])
def get_winning_candidate():
    if not candidates:
        return jsonify({"winners": []}), 232

    max_votes = -1
    for candidate in candidates.values():
        if candidate['votes'] > max_votes:
            max_votes = candidate['votes']

    winners = [candidate for candidate in candidates.values() if candidate['votes'] == max_votes]

    return jsonify({"winners": winners}), 232

if __name__ == '__main__':
    app.run(debug=True)
