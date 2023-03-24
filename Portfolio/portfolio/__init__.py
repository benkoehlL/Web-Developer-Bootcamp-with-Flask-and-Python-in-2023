from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Fast Interpolation on arbitary areas",
        "thumb": "images/habit-tracking.png",
        "hero": "imges/habit-tracking-hero.png",
        "categories": ["Numerics", "Mathematics", "C++"],
        "slug": "fast_interpolation",
        "prod": "https://www.thorsis.com/de/medizintechnik/plantapress/"
    },
    {
        "name": "Field control of magnonic heat flow",
        "thumb": "images/personal-finance.png",
        "hero": "images/personal-finance.png",
        "categories": ["Physics"],
        "slug": "field_control_of_heat_flow",
        "prod": "{{ url_for('static', filename='documents/dissertation_Koehler_Benjamin.pdf') }}"
    },
    {
        "name": "Quantum Computing: Transpiler GUI",
        "thumb": "images/rest-api-docs.png",
        "hero": "images/rest-api-docs.png",
        "categories": ["Python", "PyQt6", "Physics"],
        "slug": "Quantum_Transpiler",
        "prod": "https://saxonq.com/"
    }
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html",
                            project=slug_to_project[slug]
                            )
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404