import streamlit as st
import re

st.title("Tratador de Quebras de Linha (PDF)")

texto = st.text_area("Cole o texto aqui:", height=300)

def tratar_texto(t):
    # Remove quebras de linha que NÃO venham depois de um ponto
    return re.sub(r'(?<!\.)\n', ' ', t)

if st.button("Tratar texto"):
    saida = tratar_texto(texto)
    st.text_area("Texto tratado:", saida, height=300)
    st.text("Agora basta selecionar e copiar o texto tratado!")
