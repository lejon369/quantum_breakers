from flask import Flask, request, jsonify

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
def filter_candidates_by_party():
    party_name = request.args.get('party')
    if not party_name:
        return jsonify({"message": "Missing party parameter"}), 400

    filtered_candidates = [
        candidate for candidate in candidates.values() 
        if candidate['party'] == party_name
    ]

    return jsonify({"candidates": filtered_candidates}), 230

if __name__ == '__main__':
    app.run(debug=True)
