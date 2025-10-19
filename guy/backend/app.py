from flask import Flask, request, jsonify
from flask_cors import CORS
from gemini import generate_gemini_reply  # Import functions from gemini.py
from gemini import return_dynamic_prices
from gemini import return_wholesale_orders
from gemini import return_seasonal_items
from gemini import calculate_revenue

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    print(f"received from frontend: {user_message}")

    try:
        reply = generate_gemini_reply(user_message)
        print(f"gemini reply: {reply}")
        return jsonify({"reply": reply})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Error: Could not connect to Gemini."}), 500
    
@app.route("/api/insights", methods=["GET"])
def get_insights():
    try:
        insights_data = {
            "dynamic_pricing": return_dynamic_prices(),
            "wholesale_suggestion": return_wholesale_orders(),
            "seasonal_suggestions": return_seasonal_items()
        }
        return jsonify(insights_data)
    except Exception as e:
        print("Error generating insights:", e)
        return jsonify({"error": "Failed to generate insights"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



