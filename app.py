import time
from flask import Flask, render_template, request, redirect
import requests
from parser import *

app = Flask(__name__)

@app.route("/stackoverflow_set_request")
def form():
  return render_template("index.html")

@app.post("/stackoverflow_get_request")
def get_request():
  print(request.form['problem'])
  getHTMLfile(request.form['problem'])
  return redirect("/stackoverflow_set_request")




