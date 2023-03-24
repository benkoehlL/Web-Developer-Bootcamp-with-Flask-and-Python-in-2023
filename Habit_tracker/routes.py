from flask import Blueprint, current_app, render_template, request, redirect, url_for
import sys, os, datetime
import uuid
sys.path.append("/Habit_tracker")


pages = Blueprint("habits", __name__, template_folder="templates", static_folder="static")

@pages.context_processor
def add_calc_date_range():
    def date_range(start: datetime.datetime):
        dates = [start +datetime.timedelta(days=diff) for diff in range(-3,4)]
        return dates
    return {"date_range": date_range}

def today_at_midnight():
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month, today.day) # by default, time, min, sec are 0

@pages.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.datetime.fromisoformat(date_str)
    else:
        selected_date = today_at_midnight()

    habits_on_current_date = current_app.db.habits.find({"added": {"$lte": selected_date}})

    completions = [
        habit["habit"]
        for habit in current_app.db.completions.find({"date": selected_date})
    ]

    return render_template("index.html",
                            habits=habits_on_current_date, 
                            title="Habit Tracker - Home", 
                            selected_date=selected_date,
                            completions=completions)

@pages.route("/add", methods=["GET", "POST"])
def add_habit():
    today = today_at_midnight()
    if(request.form or request.method == "POST"):
        current_app.db.habits.insert(
            {"_id": uuid.uuid4().hex,
              "added": today,
              "name": request.form.get("habit")}
        )
    return render_template("add_habit.html", title="Habit Tracker - Add Habit", selected_date=today)

@pages.post("/complete")
def complete():
    date_string = request.form.get("date")
    habit = request.form.get("habitId")
    date = datetime.datetime.fromisoformat(date_string)
    current_app.db.completions.insert({"date": date, "habit": habit})
    return redirect(url_for("habits.index", date=date_string))