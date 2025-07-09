from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os

print("Loading text...")
with open("resolve_manual.txt", "r", encoding="utf-8") as f:
    text = f.read()

# チャンクに分割
print("Splitting text into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " ", ""]
)
docs = splitter.create_documents([text])

# ベクトル化
print(f"Total chunks: {len(docs)}")
print("Embedding and saving index...")

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

# 保存
db.save_local("vector_index")
print("✅ Index created and saved to 'vector_index/'")