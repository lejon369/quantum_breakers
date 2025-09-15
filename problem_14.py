from flask import Flask, request, jsonify

app = Flask(__name__)

# Data from previous problems for testing
voters = {
    1: {
        "voter_id": 1,
        "name": "Alice",
        "age": 22,
        "has_voted": False,
        "profile_updated": True  # Assume profile was updated
    }
}

candidates = {
    2: {
        "candidate_id": 2,
        "name": "Jane Roe",
        "party": "Red Party",
        "votes": 0
    }
}

votes = []
vote_id_counter = 200

@app.route('/api/votes/weighted', methods=['POST'])
def cast_weighted_vote():
    global vote_id_counter
    data = request.get_json()
    voter_id = data.get('voter_id')
    candidate_id = data.get('candidate_id')

    if not all([voter_id, candidate_id]):
        return jsonify({"message": "Missing required fields"}), 400

    if voter_id not in voters:
        return jsonify({"message": f"voter with id: {voter_id} was not found"}), 417

    if candidate_id not in candidates:
        return jsonify({"message": f"candidate with id: {candidate_id} was not found"}), 417

    if voters[voter_id]["has_voted"]:
        return jsonify({"message": f"voter with id: {voter_id} has already voted"}), 423

    weight = 2 if voters[voter_id].get("profile_updated") else 1

    voters[voter_id]["has_voted"] = True
    candidates[candidate_id]["votes"] += weight
    vote_id_counter += 1

    new_vote = {
        "vote_id": vote_id_counter,
        "voter_id": voter_id,
        "candidate_id": candidate_id,
        "weight": weight
    }
    votes.append(new_vote)

    return jsonify(new_vote), 234

if __name__ == '__main__':
    app.run(debug=True)
