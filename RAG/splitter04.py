# @Author : huzejun
# @Time : 2025/4/17 14:41
import os

from langchain_community.embeddings import BaichuanTextEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

with open('test.txt', encoding='utf-8') as f:
    text_data = f.read()

# os.environ['BAICHUAN_API_KEY'] = '***************************'
os.environ['BAICHUAN_API_KEY'] = '百川智能api'  # https://platform.baichuan-ai.com/console/apikey
embeddings = BaichuanTextEmbeddings()

text_splitter = SemanticChunker(embeddings,breakpoint_threshold_type='percentile')

docs_list = text_splitter.create_documents([text_data])

print(docs_list[0].page_content)