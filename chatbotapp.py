import ollama

def chat_with_bot():
    messages = [
        {"role": "system", "content": "Kamu adalah chatbot AI yang menjawab pertanyaan tentang instansi saya yaitu badan perencanaan pembangunan daerah, penelitian dan pengembangan kota surabaya."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Sampai jumpa!")
            break

        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(model="llama3:8b", messages=messages)
        answer = response['message']['content']
        print("Bot:", answer)

        messages.append({"role": "assistant", "content": answer})

chat_with_bot()