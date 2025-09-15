from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# This is a simplified implementation focusing on accepting ranked ballots.
# It does not implement the Schulze method for determining the winner.

ranked_ballots = []

@app.route('/api/ballots/ranked', methods=['POST'])
def submit_ranked_ballot():
    data = request.get_json()
    required_fields = ["election_id", "voter_id", "ranking", "timestamp"]
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Missing required fields"}), 400

    # Basic validation
    if not isinstance(data["ranking"], list) or not all(isinstance(i, int) for i in data["ranking"]):
        return jsonify({"message": "Invalid ranking format"}), 400

    ballot_id = "rb_" + hashlib.sha256(str(data).encode()).hexdigest()[:4]
    new_ballot = {
        "ballot_id": ballot_id,
        "election_id": data["election_id"],
        "voter_id": data["voter_id"],
        "ranking": data["ranking"],
        "timestamp": data["timestamp"]
    }
    ranked_ballots.append(new_ballot)

    return jsonify({
        "ballot_id": ballot_id,
        "status": "accepted"
    }), 239

if __name__ == '__main__':
    app.run(debug=True)
