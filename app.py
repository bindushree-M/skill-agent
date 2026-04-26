from flask import Flask, request, jsonify
from flask_cors import CORS

# 1) Create app FIRST
app = Flask(__name__)
CORS(app)

# 2) Test route
@app.route("/")
def home():
    return "Skill Agent Backend Running 🚀"

# 3) Main API
@app.route("/assess", methods=["POST"])
def assess():
    data = request.json or {}

    # Get inputs
    skill = data.get("skill", "").lower().strip()
    level = data.get("level", "").lower().strip()
    goal  = data.get("goal", "").lower().strip()   # ✅ define here

    # --- Skill validation ---
    valid_skills = ["java", "python", "c++", "javascript"]
    if skill not in valid_skills:
        return jsonify({
            "error": "Invalid skill. Use Java, Python, C++, or JavaScript."
        })

    # --- Level normalization (handles typos) ---
    if level in ["beginner", "begginer"]:
        level = "beginner"
    elif level in ["intermediate", "intermidate", "intermediat"]:
        level = "intermediate"
    elif level in ["advanced", "adv"]:
        level = "advanced"
    else:
        return jsonify({
            "error": "Invalid level. Use Beginner, Intermediate or Advanced."
        })

    # --- Goal-based roadmap (Frontend vs Backend) ---
    if "front" in goal:
        if level == "beginner":
            score = 3
            roadmap = [
                "Learn HTML, CSS, JavaScript",
                "Build simple web pages",
                "Understand responsive design"
            ]
        elif level == "intermediate":
            score = 6
            roadmap = [
                "Learn React or Angular",
                "Build interactive UI projects",
                "Work with APIs"
            ]
        else:
            score = 8
            roadmap = [
                "Advanced frontend architecture",
                "Optimize performance",
                "Build scalable UI systems"
            ]

    elif "back" in goal:
        if level == "beginner":
            score = 3
            roadmap = [
                "Learn backend basics (Python/Java)",
                "Understand APIs",
                "Build simple server apps"
            ]
        elif level == "intermediate":
            score = 6
            roadmap = [
                "Learn frameworks (Flask/Spring)",
                "Work with databases",
                "Build REST APIs"
            ]
        else:
            score = 8
            roadmap = [
                "System design",
                "Database optimization",
                "Scalable backend architecture"
            ]

    else:
        score = 5
        roadmap = [
            "Clarify your goal (frontend/backend)",
            "Choose a stack",
            "Start structured learning"
        ]

    # --- Response ---
    return jsonify({
        "skill": skill,
        "score": score,
        "goal": goal,
        "roadmap": roadmap
    })

# 4) Run app LAST
if __name__ == "__main__":
    app.run(debug=True)