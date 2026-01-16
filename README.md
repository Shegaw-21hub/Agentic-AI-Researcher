# Agentic-AI-Researcher: A Secure Agentic RAG System

## 🎯 Overview

**Agentic-AI-Researcher** is a specialized **Retrieval-Augmented Generation (RAG)** system designed to function as an autonomous research assistant. Unlike standard RAG systems that primarily retrieve and summarize information, this system employs an **Agentic Maker–Checker loop** to:

- Verify facts  
- Prevent hallucinations  
- Ensure all responses comply with strict safety protocols  

The system runs **entirely locally** using **Ollama (Llama 3.2)**, providing:

- 🔒 Full data privacy  
- 💸 Zero API costs  
- 🖥️ Offline-first operation  
## 🚀 Key Features

**Agentic Orchestration:** Uses a Maker-Checker architecture where a secondary agent critiques the primary agent's output.

**Safety-First Design:** Implements multi-layer guardrails (Input Validation, System Prompt Constraints, and Output Sanitization).

**Local Inference:** Powered by Ollama and FAISS for high-performance, private document retrieval.

**Self-Refinement:** The system automatically attempts to fix its own errors if the "Checker" agent identifies a hallucination or safety risk.

## 🏗️ System Architecture

The system follows a modular workflow:

- **Input Guardrail:** Scans queries for malicious intent or prompt injection.

- **Semantic Search:** Retrieves context from the local `knowledge_base.txt` using FAISS vector embeddings.

- **Maker Agent:** Synthesizes a response based strictly on the provided context.

- **Checker Agent:** Evaluates the response for:
  - **Grounding:** Is the answer supported by the text?
  - **Safety:** Does it violate any safety constraints?

- **Refinement:** If rejected, the Maker regenerates the answer using the Checker’s critique.
## 📁 Project Structure

Agentic-AI-Researcher/
├── data/
│   └── knowledge_base.txt      # The domain-specific knowledge file
├── src/
│   ├── __init__.py             # Makes 'src' a Python package
│   ├── safety.py               # Input/Output safety logic (Task 4)
│   ├── rag_engine.py           # Vector database & retrieval (Task 2)
│   └── agents.py               # Meta System Prompts & LLM chains (Task 1 & 3)
├── main.py                     # Entry point & Agentic loop (Task 3)
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files excluded from version control
└── README.md                   # Documentation
## 🛠️ Setup & Installation

### 1. Prerequisites

- **Python:** 3.10 or higher  
- **Ollama:** Install from [ollama.com](https://ollama.com)
### 2. Prepare the Model

Open your terminal/PowerShell and run:

```bash
ollama pull llama3.2
```
### 3. Clone and Install

```bash
## Clone the repository
git clone https://github.com/Shegaw-21hub/Agentic-AI-Researcher.git
cd Agentic-AI-Researcher
```
### Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate

```
### Install dependencies
pip install -r requirements.txt
```
## 🖥️ Usage

To start the AI Researcher Agent, run the `main.py` script:

```bash
python main.py
```
## 🛡️ Safety Measures (Assignment Task 4)

| Measure            | Implementation                              | Purpose                                                                 |
|--------------------|----------------------------------------------|-------------------------------------------------------------------------|
| Input Validation   | Regex-based sanitization in `safety.py`      | Prevents prompt injection and malicious commands.                       |
| Maker Constraint   | Meta System Prompt in `agents.py`            | Forces the agent to cite sources and stay in character.                 |
| Checker Loop       | Iterative review in `main.py`                | Catches hallucinations before the user sees them.                       |
| Output Scrubbing   | PII/Sensitive data filters in `safety.py`    | Ensures sensitive system info isn't leaked.                             |


## 📄 License

This project is submitted for **educational purposes** as part of an AI Research assignment.
