# @Author : huzejun
# @Time : 2025/4/13 10:05
import bs4
from langchain_community.document_loaders import WebBaseLoader
# from langchain_community.document_loaders.parsers.html import bs4 # bs4直接安装包就行，不用再引用langchain_community包下面的bs4

loader = WebBaseLoader(
    web_paths=('https://fastapi.tiangolo.com/zh/features/',),
    encoding='utf-8',
    # bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=('md-content',)))
    # bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=('md-content',)))
    bs_kwargs = dict(parse_only=bs4.SoupStrainer(class_=('md-content',)))

)

docs =  loader.load()
print(docs)