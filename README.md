# 🎬 DaVinci Resolve AI Assistant

An AI-powered question-answering tool based on the DaVinci Resolve official manual.  
Built with LangChain, OpenAI, and FAISS.

## 🧠 What it does

- Loads the official DaVinci Resolve PDF manual
- Splits it into searchable chunks
- Embeds and indexes it using FAISS
- Lets you ask questions via ChatGPT (CLI interface)

## 🚀 Quick Start

### 1. Download the Resolve manual PDF (optional)

You can download the official DaVinci Resolve 20 New Features Guide directly from Blackmagic Design:

```bash
curl -o DaVinci_Resolve_20_Reference_Manual.pdf https://documents.blackmagicdesign.com/UserManuals/DaVinci_Resolve_20_Reference_Manual.pdf
```

### 2. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/resolve-assistant.git
cd resolve-assistant
```

### 3. Set up a virtual environment

```bash
python3 -m venv rag-env
source rag-env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Export your OpenAI API key

```bash
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 6. Extract and index the Resolve manual

Place the official PDF (e.g. DaVinci_Resolve_18_Manual.pdf) into the folder.

```bash
python extract_text.py
python build_index.py
```

### 7. Ask your questions!

```bash
python qa_chat.py
```

## 💡 Example questions

• How do I export ProRes?
• What’s the difference between Edit and Cut pages?
• How can I use Fusion for compositing?

## 🛠 Tech Stack

• Python 3.10+
• LangChain
• OpenAI API
• FAISS (local vector DB)
• CLI Interface (Streamlit or macOS UI coming soon)

## 📄 License

MIT
