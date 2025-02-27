from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for GET request
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# Route for POST request
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        if not data or "data" not in data:
            return jsonify({"is_success": False, "error": "Invalid input"}), 400
        
        # Extract numbers and alphabets
        numbers = [item for item in data["data"] if item.isdigit()]
        alphabets = [item for item in data["data"] if item.isalpha()]

        # Find the highest alphabet (case insensitive)
        highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
