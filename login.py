from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<form method="POST">
  Email: <input name="email"><br><br>
  Password: <input type="password" name="password"><br><br>
  <button type="submit">Login</button>
  <p style="color:red;">{{ error }}</p>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not email or not password:
            error = "Email and password are required."
        elif "@" not in email:
            error = "Enter a valid email."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        else:
            return "Login successful!"

    return render_template_string(HTML, error=error)

app.run(debug=True)
