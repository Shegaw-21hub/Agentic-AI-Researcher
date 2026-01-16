from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import os

def get_retriever():
    loader = TextLoader("data/knowledge_base.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)
    
    # Use local Ollama embeddings
    embeddings = OllamaEmbeddings(model="llama3.2")
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store.as_retriever()