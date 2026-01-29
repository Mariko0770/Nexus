from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB = "database/nexus.db"

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def add_item(table, data, columns):
    placeholders = ",".join("?"*len(columns))
    column_names = ",".join(columns)
    query_db(f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})", data)

@app.route("/")
def index():
    notes = query_db("SELECT * FROM notes ORDER BY id DESC")
    events = query_db("SELECT * FROM events ORDER BY id DESC")
    goals = query_db("SELECT * FROM goals ORDER BY id DESC")
    tasks = query_db("SELECT * FROM tasks ORDER BY id DESC")
    birthdays = query_db("SELECT * FROM birthdays ORDER BY id DESC")
    projects = query_db("SELECT * FROM projects ORDER BY id DESC")
    return render_template("index.html",
                           notes=notes, events=events, goals=goals,
                           tasks=tasks, birthdays=birthdays, projects=projects)

# Add routes
@app.route("/add_note", methods=["POST"])
def add_note():
    add_item("notes",[request.form["title"],request.form.get("content","")],["title","content"])
    return jsonify(success=True)

@app.route("/add_event", methods=["POST"])
def add_event():
    add_item("events",[request.form["name"],request.form.get("event_date",""),request.form.get("category","")],
             ["name","event_date","category"])
    return jsonify(success=True)

@app.route("/add_goal", methods=["POST"])
def add_goal():
    add_item("goals",[request.form["title"],request.form.get("start",""),request.form.get("target","")],
             ["title","start_date","target_date"])
    return jsonify(success=True)

@app.route("/add_task", methods=["POST"])
def add_task():
    goal_id = request.form.get("goal_id") or None
    add_item("tasks",[goal_id,request.form["description"],request.form.get("due_date","")],
             ["goal_id","description","due_date"])
    return jsonify(success=True)

@app.route("/add_birthday", methods=["POST"])
def add_birthday():
    add_item("birthdays",[request.form["name"],request.form.get("birth_date",""),request.form.get("relation","")],
             ["name","birth_date","relation"])
    return jsonify(success=True)

@app.route("/add_project", methods=["POST"])
def add_project():
    add_item("projects",[request.form["name"],request.form.get("project_date","")],
             ["name","project_date"])
    return jsonify(success=True)

# Delete route
@app.route("/delete/<table>/<int:id>")
def delete_item(table,id):
    allowed = ["notes","events","goals","tasks","birthdays","projects"]
    if table in allowed:
        query_db(f"DELETE FROM {table} WHERE id = ?", [id])
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
