from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():
    return render_template("/dashboard/index.html")


@main.route("/history")
def history():
    return render_template("/history/index.html")


@main.route("/settings")
def settings():
    return render_template("/settings/index.html")
