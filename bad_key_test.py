import json
import urllib.request
import urllib.error

url = "https://api.anthropic.com/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "sk-ant-this-is-a-fake-key",
    "anthropic-version": "2023-06-01",
}
body = json.dumps({
    "model": "claude-sonnet-5-5",
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "Hello"}],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print("Status code:", e.code)
    print("Response body:", e.read().decode())
