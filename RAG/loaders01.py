# @Author : huzejun
# @Time : 2025/4/2 22:06
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='../weather_district_id.csv',encoding='utf-8')

data = loader.load()

for recod in data[:2]:
    print(recod)