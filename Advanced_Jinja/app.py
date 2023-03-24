from flask import Flask, render_template
import sys
sys.path.append("/Advanced_Jinja")

app = Flask(__name__, static_folder="static")
todos=[("Learn programming", False),
       ("Get milk", True)]

@app.route("/")
def todo():
    return render_template("home.html", todos=todos)

@app.route("/<string:todo>")
def todo_item(todo:str):
    for text, completed in todos:
        if text == todo:
            completed_text= "[x]" if completed else "[ ]"
            title = f"{completed_text} - Todos"
            return render_template("todo.html", text=text, completed=completed, title=title)
        
    return render_template("not-found.html", text=todo, title="Not found")

@app.route("/fizzbuzz")
def fizz():
    return render_template("fizzbuzz.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")