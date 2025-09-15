from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Data from previous problems for testing
votes = [
    {
        "vote_id": 101,
        "voter_id": 1,
        "candidate_id": 2,
        "timestamp": "2025-09-10T10:30:00Z"
    },
    {
        "vote_id": 102,
        "voter_id": 2,
        "candidate_id": 2,
        "timestamp": "2025-09-10T11:30:00Z"
    },
    {
        "vote_id": 103,
        "voter_id": 3,
        "candidate_id": 2,
        "timestamp": "2025-09-10T12:30:00Z"
    }
]

@app.route('/api/votes/range', methods=['GET'])
def get_range_vote_queries():
    candidate_id_str = request.args.get('candidate_id')
    from_time_str = request.args.get('from')
    to_time_str = request.args.get('to')

    if not all([candidate_id_str, from_time_str, to_time_str]):
        return jsonify({"message": "Missing required parameters"}), 400

    try:
        candidate_id = int(candidate_id_str)
        from_time = datetime.fromisoformat(from_time_str.replace('Z', '+00:00'))
        to_time = datetime.fromisoformat(to_time_str.replace('Z', '+00:00'))
    except (ValueError, TypeError):
        return jsonify({"message": "Invalid parameter format"}), 400

    if from_time > to_time:
        return jsonify({"message": "invalid interval: from > to"}), 424

    votes_gained = 0
    for vote in votes:
        if vote["candidate_id"] == candidate_id:
            vote_time = datetime.fromisoformat(vote["timestamp"].replace('Z', '+00:00'))
            if from_time <= vote_time <= to_time:
                votes_gained += 1

    return jsonify({
        "candidate_id": candidate_id,
        "from": from_time_str,
        "to": to_time_str,
        "votes_gained": votes_gained
    }), 235

if __name__ == '__main__':
    app.run(debug=True)
