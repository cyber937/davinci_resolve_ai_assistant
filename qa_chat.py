import os
import textwrap
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

def format_response(text: str, width: int = 80) -> str:
    """整形された回答を返す"""
    return textwrap.fill(text.strip(), width=width)

def main():
    print("🧠 Loading vector index...")
    try:
        db = FAISS.load_local(
            folder_path="vector_index",
            embeddings=OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY")),
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        print(f"❌ Failed to load vector index: {e}")
        return

    retriever = db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4", temperature=0),
        retriever=retriever
    )

    print("✅ Ready! Ask a question about DaVinci Resolve.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("🗣️ You: ").strip()
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        if not query:
            continue  # 空入力を無視

        try:
            response = qa_chain.invoke({"query": query})
            result = response.get("result", "No result found.")
            formatted = format_response(result)
            print("\n🤖 AI Response:\n")
            print(formatted)
        except Exception as e:
            print(f"⚠️ Error during query: {e}")

        print("-" * 50)

if __name__ == "__main__":
    main()