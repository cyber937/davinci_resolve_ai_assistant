from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

def main():
    print("🧠 Loading vector index...")
    db = FAISS.load_local(
      folder_path="vector_index",
      embeddings=OpenAIEmbeddings(),
      allow_dangerous_deserialization=True
    )
    retriever = db.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
        retriever=retriever
    )

    print("✅ Ready! Ask a question about DaVinci Resolve.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("🗣️ You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = qa_chain.invoke(query)
        print("🤖 AI:", response)
        print("-" * 40)

if __name__ == "__main__":
    main()