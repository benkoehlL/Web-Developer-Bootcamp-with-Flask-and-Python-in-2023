import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
import sys, os
from dotenv import load_dotenv
sys.path.append("/Micro_Blog")

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MongoDB_URI"))
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def Microblog():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
            app.db.entries.insert({"content": entry_content, "date": formatted_date})
        entries_with_date = [
            (entry["content"],
            entry["date"], 
            datetime.datetime.strptime(entry["date"], "%d-%m-%Y").strftime("%d %b")
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("project.html", entries=entries_with_date)

    @app.route("/Author")
    def About():
        return render_template("index.html")

    @app.route("/Sign_In")
    def Sign_In():
        return render_template("sign_in_interface.html")
    
    return app