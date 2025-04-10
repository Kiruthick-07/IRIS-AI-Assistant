from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama  
import streamlit as st

st.title=("IRIS CHATBOT")
in_txt = st.text_input("Hello There,I am IRIS,How can I help you today?")

prompt = ChatPromptTemplate.from_messages([("system" , "you are a helpful AI assistant. Your name is IRIS (Innovative Robust Intelligent System). You are developed by KIRUTHICK R. Limit your answer to 2-3 lines and try to respond like an human"),("user", "User query:{query}")])

llm = Ollama(model="llama3.2:3b")
par=StrOutputParser()
chain = prompt|llm|par

if in_txt:
    st.write(chain.invoke({"query":in_txt}))