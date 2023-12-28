from flask import Flask
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Авторизация
login_url = 'https://stackoverflow.com/users/login'
login_data = {
  'email': "ggag22221@mail.ru",
  'password': "parsman123"
}

def getAnswersForRequests(request):
  session = requests.Session()  # запуск сессии
  autorization = session.post(login_url, data=login_data)  # авторизация
  session = session.get(f"https://stackoverflow.com/search?q={request}")  # получаем страницу со всеми ответами

  soup = BeautifulSoup(session.text, "lxml")  # форматируем для работы в bs4
  answers_data = soup.findAll("div", class_="s-post-summary")  # находим все ответы по промту

  counter = 0
  for links in answers_data[0:3]:  # отделяем 3 ответа и записываем их в HTML
    find_link = links.find("h3", class_="s-post-summary--content-title").find("a", class_="s-link").get(
      "href")  # ищем ссылку на ответ
    response = requests.get(f"https://stackoverflow.com{find_link}")  # переходим на страницу с ответом
    soup = BeautifulSoup(response.text, "lxml")  # форматируем для работы в bs4
    div = soup.find("div", class_="answer").find("div", class_="s-prose js-post-body")  # вырезаем div с ответом

    counter += 1
    file = open(f'templates/new_answers/answer{counter}.html', 'w', encoding="utf-8")  # сохраняем в файлы
    for html in div:
      file.write(str(html))
