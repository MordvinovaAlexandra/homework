from flask import Blueprint, request, render_template, redirect, flash
from flask_login import login_user, logout_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import repository
import model
import services
import exceptions
from config import build_db_uri
from db_tables import start_mappers, metadata

engine = create_engine(build_db_uri(".env"))
get_session = sessionmaker(bind=engine)

# try:
#     metadata.create_all(bind=engine)
#     start_mappers()
# except Exception:
#     pass

auth = Blueprint('auth', __name__, static_folder="static", template_folder="templates"
)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('auth/login.html')
    
    login_field = request.form.get('email')
    password_field = request.form.get('password')

    session = get_session()
    print([u.username for u in session.query(model.User).where(model.User.username == login_field).all()])
    user = (
        session.query(model.User)
        .where(model.User.username == login_field)
        .first()
    )

    if user and user.check_password(password_field):
        login_user(user)
        return redirect("/admin")
    
    flash("Invalid login or password. Try again", "error")
    return render_template("auth/login.html")
    

@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/auth/login")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template('auth/signup.html')
    
    email_field = request.form.get('email')
    password_field = request.form.get('password')
    print(email_field, password_field)

    session = get_session()
    user = (
        session.query(model.User)
        .where(model.User.username == email_field)
        .first()
    )

    if user:
        flash("Account already exists. Maybe you want to sigh in?", "error")
        return render_template("auth/signup.html")
    
    session.add(model.User(email_field, password_field))
    session.commit()

    return redirect("/auth/login")