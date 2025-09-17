import json
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# load data hasil scrape
with open("scraped_bappedalitbang.json", "r", encoding="utf-8") as f:
    scraped_data = json.load(f)

documents = []
for section, contents in scraped_data.items():
    for c in contents:
        documents.append({
            "section": section,
            "content": c
        })

print("Total dokumen:", len(documents))

# menggunakan HuggingFace Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# membuat vector DB
texts = [doc["content"] for doc in documents]
metadatas = [{"section": doc["section"]} for doc in documents]

vectorstore = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

# menyimpan index biar gak bikin ulang terus
vectorstore.save_local("bappedalitbang_index")
print("Index berhasil dibuat dan disimpan")