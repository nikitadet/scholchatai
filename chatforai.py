import os
from mistralai import Mistral

a = input("введите свой запрос:")
model = "mistral-large-latest"

client = Mistral(api_key="Сюда всталяете ключ полученный на сайте")

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": f"{a}"
        },
    ]
)
print(chat_response.choices[0].message.content)
