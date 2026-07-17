# ======================================
# KPI Data Query
# MySQL实时指标
# ======================================


from sqlalchemy import create_engine
import pandas as pd



# MySQL连接

engine = create_engine(

    "mysql+pymysql://root:你的密码@localhost:3306/growth_agent?charset=utf8mb4"

)



# ===============================
# 用户数量
# ===============================

def get_user_count():

    sql = """

    SELECT COUNT(*) AS users

    FROM users

    """

    df = pd.read_sql(
        sql,
        engine
    )

    return int(
        df["users"][0]
    )



# ===============================
# 订单数量
# ===============================

def get_order_count():

    sql="""

    SELECT COUNT(*) AS orders

    FROM orders

    """

    df=pd.read_sql(

        sql,

        engine

    )


    return int(
        df["orders"][0]
    )



# ===============================
# GMV
# ===============================

def get_gmv():

    sql="""

    SELECT SUM(amount) AS gmv

    FROM orders

    """

    df=pd.read_sql(

        sql,

        engine

    )


    return round(

        float(df["gmv"][0]),

        2

    )



# ===============================
# ROI
# ===============================

def get_roi():

    sql="""

    SELECT

    SUM(revenue)/SUM(cost) AS roi

    FROM campaigns

    """

    df=pd.read_sql(

        sql,

        engine

    )


    return round(

        float(df["roi"][0]),

        2

    )