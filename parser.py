import os

from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Авторизация
login_url = 'https://stackoverflow.com/users/login'
login_data = {
  'email': "ggag22221@mail.ru",
  'password': "parsman123"
}


def getAnswersForRequests(request):
  deleteAnswers()

  session = requests.Session()  # запуск сессии
  autorization = session.post(login_url, data=login_data)  # авторизация
  session = session.get(f"https://stackoverflow.com/search?q={request}")  # получаем страницу со всеми ответами

  soup = BeautifulSoup(session.text, "lxml")  # форматируем для работы в bs4
  answers_data = soup.findAll("div", class_="s-post-summary")  # находим все ответы по промту

  num_file = 0
  count_answer = 3
  for links in answers_data:  # отделяем 3 ответа и записываем их в HTML

    is_answer = links.find("div", class_="s-post-summary--stats")  # проверка на нонтайп
    is_answer = is_answer.find("div", class_="s-post-summary--stats-item has-answers has-accepted-answer")

    if is_answer is not None:
      is_answer = int(is_answer.find("span", class_="s-post-summary--stats-item-number").text)
    else:
      continue

    if is_answer <= 0:  # проверка на наличие ответов
      continue
    else:  # все как обычно
      find_link = links.find("h3", class_="s-post-summary--content-title").find("a", class_="s-link").get(
        "href")  # ищем ссылку на ответ
      response_url = requests.get(f"https://stackoverflow.com{find_link}")  # переходим на страницу с ответом
      soup = BeautifulSoup(response_url.text, "lxml")  # форматируем для работы в bs4

      div_response = soup.find("div", class_="answer").find("div", class_="s-prose js-post-body")  # вырезаем div с ответом

      num_file += 1
      file_html = open(f'templates/new_answers/answer{num_file}.html', 'w', encoding="utf-8")  # сохраняем в файлы
      for html in div_response:
        file_html.write(str(html))

      count_answer -= 1
    if count_answer == 0:
      break


def deleteAnswers():
  if os.path.exists(f'templates/new_answers/answer1.html'):
    for i in range(1, 4):
      file = open(f'templates/new_answers/answer{i}.html', 'w', encoding="utf-8")  # сохраняем в файлы
      file.write('')
