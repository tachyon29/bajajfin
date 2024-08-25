from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
USER_ID = "aman_gupta_29042003"
EMAIL = "aman.gupta2021c@vitstudent.ac.in"
ROLL_NUMBER = "21BCE5055"

@app.route('/bfhl', methods=['POST'])
def post_endpoint():
    try:
        data = request.get_json()
        input_data = data.get('data', [])

        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]
        highest_lowercase_alphabet = sorted([item for item in alphabets if item.islower()])[-1:] if alphabets else []

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})

@app.route('/bfhl', methods=['GET'])
def get_endpoint():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
