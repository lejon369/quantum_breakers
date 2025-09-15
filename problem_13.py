from flask import Flask, request, jsonify

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
        "timestamp": "2025-09-10T10:32:00Z"
    }
]

@app.route('/api/votes/timeline', methods=['GET'])
def get_vote_timeline():
    candidate_id_str = request.args.get('candidate_id')
    if not candidate_id_str:
        return jsonify({"message": "Missing candidate_id parameter"}), 400

    try:
        candidate_id = int(candidate_id_str)
    except ValueError:
        return jsonify({"message": "Invalid candidate_id parameter"}), 400

    timeline = [
        {"vote_id": vote["vote_id"], "timestamp": vote["timestamp"]}
        for vote in votes if vote["candidate_id"] == candidate_id
    ]

    return jsonify({
        "candidate_id": candidate_id,
        "timeline": timeline
    }), 233

if __name__ == '__main__':
    app.run(debug=True)
