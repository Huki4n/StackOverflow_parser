import requests
#from getpass import getpass
#from bs4 import BeautifulSoup

def getRequestUrl(request):
  request_url = "+".join(request.split(" "))
  return  request_url

def getHTMLfile(request_url):
  login_url = 'https://stackoverflow.com/users/login'
  login_data = {
    'email': "ggag22221@mail.ru",
    'password': "parsman123"
  }

  session = requests.Session()  # запуск сессии
  autorization = session.post(login_url, data=login_data)
  session = session.get(f"https://stackoverflow.com/search?q={getRequestUrl(request_url)}")

  file = open('site.html', 'w', encoding="utf-8")
  for html in session.text:
    file.write(html)




