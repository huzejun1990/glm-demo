# @Author : huzejun
# @Time : 2025/4/15 11:18
from langchain_community.document_loaders import PyPDFLoader
from PIL import Image

loader = PyPDFLoader(file_path='test.pdf',extract_images=True)

# 每一页对应一个document
data = loader.load()
print(data)