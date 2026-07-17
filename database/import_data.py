import pandas as pd
from sqlalchemy import create_engine
import os



# ============================
# MySQL配置
# ============================

USER = "root"

PASSWORD = "你的密码"

HOST = "localhost"

PORT = "3306"

DATABASE = "growth_agent"



engine = create_engine(

    f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

)



# ============================
# CSV路径
# ============================

DATA_PATH = "E:\AI-Growth-Agent\data"



tables = [

    "users",

    "products",

    "orders",

    "campaigns",

    "marketing",

    "user_behavior",

    "customer_service"

]



# ============================
# 导入
# ============================


for table in tables:


    file_path = os.path.join(

        DATA_PATH,

        table + ".csv"

    )


    print(
        f"Loading {file_path}"
    )


    df = pd.read_csv(
        file_path
    )


    # 日期字段处理

    for col in df.columns:

        if "date" in col.lower():

            df[col] = pd.to_datetime(
                df[col]
            )

        if col == "date":

            df[col] = pd.to_datetime(
                df[col]
            )



    df.to_sql(

        name=table,

        con=engine,

        if_exists="replace",

        index=False

    )


    print(

        f"{table} import success : {len(df)} rows"

    )



print("\nAll tables imported successfully!")