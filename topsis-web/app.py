from flask import Flask, render_template, request, send_file
import os
from topsis.topsis import topsis
import yagmail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form.get("email", "").strip()

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")

        file.save(input_path)

        topsis(input_path, weights, impacts, output_path)

        if email:
            user = os.environ.get('GMAIL_USER')
            password = os.environ.get('GMAIL_APP_PASSWORD')
            if not user or not password:
                print("Email credentials not set. Please set GMAIL_USER and GMAIL_APP_PASSWORD environment variables.")
            else:
                try:
                    print(f"Sending email to {email}...")
                    yag = yagmail.SMTP(user, password)
                    yag.send(to=email, subject='TOPSIS Results', contents='Here are your TOPSIS results.', attachments=output_path)
                    print("Email sent successfully.")
                except Exception as e:
                    print(f"Email error: {e}")

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
