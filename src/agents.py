from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3.2", temperature=0)

def get_maker_chain():
    # Meta System Prompt: Defining roles and constraints
    prompt = ChatPromptTemplate.from_template("""
    ROLE: AI Researcher Agent (Maker)
    GOAL: Answer the user's question using ONLY the provided context.
    CONSTRAINTS: If you don't know, say you don't know. Do not hallucinate.
    
    CONTEXT: {context}
    QUESTION: {question}
    ANSWER:""")
    return prompt | llm | StrOutputParser()

def get_checker_chain():
    # Meta System Prompt: Defining roles and constraints
    prompt = ChatPromptTemplate.from_template("""
    ROLE: Safety & Correctness Checker
    GOAL: Verify if the Maker's answer is supported by the context and is safe.
    
    QUESTION: {question}
    MAKER_ANSWER: {answer}
    
    RESPONSE: Return 'PASS' if correct/safe, otherwise explain why it failed.
    """)
    return prompt | llm | StrOutputParser()