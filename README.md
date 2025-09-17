# Chatbot RAG Bappedalitbang Surabaya

Proyek ini adalah chatbot berbasis **RAG (Retrieval-Augmented Generation)** yang dirancang untuk menjawab pertanyaan seputar **Badan Perencanaan Pembangunan Daerah, Penelitian dan Pengembangan (Bappedalitbang) Kota Surabaya**. Chatbot mengambil informasi dari dokumen resmi hasil scraping, lalu memanfaatkan **FAISS Vector Database** + **LLM (Ollama llama3)** untuk menghasilkan jawaban yang akurat.  
Selain itu, chatbot ini juga bisa dihubungkan ke **WhatsApp** menggunakan **Baileys** agar lebih mudah diakses.

---

## Sumber Data yang Digunakan 
Menggunakan data yang berasal dari website official Badan Perencanaan Pembangunan Daerah, Penelitian dan Pengembangan (Bappedalitbang) Kota Surabaya dan website official Inovboyo.

## Fitur Utama
- **Pencarian Dokumen Otomatis** – Data hasil scraping (JSON) diubah menjadi *vector embeddings* agar chatbot bisa menemukan informasi relevan dengan cepat.  
- **RAG (Retrieval-Augmented Generation)** – Chatbot menjawab pertanyaan berdasarkan dokumen resmi terlebih dahulu, lalu fallback ke pengetahuan AI jika dokumen tidak memiliki jawabannya (dengan catatan verifikasi ulang).  
- **Integrasi WhatsApp** – Dengan bantuan **Baileys** + **FastAPI/Flask**, chatbot dapat dipanggil langsung melalui WhatsApp.  
- **Index Tersimpan** – Menggunakan FAISS, index dokumen bisa disimpan dan digunakan ulang tanpa harus membangun ulang setiap kali.

---
