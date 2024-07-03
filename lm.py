import requests

def send_inference_request(prompt):
  url = 'http://192.168.0.208:1234/v1/completions'
  headers = {'Content-Type': 'application/json'}
  data = {
    'prompt': prompt,
    'temperature': 0.7,
    'max_tokens': 100
  }

  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
    generated_text = response.json()['choices'][0]['text']
    print('生成されたテキスト:', generated_text)
  else:
    print('エラーが発生しました:', response.status_code, response.text)

if __name__ == '__main__':
  prompt = input('プロンプトを入力してください: ')
  send_inference_request(prompt)
