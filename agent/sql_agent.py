# ======================================
# SQL Agent
# DeepSeek + LangChain + MySQL
# ======================================


from langchain_community.utilities import SQLDatabase

from langchain_openai import ChatOpenAI

from langchain_community.agent_toolkits import create_sql_agent



# ======================================
# 1. MySQL数据库连接
# ======================================

db = SQLDatabase.from_uri(

    "mysql+pymysql://root:你的密码@localhost:3306/growth_agent?charset=utf8mb4&use_unicode=1"

)



# ======================================
# 2. DeepSeek大模型
# ======================================


llm = ChatOpenAI(

    model="deepseek-chat",

    temperature=0,

    api_key="DEEPSEEK_API_KEY",

    base_url="https://api.deepseek.com",
    
    max_tokens=2048

)



# ======================================
# 3. 创建SQL Agent
# ======================================


agent = create_sql_agent(

    llm=llm,

    db=db,

    verbose=True,
   agent_type="tool-calling",

    handle_parsing_errors=True

)




