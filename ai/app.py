from flask import Flask, request, jsonify
from flask_cors import CORS
from groq_client import get_llm_answer

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json(force=True)
        title = data.get("title", "")
        desc = data.get("description", "")
        reviews = data.get("reviews", [])
        question = data.get("question", "")
        if not question:
            return jsonify({"answer": "Please ask a question."})
        answer = get_llm_answer(title, desc, reviews, question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Server error: {e}"}), 500

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.get_json(force=True)
        reviews = data.get("reviews", [])
        if not reviews: return jsonify({"summary": "No reviews found."})
        question = "Summarize the main points of these reviews in a few sentences."
        answer = get_llm_answer("", "", reviews, question)
        return jsonify({"summary": answer})
    except Exception as e:
        return jsonify({"summary": f"Error: {e}"}), 500

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(force=True)
        reviews = data.get("reviews", [])
        if not reviews: return jsonify({"analysis": "No reviews found."})
        question = "Analyze these reviews: highlight strengths, weaknesses, and customer sentiment."
        answer = get_llm_answer("", "", reviews, question)
        return jsonify({"analysis": answer})
    except Exception as e:
        return jsonify({"analysis": f"Error: {e}"}), 500

@app.route("/proscons", methods=["POST"])
def proscons():
    try:
        data = request.get_json(force=True)
        reviews = data.get("reviews", [])
        if not reviews: return jsonify({"proscons": "No reviews found."})
        question = "List clear Pros and Cons from these reviews in bullet points."
        answer = get_llm_answer("", "", reviews, question)
        return jsonify({"proscons": answer})
    except Exception as e:
        return jsonify({"proscons": f"Error: {e}"}), 500

@app.route("/compare", methods=["POST"])
def compare():
    try:
        data = request.get_json(force=True)
        product1 = data.get("product1", "")
        product2 = data.get("product2", "")
        if not product1 or not product2:
            return jsonify({"comparison": "Please provide two product names."})
        question = f"Compare these two products:\n1. {product1}\n2. {product2}\nHighlight differences and advantages."
        answer = get_llm_answer("", "", [], question)
        return jsonify({"comparison": answer})
    except Exception as e:
        return jsonify({"comparison": f"Error: {e}"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
