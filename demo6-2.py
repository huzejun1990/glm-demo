# @Author : huzejun
# @Time : 2025/4/2 20:33
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.tools import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
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

chain = create_sql | (lambda x: x.replace('```sql','').replace('```','')) | execute_sql

resp = chain.invoke({'question': '请问：一共有多个员工？'})

print(resp)

# resp = chian.invoke({'question':'请问：一共有多个员工？'})
# print('大语言模型生成的SQL: ' + resp)
# sql = resp.replace('```sql','').replace('```','')
# print('提取之后的SQL: ' + sql)
#
# print(db.run(sql))