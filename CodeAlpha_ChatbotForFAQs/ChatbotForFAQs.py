import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')


faq_data = [
    {"question": "How do I turn on the headphones?", "answer": "Press and hold the power button on the right ear cup for 3 seconds until the LED flashes blue."},
    {"question": "How can I pair with bluetooth?", "answer": "Enable Bluetooth on your device. On headphones, hold the power button for 5 seconds to enter pairing mode."},
    {"question": "What is the battery life?", "answer": "The headphones last up to 20 hours on a single charge with noise cancellation on."},
    {"question": "How do I reset the device?", "answer": "Hold the volume up and power button simultaneously for 10 seconds to factory reset."},
    {"question": "Is it water resistant?", "answer": "Yes, it is IPX4 rated, meaning it is resistant to sweat and light rain."},
    {"question": "What is the warranty period?", "answer": "We offer a 1-year limited warranty for manufacturing defects."},
    {"question": "Can I use it while charging?", "answer": "Yes, but we recommend letting it charge fully for better battery health."},
    {"question": "Does it have noise cancellation?", "answer": "Yes, it features Active Noise Cancellation (ANC) which can be toggled via the app."}
]

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

processed_questions = [preprocess_text(q) for q in questions]

def get_best_match(user_query):
    processed_input = preprocess_text(user_query)
    
    all_texts = processed_questions + [processed_input]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    user_vector = tfidf_matrix[-1]
    question_vectors = tfidf_matrix[:-1]
    similarity_scores = cosine_similarity(user_vector, question_vectors)
    
    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0, best_match_index]
    
    if best_score < 0.2: 
        return "I'm sorry, I don't understand that question. Could you rephrase it?"
    else:
        return answers[best_match_index]

st.set_page_config(page_title="FAQ Bot", page_icon="🤖")

st.title("🤖 AI FAQ Support Bot")
st.markdown("Ask me anything about the **Smart Headphones** product!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your question here..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = get_best_match(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.header("💡 Try asking about:")
    st.markdown("""
    - Battery life
    - Bluetooth pairing
    - Water resistance
    - Resetting the device
    - Warranty
    """)