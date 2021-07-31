
import datetime
from flask import render_template, request, redirect, url_for, jsonify, Flask, g, Blueprint,flash
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
bp = Blueprint("todo", "__name__", url_prefix="")

@bp.route("/" ,methods=['GET'])   
def main():
  return render_template("login.html")

@bp.route("/login", methods = ["GET", "POST"])
def login():
  conn = db.get_db()
  cursor = conn.cursor()
  status = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    cursor.execute("select id from login l where uname = %s and pas=%s ; ", (username,password))
    s= cursor.fetchone()
    if s is None:
        return '''<script>alert("Invalid username or password");window.location='/'</script>'''
    else:
        return redirect(url_for("todo.home",id=s), 302)
    
@bp.route('/logout',methods=['GET'])
def logout():
    return '''<script>alert("Successfully logged out");window.location='/'</script>'''
@bp.route("/create")
def reg():
  return render_template("register.html")

@bp.route("/register", methods=["POST"])
def register():
  conn = db.get_db()
  cursor = conn.cursor()
  name = request.form['name']
  username = request.form['username']
  password = request.form['password']
  cursor.execute("""insert into login (name,uname,pas) values (%s,%s,%s);""", (name,username,password))
  conn.commit()
  return redirect(url_for("todo.main",), 302)
  
@bp.route("/home/<id>",methods=['GET'])
def home(id):
  conn = db.get_db()
  cursor = conn.cursor()
  cursor.execute("select * from todolist where uid = %s;",(id))
  s=cursor.fetchall()
  cursor.execute("select * from login where id = %s ;",(id))
  n=cursor.fetchone()
  cursor.execute("select count(*) from todolist where uid = %s and status=FALSE ;",(id))
  c=cursor.fetchone()
  return render_template("todoform.html",todo=s,user=n,id=id,count=c)
  
  
@bp.route("/addtodo/<id>",methods=["POST"])
def addtodo(id):
  conn = db.get_db()
  cursor = conn.cursor()
  task = request.form['todolist']
  date = request.form['date']
  cursor.execute("""insert into todolist (uid, task, lastdate,status) values (%s,%s, %s, FALSE);""", (id,task, date))
  conn.commit()
  return redirect(url_for("todo.home",id=id), 302)
 
@bp.route("/deletetodo/<id>/<lid>",methods=["GET"])
def deletetodo(id,lid):
  conn = db.get_db()
  cursor = conn.cursor()
  cursor.execute("""delete from todolist where id=%s and uid=%s ;""",(lid,id))
  conn.commit()
  return redirect(url_for("todo.home",id=id), 302)
 
@bp.route("/edittodo/<id>/<lid>",methods=["POST"])
def edittodo(id,lid):
  conn = db.get_db()
  cursor = conn.cursor()
  task = request.form['etodolist']
  date = request.form['edate']
  cursor.execute("""update todolist set task=%s, lastdate=%s where id=%s ;""", (task, date,lid))
  conn.commit()
  return redirect(url_for("todo.home",id=id), 302)
   
@bp.route("/edittodo/<id>/<lid>",methods=["GET"])
def edit(id,lid):
  conn = db.get_db()
  cursor = conn.cursor()
  cursor.execute("select * from todolist where id = %s;",(lid))
  s=cursor.fetchone()
  cursor.execute("select * from login where id = %s ;",(id))
  n=cursor.fetchone()
  return render_template('edit.html',todo=s,user=n,id=id,lid=lid)
  
@bp.route("completetodo/<id>/<lid>",methods=['GET'])
def completetodo(id,lid):
  conn = db.get_db()
  cursor = conn.cursor()
  cursor.execute("update todolist set status=TRUE where id = %s;",(lid))
  conn.commit()
  return redirect(url_for("todo.home",id=id), 302)
 
  
 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
