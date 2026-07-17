# ======================================
# Growth Workflow Agent
# SQL Agent + RAG Agent + DeepSeek
# ======================================


from langchain_openai import ChatOpenAI


# SQL Agent

from agent.sql_agent import agent as sql_agent


# RAG Agent

from agent.rag_agent import qa as rag_agent




# ======================================
# DeepSeek LLM
# ======================================


llm = ChatOpenAI(

    model="deepseek-chat",

    api_key="DEEPSEEK_API_KEY",

    base_url="https://api.deepseek.com",

    temperature=0

)




# ======================================
# Question Router
# ======================================


def route_question(question):


    sql_keywords = [

        "多少",
        "数量",
        "用户",
        "订单",
        "销售",
        "GMV",
        "收入",
        "ROI",
        "渠道",
        "增长",
        "下降",
        "最高",
        "最低"

    ]


    rag_keywords = [

        "规则",
        "原因",
        "策略",
        "怎么办",
        "什么是",
        "如何",
        "建议"

    ]



    need_sql = False

    need_rag = False



    for word in sql_keywords:

        if word in question:

            need_sql = True



    for word in rag_keywords:

        if word in question:

            need_rag = True



    if need_sql and need_rag:

        return "both"



    elif need_sql:

        return "sql"



    else:

        return "rag"





# ======================================
# Core Growth Agent
# ======================================


def growth_agent(question):


    route = route_question(question)



    print("\n====== Agent Route ======")

    print(route)



    context = []



    # ----------------------
    # SQL Analysis
    # ----------------------


    if route in ["sql", "both"]:


        sql_result = sql_agent.invoke(

            {

                "input": question

            }

        )


        context.append(

            "【数据库分析结果】\n"

            +

            sql_result["output"]

        )




    # ----------------------
    # RAG Knowledge
    # ----------------------


    if route in ["rag", "both"]:


        rag_result = rag_agent.invoke(

            {

                "query": question

            }

        )


        context.append(

            "【知识库信息】\n"

            +

            str(rag_result)

        )




    # ----------------------
    # DeepSeek Summary
    # ----------------------


    prompt = f"""


你是一名互联网增长分析专家。


请结合业务数据和知识库规则分析用户问题。


输出格式：


【业务判断】

说明核心结论。


【数据依据】

引用数据库或知识库信息。


【原因分析】

分析造成问题的原因。


【优化建议】

给出可执行增长策略。



参考信息：

{context}



用户问题：

{question}


"""



    response = llm.invoke(prompt)



    return response.content





# ======================================
# Streamlit Interface
# ======================================


def ask_growth_agent(question):


    return growth_agent(question)








        