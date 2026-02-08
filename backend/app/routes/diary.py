from flask import Blueprint, request, jsonify
from app.services.llm_service import LLMService

bp = Blueprint('diary', __name__)
llm = LLMService()


@bp.route("/api/diary", methods=["POST"])
def generate_diary():
    """API endpoint to generate diary novel."""
    try:
        data = request.json
        user_input = data.get("input", "").strip()
        feedback = data.get("feedback", None)

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        result = llm.generate_diary_novel(user_input, feedback=feedback)
        return jsonify({"success": True, "diary": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
