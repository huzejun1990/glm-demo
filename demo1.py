# @Author : huzejun
# @Time : 2025/3/26 19:20
from zhipuai import ZhipuAI

# 使用GLM自己的

# api_key = os.getenv('API_KEY')
# print(api_key)
client = ZhipuAI(api_key='我的帐号')
response = client.chat.completions.create(
    model='glm-4-0520', # glm-4-9b
    # model='glm-4-flash',
    messages=[
        {'role': "user", 'content': '请介绍一下大模型的定义?'}
    ],
    stream=True
)

# 流式的输出
for s in response:
    print(s.choices[0].delta)

# print(response)


# print(response.choices[0].message.content)
