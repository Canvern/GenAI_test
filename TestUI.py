#Import langchain dependencies
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Bring in stream lit for UI dev
import streamlit as st
#Bring in watsonx interface
from wastonxlangchain import LangChainInterface

#Set up the app title
st.title('Ask watsonx')

#Build a prompt input template to display the prompts
prompt = st.chat_input('Pass your prompt here')

# If the user hits enter then
if prompt:
    #Display the prompt
    st.chat_message('user').markdown(prompt)
