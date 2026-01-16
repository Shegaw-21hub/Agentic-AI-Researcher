from src.safety import validate_input, sanitize_output
from src.rag_engine import get_retriever
from src.agents import get_maker_chain, get_checker_chain, llm

def run_agentic_rag(user_query: str):
    # 1. Input Safety
    if not validate_input(user_query):
        return "Error: Malicious or invalid query detected."

    # 2. Retrieval
    retriever = get_retriever()
    docs = retriever.invoke(user_query)
    context = "\n".join([d.page_content for d in docs])

    # 3. Maker-Checker Loop
    maker = get_maker_chain()
    checker = get_checker_chain()

    print("--- Maker: Generating initial answer ---")
    draft = maker.invoke({"context": context, "question": user_query})

    print("--- Checker: Verifying answer ---")
    check_result = checker.invoke({"question": user_query, "answer": draft})

    if "PASS" in check_result:
        final_answer = draft
    else:
        print(f"--- Refinement needed: {check_result} ---")
        # Refine if checker finds issues
        refine_prompt = f"Context: {context}\nRefine this answer based on: {check_result}\nAnswer: {draft}"
        final_answer = llm.invoke(refine_prompt).content

    # 4. Final Output Sanitization
    return sanitize_output(final_answer)

if __name__ == "__main__":
    query = input("Enter your research question: ")
    print("\nFINAL RESULT:\n", run_agentic_rag(query))