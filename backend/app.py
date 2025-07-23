from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

@app.route("/contact", methods=["POST", "OPTIONS"])
def contact():
    print("Hit the /contact endpoint")

    if request.method == "OPTIONS":
        return jsonify({}), 200
    
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")
        print(f"Parsed values: name={name}, email={email}, message={message}")
    except Exception as e:
        print("Failed to parse Json:", e)

    #Validation checking
    if not name:
        return jsonify({"success": False, "error": "Name is required"}), 400
    if len(name) > 30:
        return jsonify({"sucess": False, "error": "Name too long"}), 400
    if not all(part.isalpha() for part in name.split()):
        return jsonify({"success": False, "error": "Name cannot contain numbers"}), 400
    
    if not email:
        return jsonify({"success": False, "error": "Email is required"}), 400

    print(f"Received message from {name} ({email}): {message}")

    sendgrid_api_key = os.getenv("SENDGRID_API_KEY")

    message = Mail(
        from_email="contact@ianquack.com",
        to_emails='ianq500@gmail.com',
        subject=f'New Contact Form Submission from {name}',
        html_content=f"""
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Message:</strong> {message}</p>
        """
    )

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
        if response.status_code == 202:
            return jsonify({'message': 'Email sent succesfully'}), 200
        else:
            return jsonify({'error': 'Failed to send email'}), 500
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'error': 'Exception occurred while sending mail'}), 500

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))