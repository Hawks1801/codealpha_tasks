# 🤖 FAQ Chatbot (NLP & Cosine Similarity)

A smart FAQ chatbot built using **Python**, **NLTK**, and **Scikit-Learn**. It uses **Cosine Similarity** and **TF-IDF** vectorization to match user queries with the most relevant questions in the database, wrapped in a modern **Streamlit** chat interface.

## 🚀 Features

* **Intelligent Matching:** Uses NLP (TF-IDF & Cosine Similarity) to understand user questions even if they aren't worded exactly like the database.
* **Preprocessing Pipeline:** Tokenization, stopword removal, and punctuation cleaning for better accuracy.
* **Chat Interface:** A clean, persistent chat history UI using Streamlit.
* **Confidence Threshold:** Returns a fallback message if the user's question doesn't match any known topic.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Interface:** Streamlit
* **NLP Library:** NLTK (Natural Language Toolkit)
* **Machine Learning:** Scikit-Learn (for Vectorization and Similarity calculation)

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/faq-chatbot.git](https://github.com/Hawks1801/faq-chatbot.git)
cd faq-chatbot