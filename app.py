from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Load the HTML content (single file website)
with open("templates/index.html", "r", encoding="utf-8") as f:
    html_content = f.read()


@app.route("/")
def home():
    """Serve the single-page MakeMyTrip mock website."""
    return render_template_string(html_content)


@app.route("/contact", methods=["POST"])
def contact():
    """Mock contact form submission route."""
    data = request.get_json() or request.form
    name = data.get("name", "Guest")
    email = data.get("email", "")
    message = data.get("message", "")
    print(f"Received contact from {name} ({email}): {message}")
    return jsonify({"status": "success", "message": f"Thank you, {name}! We’ll get back to you soon."})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
