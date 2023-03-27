from flask import (Blueprint,
                   current_app,
                   render_template,
                   session,
                   url_for,
                   redirect, 
                   request, 
                   flash,
                   abort)
from project.forms import MovieForm, ExtendedMovieForm, RegisterForm
import uuid, datetime
from dataclasses import asdict
from project.model import Movie, User
from passlib.hash import pbkdf2_sha256

pages = Blueprint("pages",
                __name__,
                template_folder="templates",
                static_folder="static")

@pages.route("/")
def index():
    movie_data = current_app.db.movie.find({})
    movies = [Movie(**movie) for movie in movie_data]
    return render_template(
        "index.html",
        title="Movie Watchlist",
        movies_data=movies
    )

@pages.route("/register", methods=["POST", "GET"])
def register():
    if session.get("email"):
        return redirect(url_for(".index"))
    
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(_id= uuid.uuid4().hex,
                    email=form.email.data,
                    password=pbkdf2_sha256.hash(form.password.data))
        current_app.db.user.insert(asdict(user))

        flash("User registered successfully", "success")

        return redirect(url_for(".index"))

    return render_template("register.html", title="Movies Watchlist -- Register", form=form)

@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = Movie(_id= uuid.uuid4().hex,
                    title=form.title.data,
                    director=form.director.data,
                    year= form.year.data
                )
        current_app.db.movie.insert(asdict(movie))
        return redirect(url_for(".index"))

    return render_template("new_movie.html", 
                           title="Movie Watchlist - Add Movie",
                           form=form)

@pages.get("/movie/<string:_id>")
def movie(_id:str):
    movie_data = current_app.db.movie.find_one({"_id": _id})
    if not movie_data:
        abort(404)
    movie = Movie(**movie_data)
    return render_template("movie_details.html", movie=movie)

@pages.get("/movie/<string:_id>/rate")
def rate_movie(_id):
    rating = int(request.args.get("rating"))
    current_app.db.movie.update_one({"_id": _id}, {"$set": {"rating": rating}})

    return redirect( url_for('.movie', _id=_id))

@pages.get("/movie/<string:_id>/watch")
def watch_today(_id):
    current_app.db.movie.update_one({"_id": _id}, {"$set": {"last_watched": datetime.datetime.today()}})
    
    return redirect( url_for('.movie', _id=_id))

@pages.route("/edit/<string:_id>", methods=["GET", "POST"])
def edit_movie(_id: str):
    movie_data = current_app.db.movie.find_one({"_id": _id})
    if not movie_data:
        abort(404)    
    movie = Movie(**movie_data)
    form = ExtendedMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.title = form.title.data
        movie.director = form.director.data
        movie.year = form.year.data
        movie.cast = form.cast.data
        movie.series = form.series.data
        movie.tags = form.tags.data
        movie.description = form.description.data
        movie.video_link = form.video_link.data
        

        current_app.db.movie.update_one({"_id": movie._id}, 
                                        {"$set": asdict(movie)})
        return redirect(url_for(".movie", _id=movie._id))

    return render_template("movie_form.html", 
                           movie=movie,
                           form=form)

@pages.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    return redirect(request.args.get("current_page"))