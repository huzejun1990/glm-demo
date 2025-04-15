# @Author : huzejun
# @Time : 2025/4/15 8:15
from langchain_community.document_loaders import JSONLoader

# loader = JSONLoader(
#     file_path='test.json',
#     jq_schema=".messages[].content",
#     text_content=False
# )

# loader = JSONLoader(
#     file_path='test.json',
#     jq_schema=".messages[] | {content,sender_name}",
#     text_content=False
# )

# loader = JSONLoader(
#     file_path='test.json',
#     jq_schema=".messages[]",
#     text_content=False
# )
# data = loader.load()

def create_metadata(record: dict,metadata: dict) -> dict:
    metadata['snder_name'] = record.get('sender_name')
    metadata['timestamp_ms'] = record.get('timestamp_ms')
    return metadata

loader = JSONLoader(
    file_path='test.json',
    jq_schema='.messages[]',
    metadata_func=create_metadata,
    text_content=False
)

data = loader.load()
print(data)
