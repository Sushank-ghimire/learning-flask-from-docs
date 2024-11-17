from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# File to store registered users' data
USERS_FILE = "users.txt"

# Function to save user data to file
def save_user_to_file(username, email, password):
    with open(USERS_FILE, 'a') as file:
        file.write(f"{username},{email},{password}\n")

# Function to load users' data from file
def load_users_from_file():
    users = {}
    try:
        with open(USERS_FILE, 'r') as file:
            for line in file:
                username, email, password = line.strip().split(',')
                users[email] = {'username': username, 'password': password}
    except FileNotFoundError:
        pass
    return users

@app.route("/")
def home():
    return render_template("index.html", user=session.get('user'))

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Form validation
        if not email or not password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for('login'))

        # Load users from file and check credentials
        users = load_users_from_file()
        user = users.get(email)

        if user and user['password'] == password:
            session['user'] = {'email': email, 'username': user['username']}
            flash("Logged in successfully!", "success")
            return redirect(url_for('dashboard'))
        
        flash("Invalid email or password.", "error")
    return render_template("login.html")

# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Form validation
        if not username or not email or not password:
            flash("Please fill in all fields.", "error")
            return redirect(url_for('register'))

        # Load users from file to check if email already exists
        users = load_users_from_file()
        if email in users:
            flash("Email already registered. Please log in.", "error")
            return redirect(url_for('login'))
        
        # Save new user
        save_user_to_file(username, email, password)
        flash("Registered successfully! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template("register.html")

# Logout route
@app.route("/logout")
def logout():
    session.pop('user', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

# Dashboard route accessible to logged-in users
@app.route("/dashboard")
def dashboard():
    if 'user' not in session:
        flash("Please log in to access the dashboard.", "warning")
        return redirect(url_for('login'))

    # Load all users from the file to display in the dashboard
    users = load_users_from_file()
    return render_template("dashboard.html", users=users, current_user=session['user'])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Process the message (e.g., save to a file or send an email)
    print(f"Message from {name} ({email}): {message}")

    flash("Your message has been sent successfully!", "success")
    return redirect(url_for("contact"))

# Custom 404 page route
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)