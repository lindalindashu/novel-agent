from flask import Blueprint, request, jsonify
from app.db import SessionLocal
from app.services.diary_service import DiaryService

bp = Blueprint('diary', __name__)


@bp.route("/api/diary", methods=["POST"])
def generate_diary():
    """API endpoint to generate diary novel with persistence."""
    db = SessionLocal()
    try:
        data = request.json
        user_input = data.get("input", "").strip()
        feedback = data.get("feedback", None)
        username = data.get("username", "default")

        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Use DiaryService with context injection
        service = DiaryService(db)
        entry = service.generate_diary_entry(
            user_input=user_input,
            username=username,
            feedback=feedback,
            context_limit=3
        )

        return jsonify({
            "success": True,
            "entry": entry.to_dict()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


@bp.route("/api/entries", methods=["GET"])
def get_entries():
    """Get all diary entries for a user."""
    db = SessionLocal()
    try:
        username = request.args.get("username", "default")
        limit = request.args.get("limit", type=int)

        service = DiaryService(db)
        entries = service.get_all_entries(username=username, limit=limit)

        return jsonify({
            "success": True,
            "entries": [entry.to_dict() for entry in entries],
            "count": len(entries)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


@bp.route("/api/entries/<int:entry_id>", methods=["GET"])
def get_entry(entry_id):
    """Get a specific diary entry."""
    db = SessionLocal()
    try:
        service = DiaryService(db)
        entry = service.get_entry(entry_id)

        if not entry:
            return jsonify({"error": "Entry not found"}), 404

        return jsonify({
            "success": True,
            "entry": entry.to_dict()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


@bp.route("/api/entries/<int:entry_id>", methods=["DELETE"])
def delete_entry(entry_id):
    """Delete a diary entry."""
    db = SessionLocal()
    try:
        service = DiaryService(db)
        success = service.delete_entry(entry_id)

        if not success:
            return jsonify({"error": "Entry not found"}), 404

        return jsonify({
            "success": True,
            "message": "Entry deleted successfully"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()
