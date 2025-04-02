# @Author : huzejun
# @Time : 2025/3/31 21:34
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.storage import sql
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

# print(db.dialect)
# print(db.get_usable_table_names())
# print(db.run('select * from t_user;')) # SELECT * FROM t_user;
# print(db.run('SELECT * FROM USER'))

# t_dept,t_emp,t_id_card,t_person,t_role,t_test1,t_user,t_user_role

chian = create_sql_query_chain(llm=model,db=db)
# chian.get_prompts()[0].pretty_print()
resp = chian.invoke({'question':'请问：一共有多个员工？'})
print('大语言模型生成的SQL: ' + resp)
sql = resp.replace('```sql','').replace('```','')
# sql = resp.replace('sql','').replace('','')
print('提取之后的SQL: ' + sql)
print(db.run(sql))