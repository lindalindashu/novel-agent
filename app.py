from flask import Flask, render_template, request, jsonify
from llm_service import LLMService

app = Flask(__name__)
llm = LLMService()


@app.route("/")
def index():
    """Serve the main page."""
    return render_template("index.html")


@app.route("/api/diary", methods=["POST"])
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


@app.route("/api/entities", methods=["POST"])
def extract_entities():
    """API endpoint to extract entities from text."""
    try:
        data = request.json
        text = data.get("input", "").strip()
        
        if not text:
            return jsonify({"error": "No input provided"}), 400
        
        result = llm.extract_entities(text)
        return jsonify({"success": True, "entities": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
