from requests import get 

headers = {"Authorization": "Ваш ключ"}
response = get("https://api.mistral.ai/v1/chat/completions", headers=headers, json={
  "model": "mistral-small-latest",
  "temperature": 1.5,
  "top_p": 1,
  "max_tokens": 0,
  "stream": False,
  "stop": "string",
  "random_seed": 0,
  "messages": [
    {
      "role": "user",
      "content": "Who is the best French painter? Answer in one short sentence."
    }
  ],
  "response_format": {
    "type": "text",
    "json_schema": {
      "name": "string",
      "description": "string",
      "schema": {},
      "strict": False
    }
  },
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "string",
        "description": "",
        "strict": False,
        "parameters": {}
      }
    }
  ],
  "tool_choice": "auto",
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "n": 1,
  "prediction": {
    "type": "content",
    "content": ""
  },
  "parallel_tool_calls": True,
  "prompt_mode": "reasoning",
  "safe_prompt": False
})
print(response)
