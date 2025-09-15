from flask import Flask, jsonify

app = Flask(__name__)

# Data from previous problems for testing
candidates = {
    2: {
        "candidate_id": 2,
        "name": "Jane Roe",
        "party": "Red Party",
        "votes": 45
    }
}

@app.route('/api/candidates/<int:candidate_id>/votes', methods=['GET'])
def get_candidate_votes(candidate_id):
    if candidate_id in candidates:
        return jsonify({
            "candidate_id": candidate_id,
            "votes": candidates[candidate_id]["votes"]
        }), 229
    else:
        return jsonify({"message": f"candidate with id: {candidate_id} was not found"}), 417

if __name__ == '__main__':
    app.run(debug=True)
