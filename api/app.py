
# import streamlit
# from fact_checker import load_local_llm, fact_check
# from retrieval import Retriever

# # --- Page configuration ---
# st.set_page_config(page_title="M2F2 - Tim Walz", page_icon="favicon.ico")

# st.image("Tim_Walz.jpg", width=130)
# st.title("💬 M2F2 Tim Walz")
# st.write("Ask a question about Governor Tim Walz")

# # --- Initialize chat history in session state ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display the conversation history.
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# # --- Load the FAISS retriever and local model pipeline (once) ---
# if "retriever" not in st.session_state:
#     st.session_state.retriever = Retriever()  # This loads faiss_index.bin and statements.pkl

# if "pipeline" not in st.session_state:
#     st.session_state.pipeline = load_local_llm("my_local_model")

# # --- User input ---
# user_input = st.text_input("You:", "", key="user_input")

# # --- Process input when "Send" is clicked ---
# if st.button("Send") and user_input:
#     # Save the user's message.
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.write(user_input)
    
#     # Get the model's answer using our fact_check function.
#     answer, _ = fact_check(user_input, st.session_state.retriever, st.session_state.pipeline)
    
#     # Save and display the assistant's answer.
#     st.session_state.messages.append({"role": "assistant", "content": answer})
#     with st.chat_message("assistant"):
#         st.write(answer)

# # --- Option to clear the chat ---
# if st.button("Clear Chat"):
#     st.session_state.messages = []
#     st.experimental_rerun()
import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from fact_checker import load_local_llm, fact_check
from retrieval import Retriever

# --- Page configuration ---
st.set_page_config(page_title="M2F2 - Tim Walz", page_icon="favicon.ico")

st.image("Tim_Walz.jpg", width=130)
st.title("💬 M2F2 Tim Walz")
st.write("Ask a question about Governor Tim Walz")

# --- Initialize chat history in session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the conversation history.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- Load the FAISS retriever and local model pipeline (once) ---
if "retriever" not in st.session_state:
    st.session_state.retriever = Retriever()  # This loads faiss_index.bin and statements.pkl

if "pipeline" not in st.session_state:
    st.session_state.pipeline = load_local_llm("my_local_model")

# --- Speech-to-Text (Browser-Based) ---
st.write("Click the 🎤 Speak button and start speaking...")

# JavaScript Speech-to-Text
spoken_text = streamlit_js_eval(
    js_expressions="new Promise((resolve) => { const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)(); recognition.lang = 'en-US'; recognition.interimResults = false; recognition.maxAlternatives = 1; recognition.onresult = (event) => resolve(event.results[0][0].transcript); recognition.start(); })",
    key="speech"
)

# --- User input (Text or Speech) ---
user_input = st.text_input("You:", spoken_text if spoken_text else "", key="user_input")

# --- Process input when "Send" is clicked ---
if st.button("Send") and user_input:
    # Save the user's message.
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get the model's answer using our fact_check function.
    answer, _ = fact_check(user_input, st.session_state.retriever, st.session_state.pipeline)
    
    # Save and display the assistant's answer.
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)

# --- Option to clear the chat ---
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()