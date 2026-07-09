from dotenv import load_dotenv
load_dotenv()
from flask import Flask , render_template , request , redirect , url_for, send_from_directory
import pymysql
import os
pymysql.install_as_MySQLdb()
app=Flask(__name__)
def get_db():return pymysql.connect(
    host=os.environ.get("DB_HOST"),
    port=int(os.environ.get("DB_PORT")),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_DATABASE"),
    ssl={"ssl":{}}
)
@app.route("/")
def todo():
    return render_template("todo.html")

@app.route("/options")
def options():
    return render_template("options.html")

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        task=request.form["task"]
        db=get_db()
        cursor=db.cursor()
        cursor.execute("INSERT INTO task (task_name) values (%s);",(task,))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for("options"))
    return render_template("add.html")

@app.route("/view",methods=["GET","POST"])
def view():
    db=get_db()
    cursor=db.cursor()
    cursor.execute("SELECT * from task;")
    tasks=cursor.fetchall()
    print("tasks:",tasks)
    cursor.close()
    db.close()
    return render_template("view.html",tasks=tasks)

@app.route("/delete/<int:task_id>",methods=["GET","POST"])
def delete(task_id):
    db=get_db()
    cursor=db.cursor()
    cursor.execute("delete from task where id=%s;",(task_id,))
    db.commit()
    cursor.close()
    db.close()    
    return redirect(url_for("view"))
#PWA CODE (to create an app icon after deploying)
@app.route("/manifest.json")
def manifest():
    return send_from_directory(".", "manifest.json")
@app.route("/service-worker.js")
def service_worker():
    return send_from_directory(".", "service-worker.js")

if __name__==("__main__"):
    app.run(debug=True)