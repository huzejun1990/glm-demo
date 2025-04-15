# @Author : huzejun
# @Time : 2025/4/15 10:47
from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 整个md文件内容的一个document
# loader = UnstructuredMarkdownLoader(file_path='test_translated.md')

loader = UnstructuredMarkdownLoader(file_path='test_translated.md', mode='elements')

# data = loader.load()
data = loader.load_and_split()
print(data)