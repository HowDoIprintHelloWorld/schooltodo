from flask import Flask, render_template, request, url_for, redirect, make_response
from src.ScuffedDb import DB
from src.HandleUsers import UserHandler
from src.GetSubjects import getSubjects, filterSubjects
from os import environ

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
  name = "login"
  subjects = getSubjects()
  if request.method == "POST":
    if request.form.get('subject') and request.form.get('task') and request.form.get('due-date'):
      data = f"{request.form.get('subject')}:    &| {request.form.get('task')} &|           {request.form.get('due-date')}\n"
      if request.form.get('test-check') == None:
        db.add(data)
      else:
        examdb.add(data)

  db.update()
  examdb.update()
  checkedOff = []
  user = request.cookies.get("user")
  if user:
    checkedOff = uh.getCheckedOff(user)
    name = uh.userFromCookie(user)
    name = name[0].upper() + name[1:]
    subjects = filterSubjects(uh.userFromCookie(user), subjects)
  return render_template("index.html", toDoL=db.grab(), subjects=subjects, toDoTestL=examdb.grab(), checkedOff=checkedOff, name=name)

@app.route("/remove")
def remove():
  db.remove(request.args.get("item"))
  return redirect(url_for("index"))

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    if uh.check(request.form.get("username").lower()):
      resp = make_response(redirect(url_for("index")))
      resp.set_cookie('user', uh.makeCookie(request.form.get("username").lower()))
      return resp

  # if request.cookies.get("user"):
    # if uh.loginCookie(request.cookies.get("user")): return redirect(url_for("index"))
  return render_template("login.html")


@app.route("/done")
def done():
  if request.cookies.get("user"):
    if uh.loginCookie(request.cookies.get("user")):
      uh.checkOff(request.cookies.get("user"), request.args.get("item"))
    return redirect(url_for("index"))
  else:
    return redirect(url_for("login"))


if __name__ == "__main__":
  db, examdb = DB("normal"), DB("exam")
  uh = UserHandler()
  app.run(host='0.0.0.0', port=environ.get('PORT'))