# @Author : huzejun
# @Time : 2025/3/26 20:14
from openai import OpenAI
# import os

# 使用OpenAI自己的

# api_key = os.getenv('API_KEY')
# print(api_key)
client = OpenAI(
    api_key='我的帐号',
    base_url='https://open.bigmodel.cn/api/paas/v4/'

)

# response = client.chat.completions.create(
response = client.chat.completions.create(
    # model='glm-4-0520', # glm-4-9b
    model='glm-4-9b',
    messages=[
        {'role': "user", 'content': '请介绍一下大模型的定义?'}
    ],
    # stream=True
)

# 流式的输出
# for s in response:
#     print(s.chioces[0].delta)


print(response)
#
print(response.choices[0].message.content)