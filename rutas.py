from flask import Blueprint, render_template, request, url_for, redirect
import json
file = "data.json"

CansatApp = Blueprint("rutas", __name__)

with open(file, "r") as json_file:
  datos = json.load(json_file)

@CansatApp.route("/")
def index():
    return redirect(url_for("rutas.dashboard"))

@CansatApp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", elements=datos)

@CansatApp.route("/conexion")
def conexion():
    return render_template("conexion.html")

@CansatApp.route("/ajustes")
def ajustes():
    return render_template("ajustes.html")
