from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Phishing Simulation API!"})

@app.route('/create-email', methods=['POST'])
def create_email():
    data = request.get_json()
    subject = data.get('subject')
    body = data.get('body')
    # Here you would normally save the data to a database
    return jsonify({"message": f"Phishing email created with subject: {subject}"})

if __name__ == '__main__':
    app.run(debug=True)
