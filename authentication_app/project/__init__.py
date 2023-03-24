import functools, os
from dotenv import load_dotenv
from flask import (
    Flask,
    session,
    render_template,
    request,
    abort,
    flash,
    redirect,
    url_for
)
from passlib.hash import pbkdf2_sha256
app = Flask(__name__)
load_dotenv()

# Secret key generated with secrets.token_urlsafe()
secret_key = os.environ.get("secret_key")
app.secret_key = secret_key
user = {}

def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        username = session.get("username")
        if not username or username not in user:
            return redirect(url_for("login"))
        return route(*args, **kwargs)
    return route_wrapper

@app.get("/")
@login_required
def home():
    return render_template(
                        "home.html", 
                        stylesheet="styles.css",
                        username=session.get("username"),
                        email=session.get("email"),
                        title="Home"
                        )

@app.get("/protected")
@login_required
def protected():
    return render_template("protected.html", stylesheet="styles.css", title="Protected")

@app.route("/login", methods=["POST", "GET"])
def login():
    username = ""
    if request.method == "POST":
        username = request.form.get("user_name")
        password = request.form.get("password")
        if(user.get(username) != None):
            if pbkdf2_sha256.verify(password, user.get(username)["password"]):
                session["username"] = username # this does the login for us
                session["email"] = user.get(username)["email"]
                return redirect(url_for("protected"))
        
        flash("Incorrect e-mail or password")

    return render_template("login.html", stylesheet="styles.css", title="Log in")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        
        user[user_name] = {"email" : email , "password" : pbkdf2_sha256.hash(password)}
        flash("Succesfully signed up.")
        return redirect(url_for("login"))

    return render_template("signup.html", stylesheet="sign_up_style.css", title="Signup")

@app.route("/about")
def about():
    return render_template("about.html", title="About me")
