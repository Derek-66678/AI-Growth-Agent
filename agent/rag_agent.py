# ======================================
# RAG Knowledge Agent
# DeepSeek + Chroma
# ======================================


from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI

from langchain_classic.chains import RetrievalQA



# ===============================
# 1. 加载知识库
# ===============================


loader = TextLoader(
    "E:\AI-Growth-Agent\knowledge\product_rules.txt.txt",
    encoding="utf-8"
)

documents = loader.load()



# ===============================
# 2. 文本切分
# ===============================


splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50

)


docs = splitter.split_documents(documents)



# ===============================
# 3. 创建Embedding
# ===============================


embedding = HuggingFaceEmbeddings(

    model_name="BAAI/bge-small-zh"

)


# ===============================
# 4. 创建向量数据库
# ===============================


vectorstore = FAISS.from_documents(

    docs,

    embedding

    )



# ===============================
# 5. DeepSeek
# ===============================


llm = ChatOpenAI(

    model="deepseek-chat",

    api_key="DEEPSEEK_API_KEY",

    base_url="https://api.deepseek.com",

    temperature=0

)



# ===============================
# 6. 创建RAG
# ===============================


qa = RetrievalQA.from_chain_type(

    llm=llm,

    retriever=vectorstore.as_retriever(),

    chain_type="stuff"

)




