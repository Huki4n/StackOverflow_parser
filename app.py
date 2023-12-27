import time

import requests
from flask import Flask, render_template, request, redirect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
app = Flask(__name__)


@app.route("/stackoverflow_set_request")
def form():
  return render_template("index.html")

@app.post("/stackoverflow_get_request")
def get_request():
  user_request = "+".join(request.form['problem'].split(" "))
  url = f"https://stackoverflow.com/search?q={user_request}"

  driver = webdriver.Chrome()
  driver.get(url)
  # СТОИТ НА ЭТОМ МОМЕНТЕ
  shit_cookies = driver.find_element(By.CSS_SELECTOR,".js-accept-cookies")
  shit_cookies.click()

  answer_tag = driver.find_element(By.CSS_SELECTOR,".answer-hyperlink ")
  answer_url = answer_tag.get_attribute("href")
  driver.get(answer_url)

  return redirect("/stackoverflow_set_request")


