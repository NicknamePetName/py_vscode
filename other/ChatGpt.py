import requests

def call_chatgpt_api(input_text):
    # ChatGPT API端点URL
    api_endpoint = "https://api.openai.com/v1/chat/completions"

    # 替换成你的API密钥（如果有的话）
    api_key = "sk-proj-bfbOyOqCcLupJVCjdjHFT3BlbkFJl6PtbZMbhCXTUmxj96ku"

    # 请求头
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 请求体
    data = {
        "text": input_text,
        "model": "gpt-3.5-turbo"  # 选择你想要的GPT模型
    }

    try:
        # 发送POST请求
        response = requests.post(api_endpoint, headers=headers, json=data)

        # 检查请求是否成功
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

# 调用API并打印响应
input_text = "你好，ChatGPT。"
response = call_chatgpt_api(input_text)
if response:
    print("API Response:")
    print(response)
else:
    print("Failed to get response from API.")
