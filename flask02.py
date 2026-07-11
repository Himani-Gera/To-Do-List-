from dotenv import load_dotenv
load_dotenv()
from flask import Flask , render_template , request , redirect , url_for, session, send_from_directory
import pymysql
import os
pymysql.install_as_MySQLdb()
app=Flask(__name__)
app.secret_key=os.environ.get('SECRET_KEY',"dev-secret-change-this")
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
@app.route("/login" ,methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        if username:
            session["username"]=username
            return redirect(url_for("options"))
    return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("todo"))

@app.route("/options")
def options():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("options.html")

@app.route("/add",methods=["GET","POST"])
def add():
    if "username" not in session:
       return redirect(url_for("login"))
    if request.method=="POST":
        task=request.form["task"]
        db=get_db()
        cursor=db.cursor()
        cursor.execute("INSERT INTO task (task_name,username) values (%s,%s);",(task,session["username"]))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for("options"))
    return render_template("add.html")

@app.route("/view",methods=["GET","POST"])
def view():
    if "username" not in session:
        return redirect(url_for("login"))
    db=get_db()
    cursor=db.cursor()
    cursor.execute("SELECT * from task where username=%s;",(session["username"],))
    tasks=cursor.fetchall()
    print("tasks:",tasks)
    cursor.close()
    db.close()
    return render_template("view.html",tasks=tasks)

@app.route("/delete/<int:task_id>",methods=["GET","POST"])
def delete(task_id):
    if "username" not in session:
        return redirect(url_for("login"))
    db=get_db()
    cursor=db.cursor()
    cursor.execute("delete from task where id=%s and username=%s;",(task_id,session["username"]))
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