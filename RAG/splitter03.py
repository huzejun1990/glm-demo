# @Author : huzejun
# @Time : 2025/4/16 18:33
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

with open('Foo.md', encoding='utf-8') as f:
    text_data = f.read()

lable_split = [
    ('#','大章节'),
    ('##', '小节'),
    ('###', '小点')
]

# strip_headers : 是否在内容中删除，章节的标题
markdown_splitter = MarkdownHeaderTextSplitter(lable_split,strip_headers=False)

docs_list = markdown_splitter.split_text(text_data)
print(docs_list)