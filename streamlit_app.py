from database.kpi_query import (
    get_user_count,
    get_order_count,
    get_gmv,
    get_roi
)
import streamlit as st

from agent.growth_agent import ask_growth_agent


# ==========================
# 页面配置
# ==========================

st.set_page_config(

    page_title="AI Growth Agent",

    page_icon="🚀",

    layout="wide"

)



# ==========================
# 标题
# ==========================


st.title("🚀 AI Growth Intelligence Dashboard")

st.caption(
    "SQL Agent + RAG Knowledge + DeepSeek"
)



# ==========================
# KPI区域
# ==========================


col1, col2, col3, col4 = st.columns(4)


with col1:

    users = get_user_count()

orders = get_order_count()

gmv = get_gmv()

roi = get_roi()



col1,col2,col3,col4 = st.columns(4)



with col1:

    st.metric(
        "用户数量",
        users
    )



with col2:

    st.metric(
        "订单数量",
        orders
    )



with col3:

    st.metric(
        "GMV",
        f"¥{gmv}"
    )



with col4:

    st.metric(
        "ROI",
        roi
    )


st.divider()



# ==========================
# 输入区域
# ==========================


st.subheader(
    "🧠 AI增长分析"
)


question = st.text_input(

    "请输入业务问题",

    placeholder=
    "例如：哪个渠道ROI最低？"

)



if st.button(
    "开始分析",
    type="primary"
):


    if question:


        with st.spinner(
            "AI正在分析数据库和知识库..."
        ):


            result = ask_growth_agent(
                question
            )


        st.success(
            "分析完成"
        )


        st.markdown(
            "## 📌 AI分析报告"
        )


        st.write(
            result
        )


    else:

        st.warning(
            "请输入问题"
        )



# ==========================
# Footer
# ==========================


st.divider()

st.caption(
    "Powered by LangChain + DeepSeek + MySQL + FAISS"
)