from flask import Flask, render_template
import sys
sys.path.append("/Flask")

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/fancy")
def hello_world_fancy():
    return """
    <html>
    <body>
    <h1>Greetings!</h1>
    <p>Hello, world!</p>
    </body>
    </html>
    """

@app.route("/first_template/")
def hello_first_template():
    return render_template("first_page.html")

@app.route("/second_template/")
def hello_second_template():
    return render_template("second_page.html")

@app.route("/jinja_template/")
def hello_jinja_template():
    return render_template(
        "jinja_intro.html",
        name= "Benjamin",
        template_name = "Jinja2"
    )

@app.route("/expressions/")
def hello_expressions_template():
    kwargs = {
        "color" : "black",
        "animal_one" : "Penguin",
        "animal_two" : "Tiger",
        "orange_amount" : 6,
        "apple_amount" : 13,
        "donate_amount" : 7
    }
    return render_template(
        "expressions.html",
        **kwargs
    )

@app.route("/data_structures/")
def hello_data_structures_template():
    Dinas_favourite_movies = ["Stalker", "Harry Potter", "Arrival"]
    car = {"brand": "Toyota", "model": "Corolla", "year": 1997}
    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
    
    kwargs = {"movies" : Dinas_favourite_movies,
              "car" : car,
              "moons": moons
    }
    
    return render_template("data_structures.html", 
                           **kwargs)

@app.route("/conditionals/")
def hello_conditionals_template():
    company = "Microsoft"
    return render_template("conditionals.html", company=company)

@app.route("/for_loop/")
def hello_for_loop():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptun"
    ]
    return render_template("for_loops.html", planets=planets)

@app.route("/for_loop_conditionals/")
def hello_for_loop_conditionals():
    user_os = {
        "Benjamin Köhler": {"Linux"},
        "Matthias Mendt" : {"Linux", "Microsoft"},
        "Robert Karsthof": {"Microsoft"},
        "Max Kneiß": {"Microsoft"},
        "Johannes Engel" : {"Microsoft"},
        "Tobias Herzig": {"Microsoft"},
        "Nicole Raatz": {"Microsft"}
        }
    return render_template("for_loop_conditionals.html", user_os=user_os)