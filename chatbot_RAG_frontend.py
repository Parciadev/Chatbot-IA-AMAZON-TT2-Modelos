import streamlit as st
import chatbot_RAG_backend as demo

st.title("Hola, este es el chatbot UTEMSITO :sunglasses:")

if 'memory' not in st.session_state:
    with st.spinner("🔷Cargando, porfavor espere..."):
        st.session_state.memory = demo.hr_index()

if 'chat_history' not in st.session_state:
    with st.spinner("🔷Cargando, porfavor espere..."):
        st.session_state.chat_history=demo.demo_memory()

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

input_text =st.chat_input ("Chatea con utemsito aqui")

if input_text:

    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role":"user", "text":input_text})

    chat_response = demo.demo_conversation (input_text=input_text, memory=st.session_state.memory)

    with st.chat_message("assistant"):
        st.markdown(chat_response)
    
    st.session_state.chat_history.append({"role":"assistant", "text": chat_response})