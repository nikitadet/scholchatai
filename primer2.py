import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
# Вывод ответа, полученного от сервера API
print(response.json())
