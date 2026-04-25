from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ ADD THIS

app = Flask(__name__)
CORS(app)  # ✅ ADD THIS

@app.route("/")
def home():
    return "Skill Agent Backend Running 🚀"

@app.route("/assess", methods=["POST"])
def assess():
    data = request.json

    skill = data.get("skill")
    level = data.get("level")
    goal = data.get("goal")

    if level.lower() == "beginner":
        score = 3
        roadmap = [
            "Learn basics",
            "Practice small projects",
            "Understand core concepts"
        ]
    elif level.lower() == "intermediate":
        score = 6
        roadmap = [
            "Build real projects",
            "Learn frameworks",
            "Improve problem solving"
        ]
    else:
        score = 8
        roadmap = [
            "Advanced system design",
            "Optimize code",
            "Contribute to open source"
        ]

    return jsonify({
        "skill": skill,
        "score": score,
        "goal": goal,
        "roadmap": roadmap
    })

if __name__ == "__main__":
    app.run(debug=True)