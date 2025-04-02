# @Author : huzejun
# @Time : 2025/4/2 20:57
from operator import itemgetter

from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.tools import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

# sqlalchemy 初始化MySQL数据库的连接
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db2024'
USERNAME = 'root'
PASSWORD = '123456'
# mysqlclient驱动URL
MYSQL_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# sqlalchemy 初始化mysql数据库的连接
# HOSTNAME = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'db2024'
# USERNAME = 'root'
# PASSWORD = '123456'
# # mysqlclient驱动URL
# MYSQL_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

model = ChatOpenAI(
    model='glm-4-0520',
    # temperature=0,
    api_key='我的key',
    base_url='https://open.bigmodel.cn/api/paas/v4/'
)

db = SQLDatabase.from_uri(MYSQL_URI)

create_sql = create_sql_query_chain(llm=model, db=db)

execute_sql = QuerySQLDataBaseTool(db=db)   #langchain内置的工具

create_sql = create_sql | (lambda x: x.replace('```sql', '').replace('```', ''))

# chain = create_sql | (lambda x: x.replace('```sql','').replace('```','')) | execute_sql


# resp = chain.invoke({'question': '请问：一共有多个员工？'})

answer_prompt = PromptTemplate.from_template(
    """Give the following user question, corresponding SQL query, and SQL result, answer the user question. 用中文回答最终答案
    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
)

answer_chain = answer_prompt | model | StrOutputParser()

chain = RunnablePassthrough.assign(query=create_sql).assign(result=itemgetter('query') | execute_sql) | answer_chain

resp1 = chain.invoke({'question': '请问：一共有多个员工？'})
print(resp1)

# resp = chain.invoke({'question': '请问：哪个员工的年龄最大？并且返回该员工的年龄'})
resp2 = chain.invoke({'question': '请问：哪个员工的年龄最大？'})
print(resp2)

# resp = chain.invoke({'question': '请问：一共有多个员工？'})
# print(resp)