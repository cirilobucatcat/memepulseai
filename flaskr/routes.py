from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/login")
def login():
    return render_template("/auth/login.html")


@main.route("/register")
def register():
    return render_template("/auth/register.html")


@main.route("/")
def home():
    return render_template("/home/index.html")


@main.route("/history")
def history():
    return render_template("/history/index.html")


@main.route("/settings")
def settings():
    return render_template("/settings/index.html")
