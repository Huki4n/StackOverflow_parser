from flask import Flask
import requests
from getpass import getpass
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/stackoverflow")
def hello_world():
  return "<p style = 'font-size:2rem;color:red;'>Hello, world!<p>"

login_url = 'https://stackoverflow.com/users/login'
login_data = {
    'email': "ggag22221@mail.ru",
    'password': "parsman123"
}


promt = input("Введите проблему: ")


session = requests.Session() # запуск сессии
autorization = session.post(login_url, data=login_data)
session = session.get(f"https://stackoverflow.com/search?q={promt}")

file = open('site.html', 'w')
for html in session.text:
  file.write(html)
