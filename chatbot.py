import ollama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# load embeddings & vectorstore
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("bappedalitbang_index", embeddings, allow_dangerous_deserialization=True)

def chat_with_bot():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Sampai jumpa!")
            break

        # cari context dari vectorstore
        docs = vectorstore.similarity_search(user_input, k=7)  
        context = "\n\n".join([d.page_content for d in docs])

        # buat prompt dengan context
        prompt = f"""
        Kamu adalah chatbot AI yang menjawab pertanyaan tentang Badan Perencanaan Pembangunan Daerah, Penelitian dan Pengembangan (Bappedalitbang) Kota Surabaya. Kamu juga harus selalu menjawab dengan menggunakan bahasa indonesia.
        Berikut adalah informasi referensi dari dokumen resmi:

        {context}

        Pertanyaan pengguna: {user_input}
        Jawaban kamu harus berdasarkan informasi di atas, kalau tidak ada bilang tidak tahu.
        """

        response = ollama.chat(model="llama3:8b", messages=[{"role": "user", "content": prompt}])
        answer = response['message']['content']
        print("Bot:", answer)

chat_with_bot()