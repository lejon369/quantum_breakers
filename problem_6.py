from flask import Flask, request, jsonify

app = Flask(__name__)

candidates = {}

@app.route('/api/candidates', methods=['POST'])
def register_candidate():
    data = request.get_json()
    candidate_id = data.get('candidate_id')
    name = data.get('name')
    party = data.get('party')

    if not all([candidate_id, name, party]):
        return jsonify({"message": "Missing required fields"}), 400

    if candidate_id in candidates:
        return jsonify({"message": f"candidate with id: {candidate_id} already exists"}), 409

    candidates[candidate_id] = {
        "candidate_id": candidate_id,
        "name": name,
        "party": party,
        "votes": 0
    }

    return jsonify(candidates[candidate_id]), 226

if __name__ == '__main__':
    app.run(debug=True)
